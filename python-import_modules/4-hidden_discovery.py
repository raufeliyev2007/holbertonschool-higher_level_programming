#!/usr/bin/python3
"""
Print all names from compiled module hidden_4.pyc
"""

import importlib.util
import sys

def main():
    """Load hidden_4.pyc and print names not starting with '__'"""
    file_path = "/tmp/hidden_4.pyc"  # Sandbox path

    # Load module from .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden)

    # Get names not starting with __
    names = [name for name in dir(hidden) if not name.startswith("__")]

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    main()
