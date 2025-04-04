# eProsima-CI Versions

This file includes the released versions of **eProsima-CI** along with their contributions to the project.
The [Forthcoming](#forthcoming) section includes those features added in `main` branch that are not yet in a stable release.

- [Forthcoming](#forthcoming)
- [v0.36.0](#v0.36.0)
- [v0.35.0](#v0.35.0)
- [v0.34.0](#v0.34.0)
- [v0.33.0](#v0.33.0)
- [v0.32.0](#v0.32.0)
- [v0.31.0](#v0.31.0)
- [v0.30.0](#v0.30.0)
- [v0.29.0](#v0.29.0)
- [v0.28.0](#v0.28.0)
- [v0.27.0](#v0.27.0)
- [v0.26.0](#v0.26.0)
- [v0.25.0](#v0.25.0)
- [v0.24.0](#v0.24.0)
- [v0.23.0](#v0.23.0)
- [v0.22.0](#v0.22.0)
- [v0.21.0](#v0.21.0)
- [v0.20.0](#v0.20.0)
- [v0.19.1](#v0.19.1)
- [v0.19.0](#v0.19.0)
- [v0.18.2](#v0.18.2)
- [v0.18.1](#v0.18.1)
- [v0.18.0](#v0.18.0)
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

## v0.36.0

- Make ``get_related_branch_from_repo`` compatible with MacOS.

## v0.35.0

- Fix getting tags on ``get_related_branch_from_repo``.

## v0.34.0

- Improve branch filter on ``get_related_branch_from_repo``.

## v0.33.0

- Escape ``skip_base`` in ``get_related_branch_from_repo``.

## v0.32.0

- Add an option whether to upload the test aritfact or not.

## v0.31.0

- Upgrade [upload-artifact](/external/upload-artifact/action) action version to ``v4.6.0``.

## v0.30.0

- Upgrade [upload-artifact](/external/upload-artifact/action) action version to ``v4.4.1``.

## v0.29.0

- Update docs job to include docs artifact name and option to disable artifact upload.

## v0.28.0

- Fix [upload-artifact](/external/upload-artifact/action) action version to ``v4.4.0``.
- Change default value for workspace in multiplatform [colcon-build](/multiplatform/colcon_build/action.yml) action.
- Pass workspace_dependencies in [sphinx-docs](/ubuntu/sphinx_docs/action.yml) action.

## v0.27.0

- Upgrade setuptools to 74.1.3.
- Update DDS Pipe versions for nightly jobs.
- Enable DDS Pipe build.

## v0.26.0

- Add `include-hidden-files` input as `true` by default to the [upload-artifact](/external/upload-artifact/action.yml) action.

## v0.25.0

- Add `skip_base` option to the `get_related_branch_from_repo` action so base branch is not considered.
- Add external (multi-platform) action to install Qt.

## v0.24.0

- Fix the windows action colcon build to accept multiple colcon meta files.
- Remove the windows action merge yaml meta files.

## v0.23.0

- Check if python venv already exists in `setup_python_venv` action.
- Set cmake-utils version to download in `sphinx_docs` action.

## v0.22.0

- Update nightly builds to compile on Ubuntu 24.04.
- Remove nightly builds for Ubuntu 20.04.
- Extended the action for installing python packages to setup a virtual environment.
- Added new Ubuntu action (`setup_python_venv`) for setting up a python virtual environment.

## v0.21.0

- Add external (multi-platform) action to install doxygen.
- Add get related branch multi-platform action.
- Add Windows action to merge a set of yaml meta files into a single meta file.

## v0.20.0

- Add colcon meta argument to colcon test actions.

## v0.19.1

- Remove `cat colcon.meta` command from windows colcon build action.

## v0.19.0

- Fix upload artifact action to allow branch names in the name (by removing forbidden characters).
- Add previous method to download artifact action to ensure name consistency.

## v0.18.2

- Fix warning in `colcon_build_test` action
- Expose test artifacts name to code coverage action

## v0.18.1

- Fix `colcon` installation on macOS when used in combination with `setup-python` action byt not passing the `--user` flag to `pip`.
- `change_actions_reference.sh` also updates references within the `.github` directory.

## v0.18.0

- Refactor fastdds, dev-utils, and ddspipe builds to support fastdds v2 and v3
- Fix dev-utils and ddspipe nightly artifact inputs
- Activate Fast DDS v3 build
- Enable dev-utils build for Fast DDS v3
- Expose test artifacts name to `colcon-build-test` multiplatform action

## v0.17.0

- Fix conditional statement in `colcon_test`` action in windows.
- Fix fastdds version to `2.x`.
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
