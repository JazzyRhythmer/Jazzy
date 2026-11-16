export function setupMotion(toggle) {
  const media = matchMedia('(prefers-reduced-motion: reduce)');
  const key = 'jazzy-motion', images = new Map(), prepared = new Map();
  let preference = null;
  try { preference = sessionStorage.getItem(key); } catch {}
  const enabled = () => preference === null ? !media.matches : preference === 'on';
  function prepare(src) {
    if (!prepared.has(src)) prepared.set(src, new Promise(resolve => {
      const image = new Image();
      image.onload = () => resolve(true);
      image.onerror = () => resolve(false);
      image.src = src;
    }));
    return prepared.get(src);
  }
  async function syncImage(img, visible) {
    const state = images.get(img);
    if (!state || img.dataset.ready !== 'true') return;
    const source = enabled() && visible && !state.failed ? img.dataset.motion : img.dataset.still;
    const token = ++state.token;
    // Keep the current decoded frame while the next source downloads.
    if (!source || img.getAttribute('src') === source) return;
    const ready = await prepare(source);
    if (!images.has(img) || state.token !== token) return;
    if (ready) img.src = source;
    else if (source === img.dataset.motion) { state.failed = true; syncImage(img, visible); }
  }
  const observer = typeof IntersectionObserver === 'undefined' ? null : new IntersectionObserver(entries => {
    for (const {target, isIntersecting} of entries) {
      const state = images.get(target);
      if (!state) continue;
      state.visible = isIntersecting;
      syncImage(target, isIntersecting);
    }
  });
  function sync() {
    for (const [img, state] of images) syncImage(img, state.visible);
    toggle.textContent = enabled() ? 'Pause animations' : 'Play animations';
    toggle.setAttribute('aria-pressed', String(!enabled()));
  }
  toggle.addEventListener('click', () => {
    preference = enabled() ? 'off' : 'on';
    try { sessionStorage.setItem(key, preference); } catch {}
    sync();
  });
  media.addEventListener('change', sync);
  addEventListener('pageshow', () => { try { preference = sessionStorage.getItem(key); } catch {} sync(); });
  sync();
  return {
    add(img, visibleOnly = false) {
      img.dataset.still ||= img.getAttribute('src');
      const loaded = () => { if (img.naturalWidth) img.dataset.ready = 'true'; };
      const error = () => { img.dataset.ready = 'error'; };
      img.addEventListener('load', loaded); img.addEventListener('error', error);
      loaded();
      const visible = !visibleOnly || !observer;
      images.set(img, {visible, token: 0, failed: false, loaded, error});
      if (!visible) observer.observe(img);
      // Let the initial still finish before requesting its animated replacement.
      if (img.complete && img.naturalWidth) syncImage(img, visible);
      else img.addEventListener('load', () => { const state=images.get(img); if(state) syncImage(img,state.visible); }, {once:true});
    },
    remove(img) {
      const state=images.get(img);
      if(state){ img.removeEventListener('load',state.loaded); img.removeEventListener('error',state.error); }
      images.delete(img); observer?.unobserve(img);
    },
  };
}
