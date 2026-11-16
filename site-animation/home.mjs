import { engines } from './catalog.mjs?v=20261111.1';
import { setupMotion } from './motion.mjs?v=20261117.1';

const grid = document.querySelector('#engine-grid');
const guide = document.querySelector('#engine-guide');
const guideTopic = document.querySelector('#engine-guide-topic');
const featured = document.querySelector('#featured-engines');
const cardTemplate = document.querySelector('#engine-card');
const search = document.querySelector('#engine-search');
const filters = [...document.querySelectorAll('[data-filter]')];
const count = document.querySelector('#engine-count');
const motion = setupMotion(document.querySelector('#motion-toggle'));
document.querySelectorAll('[data-motion]').forEach(img => motion.add(img));
let family = 'all';

function engineCard(engine, description) {
  const card = cardTemplate.content.firstElementChild.cloneNode(true);
  const img = card.querySelector('img');
  card.href = engine.href;
  card.dataset.family = engine.kind;
  img.src = engine.still;
  img.dataset.motion = engine.motion;
  card.querySelector('.engine-card-name').textContent = engine.name;
  card.querySelector('.engine-card-note').textContent = description ?? engine.soundCount;
  if (!description) card.id = 'engine-' + engine.slug;
  motion.add(img, true);
  return card;
}

const features = [
  [23, 'A skater leans into the beat and lifts off on the accents.'],
  [39, 'A windsock bends with each gust of poly modulation.'],
  [26, 'Two fencers trade lunges as the chord opens up.'],
  [42, 'A wrecking ball knocks bricks loose on the drum hits.'],
  [16, 'Accents and slides send ripples through a melting smile.'],
  [15, 'The record spins as the tonearm follows the break.'],
];
featured.append(...features.map(([id, description]) =>
  engineCard(engines.find(engine => engine.id === id), description)));

function fitEngineGuide() {
  // auto-fill keeps every column in the computed track list, even for one result.
  const columns = getComputedStyle(grid).gridTemplateColumns.split(' ').length;
  const cards = grid.childElementCount - 1;
  const used = cards % columns;
  guide.hidden = used === 0;
  if (used) guide.style.setProperty('--guide-span', columns - used);
}

function render() {
  const q = search.value.toLowerCase().trim();
  const matches = engines.filter(({name, kind, details}) =>
    (family === 'all' || family === kind) && (name + ' ' + details).toLowerCase().includes(q));
  grid.querySelectorAll('img').forEach(img => motion.remove(img));
  const percussion = matches.every(({kind}) => kind !== 'synth');
  guide.href = percussion ? 'manual/#drums' : 'manual/#presets';
  guideTopic.textContent = percussion ? 'Play drums and Break loops' : 'Browse sounds and presets';
  grid.replaceChildren(...matches.map(engine => engineCard(engine)), guide);
  fitEngineGuide();
  count.textContent = matches.length === 0 ? 'No matching engines' :
    matches.length === 1 ? '1 engine' : matches.length + ' engines';
}
filters.forEach(button => button.addEventListener('click', () => {
  family = button.dataset.filter;
  filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  render();
}));
search.addEventListener('input', render);
render();
new ResizeObserver(fitEngineGuide).observe(grid);
if (location.hash === '#engine-hort-drum') location.replace('#engine-hortator');

const audio = document.querySelector('#patch-audio');
const patchCaption = document.querySelector('#patch-caption');
const auditions = [...document.querySelectorAll('[data-audio]')];
const clips = {
  fmini: 'Tube Bass · syncopated analog bass',
  ober: 'Ghost Pad · four chords · low-pass and room reverb',
  hydra: 'Superstack · sustained harmony with stereo delay and reverb',
  lxr: '124 BPM house · BROKE D3 kick · Lectro snare and hats'
};
auditions.forEach(button => button.addEventListener('click', () => {
  auditions.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  const clip = button.dataset.audio;
  patchCaption.textContent = clips[clip];
  audio.src = 'assets/' + clip + '.wav?v=' + (clip === 'ober' || clip === 'lxr' ? 5 : 2);
  audio.play().catch(() => {});
}));


if (location.hash === '#engine-serum') location.replace('#engine-wavetable');
