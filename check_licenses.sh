#!/usr/bin/env bash
ansible-playbook license_project.yml -e "license_changer_check_mode=true roles_path=$PWD/.."
