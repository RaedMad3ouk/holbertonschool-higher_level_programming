#!/usr/bin/python3
"""Module for add_item method"""

import json
import sys
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    file = "add_item.json"
    json_list = load_from_json_file(file) if os.path.exists(file) else []

    for arg in sys.argv[1:]:
        json_list.append(arg)

    save_to_json_file(json_list, file)


if __name__ == "__main__":
    main()
