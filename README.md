License_changer
=========

This ansible role changes the license files in a project. It is git aware.

Requirements
------------

Ansible 2.5 or higher is required.

Role Variables
--------------
```YAML
license_changer_project_dir: "/your/project/"
license_changer_project_file_regexp: "*"  # The regular expression for the filenames that need a license
license_changer_header_file: "/your/project/LICENSE" # The license header file
license_changer_header_prefix: '# '  # All the lines in the header will have this prefix
license_changer_header_suffix: ''  # All the lines in the header will have this suffix
license_changer_check_mode: False
license_changer_header_before: BOF  # Same as blockinfile before
license_changer_header_after: EOF  # Same as blockinfile after
license_changer_header_start: "# -----"  # First line of the header.
license_changer_header_end: "# ....." # Last line of the header
# These acts as a boundary. Next time you change the license everything between start
# and end is changed
```
Example Playbook
----------------

An example playbook can be found [here](license_project.yml).

License
-------

MIT (Expat) License

Author Information
------------------

Sequencing Analysis Support Core at Leiden University Medical Center
