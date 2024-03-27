# eProsima-CI

This is a github CI auxiliary repo that contains common github steps, actions, and workflows shared along multiple eProsima libraries and tools.
The main idea is to collect every repeated or generic step of any CI to have a single more maintainable generic point.

## Index

- [User manual](#user-manual)
- [Out-of-the-box Actions Implemented](#out-of-the-box-actions-implemented)
- [Actions Implemented](#actions-implemented)
  - [Multiplatform](#multiplatform)
  - [Ubuntu](#ubuntu)
- [Dependencies built](#dependencies-built)
  - [Artifacts uploaded](#artifacts-uploaded)
  - [Generate artifacts manually](#generate-artifacts-manually)
- [External Actions](#external-actions)

---

## User manual

In order to use this repository, the following recommendations are suggested:

1. **Always use a fix version**.
   When using any of these actions, set it with a `@v<X>` version.
2. Use `multiplatform` actions when possible.
   They automatically will redirect the action to the proper OS.
3. If planning a long well preserved CI, use `@vX.Y` versioning, to be sure that CI will not change and break something in the future.
   However, this may be a problem because it will not be updated with improvements or external versions.
4. Actions are documented in their own `<platform>/<action_name>/action.yml` files.
   Check each file for description and argument definitions.

For more information about versioning handle of this project, check following [file](.dev/versioning_guidelines.md).

---

## Out-of-the-box Actions Implemented

- [uncrustify](ubuntu/uncrustify/action.yml)
  - Check the C++ linter of the new files added to the repository.
  - *Only on ubuntu*.

- [python_linter](ubuntu/python_linter/action.yml)
  - Check the Python linter of the new files added to the repository.
  - *Only on ubuntu*.

- [sphinx_docs](ubuntu/sphinx_docs/action.yml)
  - Build [Sphinx](<https://www.sphinx-doc.org/en/master/>) documentation, test it and upload results.
  - *Only on ubuntu*.
  - *Only for documentation projects based in [cmake_utils](https://github.com/eProsima/dev-utils)*.

---

## Actions Implemented

### Multiplatform

- [asan_build_test](multiplatform/asan_build_test/action.yml)
  - Build a project using colcon and ASAN flags and execute tests.

- [clang_build_test](multiplatform/clang_build_test/action.yml)
  - Build a project using colcon and CLang flags and execute tests.

- [clang_tidy_check](multiplatform/clang_tidy_check/action.yml)
  - Execute clang-tidy-check over a built project for static analysis.

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

- [fetch_dev_utils_manual](multiplatform/fetch_dev_utils_manual/action.yml)
  - Download eProsima/dev-utils setting the specific version of the repository.

- [fetch_ddspipe_manual](multiplatform/fetch_ddspipe_manual/action.yml)
  - Download eProsima/DDS-Pipe setting the specific version of the repository.

- [fetch_fastdds_manual](multiplatform/fetch_fastdds_manual/action.yml)
  - Download Fast DDS and its eProsima dependencies setting the specific version of each repository.

- [generate_dependency_artifact](multiplatform/generate_dependency_artifact/action.yml)
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
  - Install `gtest` and `gmock` C++ library.

- [install_openssl](multiplatform/install_openssl/action.yml)
  - Install `Open SSL` C++ library.

- [install_python_packages](ubuntu/install_python_packages/action.yml)
  - Install python packages.

- [install_yamlcpp](multiplatform/install_yamlcpp/action.yml)
  - Install `yaml-cpp` C++ library.

- [junit_summary](multiplatform/junit_summary/action.yaml)
  - Create a workflow summary with the results of the tests from jUnit reports.

- [tsan_build_test](multiplatform/tsan_build_test/action.yml)
  - Build a project using colcon and TSAN flags and execute tests.

- [vcs_import](multiplatform/vcs_import/action.yml)
  - Import several repositories from a Yaml file using `vcs`.

### Ubuntu

- [coverage_build_test_upload](ubuntu/coverage_build_test_upload/action.yml)
  - Build a project using colcon and coverage flags, execute tests and upload results.

- [get_git_diff_files](ubuntu/get_git_diff_files/action.yml)
  - Get the files that differ from one github reference to another.
    The result can be parsed with `grep`.

- [git_fetch_all](ubuntu/git_fetch_all/action.yml)
  - Get all branches of a specific repository.

- [install_apt_packages](ubuntu/install_apt_packages/action.yml)
  - Install apt packages.

- [junit_summary](ubuntu/junit_summary/action.yaml)
  - Create a workflow summary with the results of the tests from jUnit reports.

- [set_platform](ubuntu/set_platform/action.yml)
  - Set the platform OS version in a environment variable.

- [setup_cmake](ubuntu/setup_cmake/action.yml)
  - Set a specific CMake version

- [get_related_branch_from_repo](ubuntu/get_related_branch_from_repo/action.yml)
  - Get the related branch from a remote repository.
---

### macOS

- [install_brew_packages](macos/install_brew_packages/action.yml)
  - Install brew packages.
- [install_python_packages](macos/install_python_packages/action.yml)
  - Install python packages.
- [install_colcon](macos/install_colcon/action.yml)
  - Install colcon and its dependencies.

## Workflows

There are several workflows implemented that build projects and upload them as artifacts.
These are used for other projects to speed up the build process of the dependencies.

### Artifacts uploaded

So far, the following workflows are running to upload artifacts:

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
  uses: eProsima/eProsima-CI/multiplatform/download_dependency@main
  with:
    artifact_name: built_fastdds_ubuntu-20.04_Debug_nightly
    workflow_source: build_fastdds.yml
    workflow_source_repository: eProsima/eProsima-CI
    # Path where to download the installs from the artifact
    target_workspace: ${{ github.workspace }}/install
    # If inside an action, this value must be generated in workflow and passed as argument
    secret_token: ${{ secrets.GITHUB_TOKEN }}
    workflow_conclusion: completed
```

#### Generate artifacts manually

The artifacts can be customized so the artifacts generated follow specific configurations.
These configurations are set in a `.repos` and `colcon.meta` files in a new branch in eProsima-CI.
In order to change the dependencies required to build within an artifact,
set [dependencies.repos](.github/workflows/configurations/<artifact>/dependencies.repos) with the new repositories to download and build.
In order to change CMake options when building the artifact, set files in files in `.github/workflows/configurations/metas`.
Run the `manual_build` workflow with these arguments:

- `built_configuration_branch`: Branch created with `.repos` and `colcon.meta` files.
- `artifacts_name_postfix`: Postfix of the name of the artifact used to download and link, and also postfix of the name of the generated artifact.

> :warning: Do not generate custom artifacts with postfix `_nightly`, as this is the main name other repos will use.

> :page_facing_up: Fast DDS manual build allows to specify Fast DDS and its eProsima dependencies version as inputs of the workflow.
  In order to use the manually set versions instead of the ones taken from the `.repos` file, just disable `use_repos_file` option.

> :page_facing_up: eProsima/dev-utils build allows to specify the version as inputs of the workflow.
  In order to use the manually set versions instead of the one taken from the `.repos` file, just disable `use_repos_file` option.

> :page_facing_up: eProsima/DDS-Pipe build allows to specify the version as inputs of the workflow.
  In order to use the manually set versions instead of the one taken from the `.repos` file, just disable `use_repos_file` option.

## Custom artifact generation

The workflow [manual_build](.github/workflows/manual_build.yml) supports to create any artifact giving a `.repos` and `colcon.meta` files.
In order to run this workflow, create a branch in this repository,
set [dependencies.repos](.github/workflows/configurations/manual/dependencies.repos) file with the repositories needed to build the project and set `colcon.meta` files in `.github/workflows/configurations/metas`.
Then, run the `manual_build` workflow with these arguments:

- `built_configuration_branch`: Branch created with `.repos` and `colcon.meta` files.
- `artifacts_name_prefix`: Prefix of the name of the artifact to generate.
- `artifacts_name_postfix`: Postfix of the name of the artifact to generate.

The result artifacts will be called `<artifacts_name_prefix>_<os>_<cmake_build_type><artifacts_name_postfix>`.

## External Actions

This repository also includes a wrapper around the external actions being used by eProsima CI workflows.
Thus, the maintainability and upgrading of these actions is performed in a single step.
Find below the external actions listed:

| External Action | Description | LICENSE |
|---|---|---|
| [add_labels](external/add_labels/action.yml) | Add labels from an issue or PR | Apache-2.0 license |
| [action-download-artifact](external/action-download-artifact/action.yml) | Download and extract an artifact | MIT license |
| [checkout](external/checkout/action.yml) | Checkout repository | MIT license |
| [codecov-action](external/codecov-action/action.yml) | Upload coverage report to codecov.io | MIT license |
| [create-pull-request](external/create-pull-request/action.yml) | Create PR | MIT license |
| [get-cmake](external/get-cmake/action.yml) | Installs desired versions of CMake and Ninja | Mit license |
| [mirror-branch-action](external/mirror-branch-action/action.yml) | Mirror branch within the same repository | Apache-2.0 license |
| [remove_labels](external/remove_labels/action.yml) | Remove labels from an issue or PR | Apache-2.0 license |
| [setup-ccache-action](external/setup-ccache-action/action.yml) | Setup CCache in a workflow | MIT license |
| [setup-python](external/setup-python/action.yml) | Installs a version of Python or PyPy and (by default) adds it to the PATH | MIT license |
| [test-reporter](external/test-reporter/action.yml) | Display test results directly in GitHub | MIT license |
| [upload-artifact](external/upload-artifact/action.yml) | Upload build artifact | MIT license |
| [wait-on-check-action](external/wait-on-check-action/action.yml) | Wait on certain check | MIT license |
| [test-reporter](external/test-reporter/action.yml) | Generate test reports in workflow summaries | MIT license |
