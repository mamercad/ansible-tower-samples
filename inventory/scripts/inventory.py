#!/usr/bin/env python3

print("""
{
    "group": {
        "hosts": [
            "127.0.0.1"
        ],
        "vars": {
            "ansible_ssh_user": "nobody"
        }
    },
    "_meta": {
        "hostvars": {
            "127.0.0.1": {
              "foo": "bar"
            }
        }
    }
}
""")
