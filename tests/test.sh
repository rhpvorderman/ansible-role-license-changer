#!/usr/bin/env bash
project_root=$(git rev-parse --show-toplevel)
ansible-playbook tests/test.yml -e "roles_path=$project_root/.."
ansible-playbook tests/test.yml -e "roles_path=$project_root/.." -e "license_changer_check_mode=true"
