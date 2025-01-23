#!/usr/bin/env python3
"""this python script installs the dependencies
but skips the dependencies that are not available
"""

import subprocess

with open("requirements.txt") as reqs:
    """This function takes in the requirements.txt
    file as input
    """
    for line in reqs:
        package = line.strip()
        if package and not package.startswith("#"):
            try:
                subprocess.check_call(["pip", "install", package])
            except subprocess.CalledProcessError:
                print(f"Skipping {package} due to installation errors.")
