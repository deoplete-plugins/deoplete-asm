# deoplete-asm

[![CircleCI][circleci-badge]][circleci] [![Releases][release-badge]][release] [![GA][ga-badge]][ga]

[deoplete.nvim][deoplete.nvim] source for Assembly based by [google/EXEgesis][EXEgesis].

## Overview

### [deoplete-asm](https://github.com/zchee/deoplete-asm)

deoplete-asm provides the Assembly code completion for [deoplete.nvim][deoplete.nvim].  

The completion candidate is acquired from [protobuf binary data](rplugin/python3/deoplete/sources/pb/instructions.sdm.pb). That human-readable text is [instructions_transformed.pbtxt](rplugin/python3/deoplete/sources/pb/instructions_transformed.pbtxt).

### [google/EXEgesis](EXEgesis)

> Google's EXEgesis project aims to improve code generation in compilers, via:
> - Providing machine-readable lists of instructions for hardware vendors and microarchitectures.
> - Inferring latencies and µOps scheduling for each instruction/microarchitecture pair.
> - Providing tools for debugging the performance of code based on this data.

EXEgesis parses and dump protobuf format binary from Intel x86-64 instruction set reference manual:

- [Intel® 64 and IA-32 architectures software developer’s manual][intel-64-ia-32-architectures-instruction-set-reference-manual]

## Support architectures

See [google/EXEgesis/README.md#whats-next](https://github.com/google/EXEgesis#whats-next)

- Intel x86-64

## Config

### `g:deoplete#sources#asm#go_mode`

If set `1`, Use Go Plan9 assembly mode.  
Let's try test edit [testdata/cpuid_amd64.s](testdata/cpuid_amd64.s) with `1`.

## Update protobuf binary

just `make dump_protobuf`.  
Required `docker` engine. See also [Dockerfile](docker/Dockerfile).


## TODO

- Support registers


[deoplete.nvim]: https://github.com/Shougo/deoplete.nvim
[EXEgesis]: https://github.com/google/EXEgesis
[intel-64-ia-32-architectures-instruction-set-reference-manual]: https://software.intel.com/sites/default/files/managed/39/c5/325462-sdm-vol-1-2abcd-3abcd.pdf

[circleci]: https://circleci.com/gh/zchee/deoplete-asm
[release]: https://github.com/zchee/deoplete-asm/releases
[ga]: https://github.com/zchee/deoplete-asm

[circleci-badge]: https://img.shields.io/circleci/project/github/zchee/deoplete-asm/master.svg?style=flat-square&label=%20%20CircleCI&logoWidth=16&logo=data%3Aimage%2Fsvg%2Bxml%3Bcharset%3Dutf-8%3Bbase64%2CPHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI0MCIgdmlld0JveD0iMCAwIDIwMCAyMDAiPjxwYXRoIGZpbGw9IiNEREQiIGQ9Ik03NC43IDEwMGMwLTEzLjIgMTAuNy0yMy44IDIzLjgtMjMuOCAxMy4xIDAgMjMuOCAxMC43IDIzLjggMjMuOCAwIDEzLjEtMTAuNyAyMy44LTIzLjggMjMuOC0xMy4xIDAtMjMuOC0xMC43LTIzLjgtMjMuOHpNOTguNSAwQzUxLjggMCAxMi43IDMyIDEuNiA3NS4yYy0uMS4zLS4xLjYtLjEgMSAwIDIuNiAyLjEgNC44IDQuOCA0LjhoNDAuM2MxLjkgMCAzLjYtMS4xIDQuMy0yLjggOC4zLTE4IDI2LjUtMzAuNiA0Ny42LTMwLjYgMjguOSAwIDUyLjQgMjMuNSA1Mi40IDUyLjRzLTIzLjUgNTIuNC01Mi40IDUyLjRjLTIxLjEgMC0zOS4zLTEyLjUtNDcuNi0zMC42LS44LTEuNi0yLjQtMi44LTQuMy0yLjhINi4zYy0yLjYgMC00LjggMi4xLTQuOCA0LjggMCAuMy4xLjYuMSAxQzEyLjYgMTY4IDUxLjggMjAwIDk4LjUgMjAwYzU1LjIgMCAxMDAtNDQuOCAxMDAtMTAwUzE1My43IDAgOTguNSAweiIvPjwvc3ZnPg%3D%3D
[release-badge]: https://img.shields.io/github/release/zchee/deoplete-asm.svg?style=flat-square
[ga-badge]: https://ga-beacon.appspot.com/UA-89201129-1/deoplete-asm?flat&useReferer&pixel
