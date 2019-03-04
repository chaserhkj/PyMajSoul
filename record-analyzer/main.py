#!/usr/bin/env python2

from sys import stdin, argv
from os.path import ismount, exists, join
from runpy import run_path
from lib.types import StandardParser

import json
import base64
import StringIO

# Parse arguments
root_type = "root"
filename = argv[1]
with open(filename) as f:
    data = json.load(f)
data = base64.b64decode(data["data"])
buf = StringIO.StringIO(data)

# Load the config
config = {}
directory = "."
while not ismount(directory):
    filename = join(directory, "protobuf_config.py")
    if exists(filename):
        config = run_path(filename)
        break
    directory = join(directory, "..")

# Create and initialize parser with config
parser = StandardParser()
if "types" in config:
    for type, value in config["types"].items():
        type = unicode(type)
        assert(type not in parser.types)
        parser.types[type] = value
if "native_types" in config:
    for type, value in config["native_types"].items():
        parser.native_types[unicode(type)] = value

# Make sure root type is defined and not compactable
if root_type not in parser.types: parser.types[root_type] = {}
parser.types[root_type]["compact"] = False

# PARSE!
print parser.safe_call(parser.match_handler("message"), buf, root_type) + "\n"
exit(1 if len(parser.errors_produced) else 0)
