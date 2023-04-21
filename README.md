# Fast-DDS-CI

> This is the eProsima Annapurna Team branch of eprosima-CI

This is a github CI auxiliary repo that contains common github steps and actions shared along multiple eProsima libraries and tools.
The main idea is to collect every repeated or generic step of any CI to have a single more maintainable generic point.

## Steps Implemented

* **Ubuntu (generic)**

  * `set_platform`
    * Set the platform OS version in a environment variable.

  * `install_apt_packages`
    * Install apt packages.

  * `install_python_packages`
    * Install python packages.

  * `install_colcon`
    * Install colcon and its dependencies depending on the platform.

  * `get_git_diff_files`
    * Get the files that differ from one github reference to another. Can grep result.

  * `git_fetch_all`
    * Get all branches of a specific repository.

## Full Actions Implemented

* `uncrustify`
  * Check the C++ linter of the new files added to the repository.

* `python_linter`
  * Check the Python linter of the new files added to the repository.
