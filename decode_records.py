#!/usr/bin/env python3
from PyMajsoul import majsoul_pb2 as pb
import json
import sys
import base64
from google.protobuf.json_format import MessageToDict

filename = sys.argv[1]
with open(filename) as f:
    data = json.load(f)
if "records" in data:
    print("Decoded records present in {}, exiting".format(filename))
    sys.exit(0)
blob = base64.b64decode(data['data'])

wrapper = pb.Wrapper()
wrapper.ParseFromString(blob)
assert wrapper.name == '.lq.GameDetailRecords'
records_data = wrapper.data

records = pb.GameDetailRecords()
records.ParseFromString(records_data)
records = records.records

results = []
for record in records:
    wrapper = pb.Wrapper()
    wrapper.ParseFromString(record)
    name = wrapper.name.replace(".lq.", "")
    cls = getattr(pb, name)
    obj = cls()
    obj.ParseFromString(wrapper.data)
    result = MessageToDict(obj)
    result['@type'] = name
    results.append(result)
data["records"] = results

with open(filename, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Processed {}".format(filename))


