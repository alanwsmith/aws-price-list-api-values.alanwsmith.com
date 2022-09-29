#!/usr/bin/env python3

import boto3
import json

output_file = usage_example_output.json

client = boto3.client('pricing')
paginator = client.get_paginator('get_products')

prices = []

response_iterator = paginator.paginate(
    ServiceCode='AmazonEC2'
    Filters=[
        {
            'Field':'regionCode',
            'Type':'TERM_MATCH',
            'Value':'us-east-1'
        },
        {
            'Field':'operatingSystem',
            'Type':'TERM_MATCH',
            'Value':'Linux'
        }
    ],
    FormatVersion='aws_v1',
    PaginationConfig={
        'MaxItems': 5
    },
)

for page in response_iterator:
    for price_data in page['PriceList']:
        prices.append(json.loads(price_data))

with open('data.json', 'w') as _json_file:
    json.dump(prices, _json_file, sort_keys=True, indent=2)


