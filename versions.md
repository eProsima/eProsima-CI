# eProsima-CI Versions

This file includes the released versions of **eProsima-CI** along with their contributions to the project.
The [Forthcoming](#forthcoming) section includes those features added in `main` branch that are not yet in a stable release.

- [Forthcoming](#forthcoming)
- [v0.17.0](#v0.17.0)
- [v0.16.1](#v0.16.1)
- [v0.16.0](#v0.16.0)
- [v0.15.0](#v0.15.0)
- [v0.14.0](#v0.14.0)
- [v0.13.0](#v0.13.0)
- [v0.12.1](#v0.12.1)
- [v0.12.0](#v0.12.0)
- [v0.11.0](#v0.11.0)
- [v0.10.0](#v0.10.0)
- [v0.9.0](#v0.9.0)
- [v0.8.0](#v0.8.0)
- [v0.7.0](#v0.7.0)
- [v0.6.0](#v0.6.0)
- [v0.5.0](#v0.5.0)
- [v0.4.0](#v0.4.0)
- [v0.4.0](#v0.4.0)
- [v0.3.0](#v0.3.0)
- [v0.2.0](#v0.2.0)

## Forthcoming

The upcoming release will include the following **features**:

## v0.17.0

- Fix conditional statement in `colcon_test`` action in windows.
- Fix fastdds verstion to `2.x`.
- Fix user installation path when installing with `pip` in macOS and Ubuntu.

## v0.16.1

- Fix `get_related_branch_from_repo` action to get related tags from remote repositories.

## v0.16.0

- Remove `uncrustify` installation action for Ubuntu 20.04.
- Update `uncrustify` action to use eProsima fork of `ament_lint` repository.
- Fix `uncrustify` action to properly calculate the path to files with changes.

## v0.15.0

- New Ubuntu `get_related_branch_from_repo` action to get the related branch from a remote repository.

## v0.14.0

- New `add_labels` action to add labels to a pull request.
- New `remove_labels` action to remove labels from a pull request.
- Set default CMake version in the `install_fastdds_dependencies` action

## v0.13.0

- Update TSAN action to use GCC 12

## v0.12.1

- Fix a regression in `colcon_build` action for macOS.

## v0.12.0

- Temporary `TSAN` & `ASAN` workflow fix: set the number of random bits for `mmap` to 28.

## v0.11.0

This release includes the following **updates**:

- Remove `CXXFLAGS` for windows build.
- Bump download artifact action to v4
- Support for the `vcs_import` action in macOS.

## v0.10.0

This release includes the following **updates**:

- Support for skipping existing repositories in the `vcs_import` action.
- `colcon_build` action does not provide a default value for the `cmake_args_default` input.

## v0.9.0

This release includes the following **features**:

- An action to install brew packages on macOS.
- An action to install python packages on macOS.
- An action to install colcon on macOS.
- macOS support through the following multiplatform actions:
  - `colcon_build`
  - `colcon_test`
  - `install_colcon`
  - `install_gtest`
  - `install_python_packages`
  - `junit_summary`

## v0.8.0

This release includes the following **features**:

- Add a `junit-summary` action to generate a summary of JUnit test results.

## v0.7.0

This release includes the following **features**:

- Add `test-reporter` action
- Add `setup_cmake` action

## v0.6.0

This release includes the following **features**:

- Download eProsima dev-utils (`fetch_dev_utils_manual` action)
- Download eProsima ddspipe (`fetch_ddspipe_manual` action)
- Download eProsima Fast DDS (`fetch_fastdds_manual` action)
- New external action: download artifacts

## v0.5.0

This release includes the following **features**:

- Setup CCache.
- Install specific CMake and Ninja versions.
- Install and setup Python.

## v0.4.0

This release includes the following **features**:

- Mirror external action
- Create pull request external action

## v0.3.0

This release includes the following **bug-fixes**:

- Fix codecov action
- Fix windows `install_python_packages` action
- Find artifacts of just completed workflows, and not only for successful ones.

## v0.2.0

First project release.

This release includes the following **features**:

- General purpose actions
- Multiplatform support
- Artifacts generation workflows for projects:
  - Fast DDS
  - dev-utils
  - DDS Pipe

This release includes the following **documentation**:

- updated (README.md)
- developer contributing information (`.dev/contributions.md`).
