#!/usr/bin/env bash
project_root=$(git rev-parse --show-toplevel)
ansible-playbook license_project.yml -e "license_changer_check_mode=true roles_path=$project_root/.."
