ansible-playbook tests/test.yml -e "roles_path=$PWD/.."
ansible-playbook tests/test.yml -e "roles_path=$PWD/.." -e "license_changer_check_mode=true"
