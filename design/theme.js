/* Enhancement only. Links, research records and disclosures work without JS.
   An inline script in <head> applies a saved theme before first paint; this
   file wires the theme control and opens a method step named in the URL. */
const root = document.documentElement;
const control = document.querySelector('#theme-toggle');
const preference = matchMedia('(prefers-color-scheme: dark)');
const isInk = () => root.dataset.theme ? root.dataset.theme === 'ink' : preference.matches;
if (control) {
  const label = () => {
    control.setAttribute('aria-label', isInk() ? 'Use paper theme' : 'Use ink theme');
    control.title = isInk() ? 'Use paper theme' : 'Use ink theme';
  };
  control.hidden = false;
  label();
  control.addEventListener('click', () => {
    root.dataset.theme = isInk() ? 'paper' : 'ink';
    try { localStorage.setItem('pureland-theme', root.dataset.theme); } catch { /* Storage is optional. */ }
    label();
  });
  if (preference.addEventListener) preference.addEventListener('change', label);
}
/* A link to a step, such as index.html#step-attend, shows the step's copy and not only its summary line. */
const reveal = () => {
  const target = location.hash.length > 1 && document.getElementById(location.hash.slice(1));
  if (target && target.tagName === 'DETAILS') target.open = true;
};
reveal();
addEventListener('hashchange', reveal);
