# Nvidia-HPCG benchmarks

 NVIDIA HPCG is based on the [HPCG](https://hpcg-benchmark.org/) Conjugate Gradient solver benchmark and optimized for performance on NVIDIA accelerated HPC systems.

## Usage

Note that the executable (`xhpcg-cpu` or `xhpcg`) and the driver script that sets various environment variables must be available in `PATH`. This app does not build the executable and just runs the prebuilt executable.

The systems intending to run the test on `aarch64` platforms must define the `grace` feature in the partition.

From the top-level directory of the repository, you can run the benchmarks with

```sh
reframe -c benchmarks/apps/nvidia_hpcg -r --performance-report
```

You can use the `-n/--name` argument to pick `HPCG_Original / HPCG_Stencil / HPCG_LFRic` to select a particular benchmark.
Alternatively, if you want to compare the two implementations of the 27 point stencil problem (Original and Stencil), you can filter by tag `-t 27pt_stencil`.

This app is currently tested on the Grace CPU ofthe GH200 superchip. It uses MPI parallelisation, but is launched with a custom shell script. and it is recommended to use the `--system` argument to pick up the appropriate hardware details.
