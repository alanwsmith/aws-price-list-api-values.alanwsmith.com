#!/usr/bin/env python3

import boto3
import json

output_file = 'example_output.json'

client = boto3.client('pricing')
paginator = client.get_paginator('get_products')

prices = []

response_iterator = paginator.paginate(
    ServiceCode='AmazonCognito',
    Filters=[
        {
            'Field':'regionCode',
            'Type':'TERM_MATCH',
            'Value':'us-east-1'
        },
    #     {
    #         'Field':'operatingSystem',
    #         'Type':'TERM_MATCH',
    #         'Value':'Linux'
    #     }
     ],

    FormatVersion='aws_v1',
    PaginationConfig={
        'MaxItems': 3
    }
)

for page in response_iterator:
    for price_data in page['PriceList']:
        prices.append(json.loads(price_data))

with open(output_file, 'w') as _json_file:
    json.dump(prices, _json_file, sort_keys=True, indent=2)


