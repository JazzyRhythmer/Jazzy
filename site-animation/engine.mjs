import { engines } from './catalog.mjs?v=20261111.1';
import { setupMotion } from './motion.mjs?v=20261117.1';

const el = id => document.getElementById(id);
const model = new URLSearchParams(location.search).get('model');
const slug = model === 'hort-drum' ? 'hortator' : model === 'serum' ? 'wavetable' : model;
const index = engines.findIndex(engine => engine.slug === slug);

if (index === -1) {
  el('engine-not-found').hidden = false;
} else {
  const engine = engines[index];
  const familyNames = {synth: 'Synth engine', drum: 'Drum engine', sample: 'Break engine'};
  document.title = engine.name + ' — JAZZY Engine Room';
  el('engine-family').textContent = familyNames[engine.kind];
  el('engine-name').textContent = engine.name;
  el('engine-description').textContent = engine.details;
  el('engine-sound-count').textContent = engine.soundCount;
  el('lxr-credit-link').hidden = engine.slug !== 'lxr';
  el('back-to-catalog').href = './#engine-' + engine.slug;

  const previous = engines[(index + engines.length - 1) % engines.length];
  const next = engines[(index + 1) % engines.length];
  el('engine-previous').href = previous.href;
  el('engine-previous').textContent = '← ' + previous.name;
  el('engine-next').href = next.href;
  el('engine-next').textContent = next.name + ' →';

  const animation = el('engine-animation');
  animation.alt = engine.name + ' animation on the JAZZY firmware screen';
  animation.src = engine.still;
  animation.dataset.motion = engine.motion;
  setupMotion(el('motion-toggle')).add(animation);
  el('engine-detail').hidden = false;
}
