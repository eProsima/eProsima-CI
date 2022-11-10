# Fast-DDS-CI

This is a github CI auxiliary repo that mimics the [gitlab
one](https://gitlab.intranet.eprosima.com/eProsima/fastrtps-ci.git) currently used in the jenkins CI.
The main goals are:
- Keep colcon metas associated with the CI. The repo is used as a dictionary where branches are used as keys.
  Some works have specific branches as the nightlies but generally the CI tries to match the `Fast-DDS` repo branch with
  this repo branch in order to retrieve the metas. If no specific branch is found it fallbacks to main.
- Keep [vcs](https://github.com/dirk-thomas/vcstool) depends files (`.repos`). Philosophy is the same followed in metas
  management.
- Keep github actions associated to the CI workflows. More or less what the `setup.py` files do on the gitlab repo
  aforementioned.
