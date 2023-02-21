#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Ansible module to manage CheckPoint Firewall (c) 2019
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
---
module: cp_mgmt_delete_repository_package
short_description: Delete the repository software package from the central repository.<br>On Multi-Domain Server this command is available only after logging
in to the Global domain.
description:
  - Delete the repository software package from the central repository.<br>On Multi-Domain Server this command is available only after logging in to the
    Global domain.
  - All operations are performed over Web Services API.
version_added: "6.3.0"
author: "Shiran Golzar (@chkp-shirango)"
options:
  name:
    description:
      - The name of the software package.
    type: str
extends_documentation_fragment: check_point.mgmt.checkpoint_commands
"""

EXAMPLES = """
- name: delete-repository-package
  cp_mgmt_delete_repository_package:
    name: Check_Point_R80_20_JUMBO_HF_Bundle_T118_sk137592_Security_Gateway_and_Standalone_2_6_18_FULL.tgz
    state: absent
"""

RETURN = """
cp_mgmt_delete_repository_package:
  description: The checkpoint delete-repository-package output.
  returned: always.
  type: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.check_point.mgmt.plugins.module_utils.checkpoint import checkpoint_argument_spec_for_commands, \
    api_command


def main():
    argument_spec = dict(
        name=dict(type='str')
    )
    argument_spec.update(checkpoint_argument_spec_for_commands)

    module = AnsibleModule(argument_spec=argument_spec)

    command = "delete-repository-package"

    result = api_command(module, command)
    module.exit_json(**result)


if __name__ == '__main__':
    main()
