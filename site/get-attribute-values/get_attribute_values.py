#!/usr/bin/env python3

import boto3
import json

output_file = 'example_output.json'

client = boto3.client('pricing')
paginator = client.get_paginator('get_attribute_values')

prices = []

response_iterator = paginator.paginate(
    ServiceCode='AmazonCognito',
    AttributeName='regionCode',
    PaginationConfig={
        'MaxItems': 3
    }
)

for page in response_iterator:
    print(page)
    #for attr_data in page['PriceList']:
        # print(attr_data)
        # prices.append(json.loads(price_data))

# with open(output_file, 'w') as _json_file:
#     json.dump(prices, _json_file, sort_keys=True, indent=2)


