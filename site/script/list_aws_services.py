#!/usr/bin/env python3

import boto3

client = boto3.client('pricing')
paginator = client.get_paginator('describe_services')

services = []

response_iterator = paginator.paginate()

for page in response_iterator:
    for service in page['Services']:
        services.append(service)

with open('services.txt', 'w') as _out:
    for item in sorted(services, key=lambda x: x['ServiceCode'].lower()):
        _out.write(f"- {item['ServiceCode']}\n")
        for attribute in sorted(item['AttributeNames'], key=lambda x: x.lower()): 
            _out.write(f"  - {attribute}\n")



