#!/usr/bin/python3
"""Module that adds arguments to a python list"""
import sys

if __name__ == "__main__":
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        json_data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        json_data = []
    json_data.extend(sys.argv[1:])

    save_to_json_file(json_data, "add_item.json")
