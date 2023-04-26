# eProsima-CI

This is a github CI auxiliary repo that contains common github steps, actions, and workflows shared along multiple eProsima libraries and tools.
The main idea is to collect every repeated or generic step of any CI to have a single more maintainable generic point.

---

## Index

- [eProsima-CI](#eprosima-ci)
  - [Index](#index)
  - [User manual](#user-manual)
  - [Out-of-the-box Actions Implemented](#out-of-the-box-actions-implemented)
  - [Actions Implemented](#actions-implemented)
    - [Multiplatform](#multiplatform)
    - [Ubuntu](#ubuntu)
  - [Dependencies built](#dependencies-built)
    - [Artifacts uploaded](#artifacts-uploaded)
    - [Generate artifacts manually](#generate-artifacts-manually)

---

## User manual

In order to use this repository, we recommend you:

1. **Always use a fix version**. When using any of these actions, set it with a `@v<X>` version.
2. Use `multiplatform` actions when possible. They automatically will redirect the action to the proper OS.
3. If you want a long well preserved CI, use `@vX.Y` versioning, to be sure that CI will not change and break something in the future. However, this may be a problem because it will not be updated with improvements or external versions.
4. Actions are documented in their own `<platform>/<action_name>/action.yml` files. Check them for description and argument definitions.

---

## Out-of-the-box Actions Implemented

- [uncrustify](ubuntu/uncrustify/action.yml)
  - Check the C++ linter of the new files added to the repository.
  - *Only on ubuntu*.

- [python_linter](ubuntu/python_linter/action.yml)
  - Check the Python linter of the new files added to the repository.
  - *Only on ubuntu*.

- [sphinx_docs](ubuntu/sphinx_docs/action.yml)
  - Build Sphinx documentation, test it and upload results.
  - *Only on ubuntu*.
  - *Only for documentation projects based in `cmake_utils`*.

---

## Actions Implemented

### Multiplatform

- [asan_build_test](multiplatform/asan_build_test/action.yml)
  - Build a project using colcon and ASAN flags and execute tests.

- [clang_build_test](multiplatform/clang_build_test/action.yml)
  - Build a project using colcon and CLang flags and execute tests.

- [clang_tidy_check](multiplatform/clang_tidy_check/action.yml)
  - Execute clang-tidy-check over a built project to static analysis.

- [colcon_build](multiplatform/colcon_build/action.yml)
  - Execute `colcon build` command to build a project.

- [colcon_build_test](multiplatform/colcon_build_test/action.yml)
  - Build a project using colcon and execute tests.

- [colcon_build_test_flaky](multiplatform/colcon_build_test_flaky/action.yml)
  - Build a project using colcon and execute only flaky tests (labeled as `xfail`).

- [colcon_test](multiplatform/colcon_test/action.yml)
  - Execute `colcon test` command to test a project.

- [download_dependency](multiplatform/download_dependency/action.yml)
  - Download an artifact previously generated from a workflow run.

- [generate_dependency](multiplatform/generate_dependency/action.yml)
  - Build a project and upload the installed objects as an artifact.

- [get_configurations_from_repo](multiplatform/get_configurations_from_repo/action.yml)
  - Download a `.repos` and a `colcon.meta` file from a repository.

- [get_file_from_repo](multiplatform/get_file_from_repo/action.yml)
  - Download a file from a repository.

- [get_workflow_id](multiplatform/get_workflow_id/action.yml)
  - Get the ID of a specific workflow run.

- [install_colcon](multiplatform/install_colcon/action.yml)
  - Install colcon and its dependencies depending on the platform.

- [install_fastdds_dependencies](multiplatform/install_fastdds_dependencies/action.yml)
  - Install Fast DDS and general eProsima projects dependencies.

- [install_gtest](multiplatform/install_gtest/action.yml)
  - Instal `gtest` and `gmock` C++ library.

- [install_openssl](multiplatform/install_openssl/action.yml)
  - Instal `Open SSL` C++ library.

- [install_yamlcpp](multiplatform/install_yamlcpp/action.yml)
  - Instal `yaml-cpp` C++ library.

- [tsan_build_test](multiplatform/tsan_build_test/action.yml)
  - Build a project using colcon and TSAN flags and execute tests.

- [vcs_import](multiplatform/vcs_import/action.yml)
  - Import several repositories from a Yaml file using `vcs`.

### Ubuntu

- [get_git_diff_files](ubuntu/get_git_diff_files/action.yml)
  - Get the files that differ from one github reference to another. Can grep result.

- [git_fetch_all](ubuntu/git_fetch_all/action.yml)
  - Get all branches of a specific repository.

- [install_apt_packages](ubuntu/install_apt_packages/action.yml)
  - Install apt packages.

- [install_python_packages](ubuntu/install_python_packages/action.yml)
  - Install python packages.

- [set_platform](ubuntu/set_platform/action.yml)
  - Set the platform OS version in a environment variable.

---

## Dependencies built

There are several workflows implemented that build projects and upload them as artifacts.
These are used for other projects to speed up the built process of the dependencies.

### Artifacts uploaded

So far, there are 3 workflows running to upload artifacts:

- [Fast DDS](<https://github.com/eProsima/Fast-DDS>)
- [dev-utils](<https://github.com/eProsima/dev-utils>)
- [DDS Pipe](<https://github.com/eProsima/DDS-Pipe/>)

These are the artifacts that are generated every night with the latest versions of each project:

- Fast DDS
  - built_fastdds_ubuntu-20.04_Debug_nightly
  - built_fastdds_ubuntu-20.04_Release_nightly
  - built_fastdds_ubuntu-22.04_Debug_nightly
  - built_fastdds_ubuntu-22.04_Release_nightly
  - built_fastdds_windows-2019_Debug_nightly
  - built_fastdds_windows-2019_Release_nightly
  - built_fastdds_windows-2022_Debug_nightly
  - built_fastdds_windows-2022_Release_nightly

- dev-utils
  - built_dev_utils_ubuntu-20.04_Debug_nightly
  - built_dev_utils_ubuntu-20.04_Release_nightly
  - built_dev_utils_ubuntu-22.04_Debug_nightly
  - built_dev_utils_ubuntu-22.04_Release_nightly
  - built_dev_utils_windows-2019_Debug_nightly
  - built_dev_utils_windows-2019_Release_nightly
  - built_dev_utils_windows-2022_Debug_nightly
  - built_dev_utils_windows-2022_Release_nightly

- DDS Pipe
  - built_ddspipe_ubuntu-20.04_Debug_nightly
  - built_ddspipe_ubuntu-20.04_Release_nightly
  - built_ddspipe_ubuntu-22.04_Debug_nightly
  - built_ddspipe_ubuntu-22.04_Release_nightly
  - built_ddspipe_windows-2019_Debug_nightly
  - built_ddspipe_windows-2019_Release_nightly
  - built_ddspipe_windows-2022_Debug_nightly
  - built_ddspipe_windows-2022_Release_nightly

In order to use one of these artifacts, use the following action as a step:

```yml
- name: Get fastdds artifact
  uses: jparisu/eProsima-CI/multiplatform/download_dependency@main
  with:
    artifact_name: built_fastdds_ubuntu-20.04_Debug_nightly
    workflow_source: build_fastdds.yml
    workflow_source_repository: eProsima/eProsima-CI
    # Path where to download the installs from the artifact
    target_workspace: ${{ github.workspace }}/install
    # If inside an action, this value must be generated in workflow and passed as argument
    secret_token: ${{ secrets.GITHUB_TOKEN }}
```

### Generate artifacts manually

Artifacts could be executed manually with different dependencies and/or different CMake arguments.
In order to do so there are 2 possibilities:
