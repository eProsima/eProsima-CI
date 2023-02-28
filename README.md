# Fast-DDS-CI

> This is the eProsima Annapurna Team branch of eprosima-CI

This is a github CI auxiliary repo that contains common github steps and actions shared along multiple eProsima libraries and tools.
The main idea is to collect every repeated or generic step of any CI to have a single more maintainable generic point.

## Steps Implemented

* **Ubuntu-20.04**
  * `install_uncrustify`
    * Install uncrustify manually from github repo.

* **Ubuntu-22.04**
  * `install_uncrustify`
    * Install uncrustify using apt.

* **Ubuntu (generic)**

  * `set_platform`
    * Set the platform OS version in a environment variable.

  * `install_apt_packages`
    * Install generic apt packages required by these actions and most eProsima projects.
  * `install_python_packages`
    * Install generic python packages required by these actions and most eProsima projects.
  * `install_uncrustify`
    * Install uncrustify depending on the platform.

  * `get_git_diff_files`
    * Get the files that differ from one github reference to another. Can grep result.

## Full Actions Implemented

* **Ubuntu (generic)**
  * `uncrustify`
    * Check the C++ linter of the new files added to the repository.
