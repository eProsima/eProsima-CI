# Fast-DDS-CI

This is a github CI auxiliary repo that contains common github actions and workflows shared along multiple eProsima libraries and tools.
The main idea is to collect every repeated or generic step of any CI to have a single more maintainable generic point.

## Steps Implemented

* **Ubuntu (generic)**

  * [get_git_diff_files](ubuntu/get_git_diff_files/action.yml)
    * Get the files that differ from one github reference to another. Can grep result.

  * [git_fetch_all](ubuntu/git_fetch_all/action.yml)
    * Get all branches of a specific repository.

  * [install_apt_packages](ubuntu/install_apt_packages/action.yml)
    * Install generic apt packages required by these actions and most eProsima projects.

  * [install_colcon](ubuntu/install_colcon/action.yml)
    * Install colcon and its dependencies depending on the platform.

  * [install_python_packages](ubuntu/install_python_packages/action.yml)
    * Install generic python packages required by these actions and most eProsima projects.

  * [set_platform](ubuntu/set_platform/action.yml)
    * Set the platform OS version in a environment variable.

## Out-of-the-box Actions Implemented

These actions could be used right away in any repository.

* [uncrustify](actions/uncrustify/action.yml)
  * Check the C++ linter of the new files added to the repository.

* [python_linter](actions/python_linter/action.yml)
  * Check the Python linter of the new files added to the repository.
