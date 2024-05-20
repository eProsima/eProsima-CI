#!/bin/bash

red='\E[1;31m'
yellow='\E[1;33m'
textreset='\E[1;0m'

current_dir=$(git rev-parse --show-toplevel)

if [[ ! "$(pwd -P)" -ef "$current_dir" ]]; then
    echo -e "${red}This script must be executed in the repository root directory.${textreset}"
    exit -1
fi

if [[ $# -ne 2 ]]; then
    echo -e "${red}Invalid number of arguments.${textreset}"
    echo "Usage: ./scripts/change_actions_reference.sh [current_reference] [new_reference]"
    echo "Example: ./scripts/change_actions_reference.sh v0.2 feature/my-branch"
fi

current_ref=$1
new_ref=$2

echo -e "Changing current reference ${yellow}@$current_ref${textreset} to ${yellow}@$new_ref${textreset}."

# Substitute the reference in the provided actions
git grep -lz "@$current_ref" -- :^external :^.github :^README.md | xargs -0 sed -i "s+@$current_ref+@$new_ref+g"

# Substitute the reference in the eProsima-CI workflows
git grep -lz "eProsima-CI.*@$current_ref" .github | xargs -0 sed -i "/eProsima-CI/s/@$current_ref/@$new_ref/g"
