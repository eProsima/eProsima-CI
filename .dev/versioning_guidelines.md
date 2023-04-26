
# eProsima-CI VERSIONING GUIDELINES

Versioning in Github actions is very important, as many other projects will be affected from any change in this repository.
These are the main guidelines to versioning this repository.

---

## Versions

### Mayor version

Any change can be done in a mayor version change.

### Minor version

Minor version should preserve old API, as actions names and locations and arguments anrevisionsd arguments names.
It can add new actions or optional arguments
It can change external action versions.

### Patch version

A patch version cannot add or change any API (action or argument name).
It should only fix possible bugs.

---

## Updating version

Steps to update the version of this repository to `vX.Y.Z`:

1. (Only if updating the newest version) Update [VERSION](../VERSION) file in `main` branch.
2. Change to new branch `vX.Y.Z`.
3. Change every `@main` for `@vX.Y.Z` along the project.
4. Set new tag in Github: <https://github.com/eProsima/eProsima-CI>.
5. Move `vX.Y` tag to refer `vX.Y.Z` tag.
6. Move `vX` tag to refer `vX.Y` tag.
