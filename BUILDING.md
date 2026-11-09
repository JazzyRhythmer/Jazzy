# Build the JAZZY public beta

This repository contains the corresponding source for the FM-1_900 JAZZY v0.1.0-beta.1 package. It includes the firmware, loader, build and packaging scripts, exact generated tables, and the factory slot inputs for the released binary.

Use Python 3.10 or later and the JieLi pi32v2 toolchain. On Linux x86-64 the toolchain runs natively. On macOS use Docker with linux/amd64 support. Set JIELI_TOOLCHAIN to the directory containing pi32v2 and common. The upstream toolchain helper is [rhythmer/tools/get_toolchain.sh](rhythmer/tools/get_toolchain.sh).

Set AC79_SDK to the JieLi AC79 SDK checkout at tag AC79NN_SDK_V1.2.1_2023-12-13. The [SDK repository](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK) supplies uboot.boot, cfg_tool.bin, and cfg/eq_cfg_hw.bin. The build checks their hashes.

```sh
export JIELI_TOOLCHAIN=/path/to/jieli/toolchain
export AC79_SDK=/path/to/fw-AC79_AIoT_SDK
./build.sh
```

The build writes build/felucca.fwsc by default. Set RHYTHMER_BUILD_DIR to put the outputs elsewhere. The build uses the checked-in generated inputs and the linker checks for the FM-1_900 layout. Compare the result with the release SHA256SUMS.txt. The package includes two Break banks and the synth tables in their reserved tails.

The open-source code license and third-party asset notices are in LICENSE, LICENSING.md, THIRD-PARTY-AUDIO.txt and the source-level license files.
