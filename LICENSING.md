# X0X licensing

X0X is free software under the GNU General Public License, version 3 only
(`GPL-3.0-only`, full text in `LICENSE`). It is a fork of Felucca and keeps Felucca's
licence. If you distribute X0X, or firmware derived from it, you must give your
recipients its complete corresponding source under the same licence.

## Where the code comes from

| What | Origin | Licence |
| --- | --- | --- |
| Platform: `firmware/hal/`, `firmware/loader/`, `firmware/src/{libc,lcd,gfx,usb,storage,ota}.c`, `tools/` (build, package, install, upload), `web/` (installer) | [Felucca](https://github.com/hugelton/Felucca), Copyright (C) 2026 Leo Kuroshita (@kurogedelic), Hügelton Instruments; `usb.c` and `storage.c` changed for X0X | GPL-3.0-only |
| `firmware/src/app/{slots,editor,panel,main_fm1}.c` | adapted from Felucca's `eng_sample.c`, `editor.c`, `panel.c`, `main.c` / `audio.c` | GPL-3.0-only |
| 909 (`dsp/drum909*`, `dsp/fxbus*`) | ported from [9W9](https://github.com/athousanddetails/schwung-9W9) (athousanddetails), itself after [ER-99](https://github.com/matthewcieplak/er-99) (Matthew Cieplak) | GPL-3.0 |
| 909 hi-hat, ride and crash samples (`assets/909/`) | ER-99 via 9W9 | GPL-3.0 |
| 808 (`dsp/drum808*`) | ported from [8W8](https://github.com/athousanddetails/schwung-8W8) (athousanddetails); circuit models after the TR-808 service notes and Werner / Abel / Smith; rim shot after sc808 (Yoshinosuke Horiuchi / Sam Aaron) | GPL-3.0 |
| 303 (`dsp/bass303*`) | ported from [schwung-303](https://github.com/charlesvestal/schwung-303): Open303 by Robin Schmidt (MIT), Devilfish extensions after jc303 (midilab), RAT drive after dm-Rat (Dave Mollen) | GPL-3.0 (Open303 parts MIT) |
| TB-3PO (`seq/tb3po*`) | ported from [schwung-tb3po](https://github.com/charlesvestal/schwung-tb3po), itself a port of the Phazerville Hemisphere Suite `TB_3PO` applet (djphazer and contributors) | GPL-3.0 |
| Break generator (`dsp/breaks*`) | ported from [schwung-breakbeat](https://github.com/mestela/schwung-breakbeat) (BB Gen) by mestela, **used with the author's permission** (that repository carries no licence file) | GPL-3.0-only here, by permission |
| The second core's start-up and job hand-off (`firmware/hal/fm1_cpu1.*`) | X0X, after what [Melodee](https://github.com/keremimo/melodee) (keremimo)'s dual-core audio found, with [Jangada](https://github.com/zednaked/jangada) (zednaked)'s measurements and mailbox layout | GPL-3.0-only |
| Speed-ups of the 303's render (passes over sub-blocks, the shared coefficients), the 909's sample voices and the 808's metal bank (`dsp/bass303*`, `dsp/drum909.c`, `dsp/drum808*`), the same samples bit for bit | after [Optimist](https://github.com/w0ts/optimist) (henri / hdavid), a fork of X0X | GPL-3.0-only |
| The idea of a browser emulator for FM-1 firmware (`web/emu/`) | [Groove OS](https://www.groove-os.com/) by Peter Gombos, whose site runs its firmware in the browser; no code from it | credit only |
| The screen reader's firmware side: `firmware/src/announce.c`, `tools/gen_words.py` | [fm1-base](https://github.com/charlesvestal/fm1-base) (`device/announce.c`, `tools/gen_words.py`), Copyright (C) 2026 Charles Vestal, copied by [fm1-reader](https://github.com/charlesvestal/fm1-reader)'s `tools/sync_announce.sh` | MPL-2.0 (compatible with the GPL: MPL-2.0 section 3.3) |
| Everything else in `firmware/src/{app,dsp,seq}`, `host/`, `tests/` | X0X | GPL-3.0-only |

No recorded breaks are in this tree or in the default firmware: the built-in break loops are
generated at build time by X0X's own 909 code. `tools/import_breaks.py`,
`tools/gen_break_bank.py` (`X0X_BREAK_BANK`) and `tools/upload_breaks.py` can put recordings
of your choosing into a build or onto a device; those recordings keep their own copyright.

## Felucca Assets

Felucca's non-GPL assets — the icon atlas, the panel photo and the Hügelton drum pack —
are **not** part of this fork and are not used by it. Felucca's section 7 additional
permission concerns those assets only, so it is not needed here.

## Third-party material

| What | Licence | Where |
| --- | --- | --- |
| Barlow Semi Condensed (The Barlow Project Authors), the default UI face | SIL OFL 1.1 | `assets/fonts/BarlowSemiCondensed-*.ttf`, `assets/fonts/Barlow-OFL.txt` |
| Terminus (Dimitar Toshkov Zhekov), the `terminus` font set | SIL OFL 1.1 | `assets/fonts/ter-u*.bdf`, `assets/fonts/Terminus-LICENSE.txt` |
| Fukiai icon font (Hügelton Instruments), web pages only | MIT | `web/fukiai.ttf`, `web/FUKIAI-LICENSE.txt` |
| JieLi AC79 SDK: `uboot.boot`, `cfg_tool.bin`, `eq_cfg_hw.bin` are read from your SDK checkout at build time and placed in the package; no SDK files are in this tree | Apache-2.0 | <https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK> |

## Trademarks

"Felucca" and "Hügelton Instruments" are names of Hügelton Instruments. "M-VAVE" and
"FM-1" are trademarks of their respective owners. TR-808, TR-909 and TB-303 are
trademarks of Roland Corporation, used only to describe what the parts emulate. X0X is
independent firmware; it is not affiliated with, endorsed by or supported by any of them.

## Radio

X0X never enables the Bluetooth / Wi-Fi radio of the hardware.

## JAZZY expansion sources

- S1Vave v1.12.3, commit `8588da5064fe4e8a0d10fd93be6e68ea50509b8d`: S1 voice behavior and factory settings by AndrewGG88 and the credited OberVave contributors, GPL-3.0-only. Original S1Vave branding assets are excluded. See `rhythmer/firmware/jazzy/licenses/s1vave/`.
- Saadet v1.0.0, commit `c83b05f5377703c30d649e7f2b39181c371a2a11`: HYDRA source files and wave/patch code by Kerem Kilic and the authors credited in each source, MPL-2.0. The corresponding MPL-covered files and their source notices are included in `rhythmer/firmware/jazzy/` and the pinned import inputs. See `rhythmer/firmware/jazzy/licenses/saadet/`. HYDRA is an independent model.
- JAZZY's procedural motion and screen compositions are original. No artwork or assets from Teenage Engineering are included.

- Elixir commit `d35a1cc45248e2c3d68014aaa1d3a34d6787a6f4` supplies the LXR-02 synthesis topology, factory source voices and sequence generator. The LXR-02 firmware is Copyright (C) 2012–2026 Erica Synths, based on Julian Schmidt's Sonic Potions LXR, GPL-3.0. See `rhythmer/LICENSES/GPL-3.0-Elixir-LXR.txt`. Grids is Copyright (C) 2011–2012 Emilie Gillet, GPL-3.0-or-later, used here under GPL-3.0.
- JAZZY includes 595 individual presets derived from 85 LXR-02 factory kits by Erica Synths and Hrtl. Elixir distributes those kits under a separate permission from Erica Synths. The project owner directed inclusion of the adapted preset bank. JAZZY has not obtained rights-holder authorization to redistribute it. This notice does not grant a license to the factory preset data.

- USB MIDI Host is adapted from Rhythmer's ChoralRoot/Melodee port. Copyright (C) 2026 Kerem Kilic (Ellic Studio), with enumeration and descriptor work by recursivefieldinstruments. See the retained notices in `rhythmer/firmware/src/usb_host.c` and `usb_host_desc.h`. GPL-3.0-only.
