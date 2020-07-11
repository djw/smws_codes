#!/usr/bin/env python

import sys
import os
from jinja2 import FileSystemLoader, Environment
import json

def main():
    with open("data.json", "r") as f:
        whiskies = []
        for code, info in json.load(f).items():
            info["code"] = code
            whiskies.append(info)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('whisky.html')

    print(template.render(whiskies=whiskies))


if __name__ == '__main__':
    main()

