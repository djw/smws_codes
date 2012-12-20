#!/usr/bin/env python
# encoding: utf-8

import sys
import os
from jinja2 import FileSystemLoader, Environment
import json

def main():
    f = open("data.json", "r")

    whiskies = []
    for num, info in json.load(f).items():
        info["number"] = int(num)
        whiskies.append(info)

    whiskies = sorted(whiskies, key=lambda w: w["number"])

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('whisky.html')

    print template.render(whiskies=whiskies)


if __name__ == '__main__':
    main()

