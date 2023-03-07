# Fast-DDS-CI

This is a github CI auxiliary repo that contains common github actions and workflows shared along multiple eProsima libraries and tools.
The main idea is to collect every repeated or generic step of any CI to have a single more maintainable generic point.

---

## Out-of-the-box Actions

These actions could be used right away in any repository.

---

* [uncrustify](ubuntu-20.04/uncrustify/action.yml)
  * Check the C++ linter of the new files added to the repository.

```yml
uses: eProsima/eProsima-CI/ubuntu-20.04/uncrustify@main
with:
  result_filename: uncrustify_results.xml  # File to store results
  uncrustify_configuration_version: master  # Version of eProsima/cpp-style repo to get configuration
  file_extensions_grep_args: "-e '\\.h' -e '\\.hpp' -e '\\.cpp' -e '\\.ipp' -e '\\.cxx'"  # Grep arguments to include files to check
```

---

* [python_linter](ubuntu/python_linter/action.yml)
  * Check the Python linter of the new files added to the repository.

```yml
uses: eProsima/eProsima-CI/ubuntu/uncrustify@main
with:
  linter_configuration_version: master  # Version of eProsima/cpp-style repo to get configuration
  file_extensions_grep_args: "-e '\\.py'"  # Grep arguments to include files to check
```

---
---

## Auxiliary Actions

These actions are of generic use, commonly as auxiliary steps in other actions

### Ubuntu (generic)

* [get_git_diff_files](ubuntu/get_git_diff_files/action.yml)
  * Get the files that differ from one github reference to another. Can grep result.
  * `uses: eProsima/eProsima-CI/ubuntu/get_git_diff_files@main`

* [git_fetch_all](ubuntu/git_fetch_all/action.yml)
  * Get all branches of a specific repository.
  * `uses: eProsima/eProsima-CI/ubuntu/git_fetch_all@main`

* [install_apt_packages](ubuntu/install_apt_packages/action.yml)
  * Install generic apt packages required by these actions and most eProsima projects.
  * `uses: eProsima/eProsima-CI/ubuntu/install_apt_packages@main`

* [install_colcon](ubuntu/install_colcon/action.yml)
  * Install colcon and its dependencies depending on the platform.
  * `uses: eProsima/eProsima-CI/ubuntu/install_colcon@main`

* [install_python_packages](ubuntu/install_python_packages/action.yml)
  * Install generic python packages required by these actions and most eProsima projects.
  * `uses: eProsima/eProsima-CI/ubuntu/install_python_packages@main`

* [set_platform](ubuntu/set_platform/action.yml)
  * Set the platform OS version in a environment variable.
  * `uses: eProsima/eProsima-CI/ubuntu/set_platform@main`
