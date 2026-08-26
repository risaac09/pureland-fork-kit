#!/usr/bin/env bash
# llm-lane.sh: shell functions for the open-model lane (OPEN-MODEL-LANE.md).
#
# License: MIT (see LICENSES/MIT.txt).
#
# This is an example to adapt, not a turnkey tool. Replace the model name,
# host, and port below with your own. Source it from your shell profile:
#
#   source /path/to/llm-lane.sh
#
# It provides three functions:
#   llm-lane-start : start an on-demand large model on this machine (tier 2)
#   llm-lane-stop  : stop it and confirm the port is free
#   llm-lane-small : point LLM_BASE_URL at an always-on small model (tier 1)
#
# Requires llama-server (llama.cpp) on PATH for tier 2. Any OpenAI-compatible
# server works for tier 1; this script only points at it.

# ── Settings to replace ─────────────────────────────────────────────────
# Tier 2: the on-demand model served on THIS machine, localhost only.
LLM_LANE_MODEL="${LLM_LANE_MODEL:-example-org/example-model-30B-GGUF:Q4_K_M}"
LLM_LANE_HOST="127.0.0.1"   # never 0.0.0.0: personal on-demand use, no LAN exposure
LLM_LANE_PORT="${LLM_LANE_PORT:-8080}"
# Tier 1: the always-on small model on a spare machine.
LLM_LANE_SMALL_URL="${LLM_LANE_SMALL_URL:-http://workshop.local:8080}"

# Servers default to the model's full trained context length. The memory for
# that context, on top of the quantized weights, can exceed physical RAM the
# moment a real prompt arrives: an out-of-memory crash mid-generation, not at
# load time. Set a size that fits your machine and your actual use.
LLM_LANE_CTX_SIZE="${LLM_LANE_CTX_SIZE:-8192}"

# Own subdirectory, not a shared temp dir: in a world-writable directory a
# fixed-name PID file can collide with another tool's or another user's file,
# so llm-lane-stop could signal a process that was never ours. A private
# directory closes that path. It does not close PID recycling: if the server
# dies out-of-band and the OS reuses the number, the stale file points at an
# unrelated process, and no tool reading it can tell. If you know the server
# died outside llm-lane-stop, delete the PID file instead of trusting it.
LLM_LANE_DIR="${TMPDIR:-$HOME/.cache}/llm-lane"
LLM_LANE_LOG="$LLM_LANE_DIR/llama-server.log"
LLM_LANE_PID_FILE="$LLM_LANE_DIR/llama-server.pid"

# ── Tier 2: on-demand large model ───────────────────────────────────────
# Deliberately NOT a persistent service. On unified-memory machines a large
# resident model starves every other memory-hungry application. Do not wire
# this into launchd/systemd; start it when needed, stop it when done.
llm-lane-start() {
  local pid=""
  mkdir -p "$LLM_LANE_DIR"
  [ -f "$LLM_LANE_PID_FILE" ] && pid="$(cat "$LLM_LANE_PID_FILE")"
  if [ -n "$pid" ] && kill -0 "$pid" 2>/dev/null; then
    echo "llm-lane-start: already running (PID $pid)"
    export LLM_BASE_URL="http://localhost:${LLM_LANE_PORT}"
    return 0
  fi
  if ! command -v llama-server >/dev/null 2>&1; then
    echo "llm-lane-start: llama-server not found on PATH" >&2
    return 1
  fi
  echo "llm-lane-start: launching llama-server (${LLM_LANE_MODEL}) on ${LLM_LANE_HOST}:${LLM_LANE_PORT}..."
  nohup llama-server -hf "$LLM_LANE_MODEL" --host "$LLM_LANE_HOST" --port "$LLM_LANE_PORT" \
    --ctx-size "$LLM_LANE_CTX_SIZE" \
    > "$LLM_LANE_LOG" 2>&1 &
  pid=$!
  echo "$pid" > "$LLM_LANE_PID_FILE"
  export LLM_BASE_URL="http://localhost:${LLM_LANE_PORT}"
  echo "llm-lane-start: PID $pid; log: $LLM_LANE_LOG; LLM_BASE_URL=$LLM_BASE_URL"
  echo "llm-lane-start: first run downloads the model, which can take a while; tail -f $LLM_LANE_LOG to watch."
}

llm-lane-stop() {
  if [ -f "$LLM_LANE_PID_FILE" ]; then
    local pid waited=0
    pid="$(cat "$LLM_LANE_PID_FILE")"
    if kill -0 "$pid" 2>/dev/null; then
      kill "$pid"
      echo "llm-lane-stop: sent SIGTERM to PID $pid"
      # Signal handling plus socket teardown takes nonzero time; wait briefly
      # instead of racing the port check below.
      while kill -0 "$pid" 2>/dev/null && [ "$waited" -lt 5 ]; do
        sleep 1
        waited=$((waited + 1))
      done
      if kill -0 "$pid" 2>/dev/null; then
        # Keep the PID file: it is the only record of the process still
        # holding the port, and a second llm-lane-stop needs it.
        echo "llm-lane-stop: WARNING PID $pid still alive after ${waited}s; keeping $LLM_LANE_PID_FILE"
      else
        echo "llm-lane-stop: stopped PID $pid"
        rm -f "$LLM_LANE_PID_FILE"
      fi
    else
      echo "llm-lane-stop: PID $pid not running"
      rm -f "$LLM_LANE_PID_FILE"
    fi
  else
    echo "llm-lane-stop: no PID file found"
  fi
  unset LLM_BASE_URL
  if ! command -v lsof >/dev/null 2>&1; then
    echo "llm-lane-stop: lsof not available, could not verify :${LLM_LANE_PORT} is free"
  elif lsof -i ":${LLM_LANE_PORT}" >/dev/null 2>&1; then
    echo "llm-lane-stop: WARNING something is still listening on :${LLM_LANE_PORT}"
  else
    echo "llm-lane-stop: confirmed nothing on :${LLM_LANE_PORT}"
  fi
}

# ── Tier 1: always-on small model ───────────────────────────────────────
# Low-impact work only: conversion, summarization, bulk classification, rough
# drafts. Audit-class and voice-gated work stays above the quality floor.
#
# Use it in single-shot microprompts, not a running chat: one system+user
# message, one completion, session over. A small model's quality drops fast
# once history accumulates across turns. A multi-step task should be several
# short calls, each a fresh exchange.
llm-lane-small() {
  export LLM_BASE_URL="$LLM_LANE_SMALL_URL"
  if curl -s -m 3 "${LLM_LANE_SMALL_URL}/v1/models" >/dev/null; then
    echo "llm-lane-small: LLM_BASE_URL=$LLM_BASE_URL (server reachable)"
  else
    echo "llm-lane-small: WARNING ${LLM_LANE_SMALL_URL} not answering; LLM_BASE_URL set anyway"
  fi
}
