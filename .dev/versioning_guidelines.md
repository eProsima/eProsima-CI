
# eProsima-CI VERSIONING GUIDELINES

Versioning in Github actions is very important, as many other projects will be affected from any change in this repository.
These are the main guidelines to versioning this repository.

---

## Versions

### Mayor version

Any change can be done in a mayor version change.

### Minor version

Minor version should preserve old API, as actions names, locations, arguments and arguments names.
It can add new actions or optional arguments
It can change external action versions.

### Patch version

A patch version cannot add or change any API (action or argument name).
It should only fix possible bugs.

---

## Updating version

Steps to update the version of this repository to `vX.Y.Z`:

### If updating the newest version

1. Update [VERSION](../VERSION) file in `main` branch.
1. Update [versions.md](../versions.md) documentation file in `main` branch.
1. Create new branch `X.Y.Z` from `main`.
1. Change to new branch `release/X.Y.Z`.
1. Change every `@<main>` for `@vX.Y.Z` along the project.
1. Set new release in Github: <https://github.com/eProsima/eProsima-CI> as `vX.Y.Z`.
1. Move `vX.Y` tag to refer `vX.Y.Z` tag [commands](#git-commands-for-tags).
1. Move `vX` tag to refer `vX.Y` tag [commands](#git-commands-for-tags).

### If updating a version that is not the last one

1. Create new branch `vX.Y.Z` from base version `vX.Y.Z'`.
1. Update [VERSION](../VERSION) file.
1. Update [versions.md](../versions.md) documentation file.
1. Change every `@vX.Y.Z'` for `@vX.Y.Z` along the project.
1. Set new release in Github: <https://github.com/eProsima/eProsima-CI> (be aware that this set this new release as latest).
1. Move `vX.Y` tag to refer `vX.Y.Z` tag [commands](#git-commands-for-tags).
1. Move `vX` tag to refer `vX.Y` tag if there is not a newer `Y` [commands](#git-commands-for-tags).

#### Git commands for tags

```sh
# Create new tag (from git repo directory checkout to the branch to create new tag)
git tag --annotate vX.Y

# Move new tag (from git repo directory checkout to the branch to move tag)
git tag --annotate --force vX.Y

# Push new tags
git push --tags

# Push tags moved
git push --tags --force
```
