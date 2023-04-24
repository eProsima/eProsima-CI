
# eProsima-CI CONTRIBUTIONS GUIDELINES

This file contains some advices and guidelines in order to contribute to the project.

---

## Uniformity

We will try to keep repository as uniform as possible.
Thus, read [code_style](code_style.md), and [multiplatform_support](multiplatform_support.md) in order to make a contribution.

---

## Pull request

As this repository implements CI actions, it is hard to test.
Thus, these are the steps that must be followed in order to make a contribution:

1. Change every `@main` action version of internal actions to your branch name (if applicable, change also the repository owner to the fork owner).
2. Apply and/or add changes.
3. Add a link in the PR to an external PR from other repository using the new features aside with the old ones, all actions using `@<new-branch>` (to check nothing is broken).
4. **After revisions and correction are finished** change every version to `@main` again.

We know this is error-prone as the actual code that is going to be updated is not the same that is being tested.
However, it is the only way to test it so far, as actions names and versions do not allow to be parametrized.
