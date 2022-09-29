#!/usr/bin/env python3

import boto3
import json

from datetime import datetime 

client = boto3.client('pricing')
paginator = client.get_paginator('describe_services')

tmp_services = []

data = {
    "generated": datetime.now().strftime("%a. %B %-d, %Y"),
    "services": []
}

response_iterator = paginator.paginate()

for page in response_iterator:
    for service in page['Services']:
       tmp_services.append(service)

for service in sorted(tmp_services, key=lambda x: x['ServiceCode'].lower()):
    service['AttributeNames'].sort(key=lambda x: x.lower())
    data['services'].append(service)

with open('service_list.json', 'w') as _json_out:
    json.dump(data, _json_out, indent=2, sort_keys=True)

