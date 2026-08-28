# Contributing

PureLand needs documented disagreement more than applause.

## Useful contributions

- a field-test proposal in public-safe, general terms;
- a rights-cleared field report after the private review stage;
- a case where a category failed or caused harm;
- a correction to a source or a claim;
- a clearer consent boundary;
- an accessibility or translation improvement;
- an adaptation that states what changed and why.

Do not submit participant material, direct or indirect identifying data, confidential or client records, protected community knowledge, consent records, or content you lack the authority to license. Anonymization does not settle re-identification risk or publication authority.

## Process

1. Open an issue describing the context and the proposed change in public-safe terms.
2. Fork from the current main branch.
3. Make one bounded change and update the relevant provenance or research-status entry.
4. Run `python3 -m pip install -r requirements.txt`, then `python3 scripts/check_repo.py`.
5. Submit a pull request using the template.

 A field-test record submitted as JSON has to clear the data boundary first. Read [data/README.md](data/README.md): it says what may not be committed and points at the schema the record must validate against.

For a field test involving participant, client, confidential, community-held, or identifying material, the public issue is Stage 1 scoping only. Do not add evidence links or protected details. Stage 2 begins only after the maintainer establishes an appropriate private review channel and confirms the rights basis. See [RIGHTS-AND-CONSENT.md](RIGHTS-AND-CONSENT.md).

If a correction or takedown request contains protected information, follow [SECURITY.md](SECURITY.md). A public issue may request a private channel but must not describe the protected material.

By submitting original repository content, you agree to license that contribution under CC BY-SA 4.0. This does not cover third-party or participant material.

Maintainer decisions follow [GOVERNANCE.md](GOVERNANCE.md). Pull requests must identify affected people, the rights and consent basis, new exposure or burden, unresolved disagreement, the public-safe review, and the status of each claim under the vocabulary in [RESEARCH-STATUS.md](RESEARCH-STATUS.md), which separates a source-backed claim from PureLand synthesis and from a claim derived from practice with no text behind it. Critique the method and the decisions. Do not diagnose contributors with contemplative categories, and do not attack anyone's identity.
