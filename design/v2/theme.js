/* Enhancement only. Links, research records and disclosures work without JS. */
const root = document.documentElement;
const control = document.querySelector('#theme-toggle');
const preference = matchMedia('(prefers-color-scheme: dark)');
let saved = null;
try { saved = localStorage.getItem('pureland-v2-theme'); } catch { /* Session choice still works. */ }
if (saved === 'paper' || saved === 'ink') root.dataset.theme = saved;
const isInk = () => root.dataset.theme ? root.dataset.theme === 'ink' : preference.matches;
const label = () => {
  control.setAttribute('aria-label', isInk() ? 'Use paper theme' : 'Use ink theme');
  control.title = isInk() ? 'Use paper theme' : 'Use ink theme';
};
if (control) {
  control.hidden = false;
  label();
  control.addEventListener('click', () => {
    root.dataset.theme = isInk() ? 'paper' : 'ink';
    try { localStorage.setItem('pureland-v2-theme', root.dataset.theme); } catch { /* Storage is optional. */ }
    label();
  });
  preference.addEventListener('change', label);
}
