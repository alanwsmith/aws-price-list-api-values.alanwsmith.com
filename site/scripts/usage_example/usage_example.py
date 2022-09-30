#!/usr/bin/env python3

import boto3
import json

client = boto3.client('pricing')
paginator = client.get_paginator('get_products')

response_iterator = paginator.paginate(
    ServiceCode='AmazonEC2',
    Filters=[
        {
            'Type':  'TERM_MATCH',
            'Field': 'regionCode',
            'Value': 'us-east-1'
        },
        {
            'Type':  'TERM_MATCH',
            'Field': 'operatingSystem',
            'Value': 'Linux'
        }
    ],
    FormatVersion='aws_v1',
    PaginationConfig={
        'MaxItems': 5,
    },
)

for page in response_iterator:
    for price_data_string in page['PriceList']:
        price_data = json.loads(price_data_string)
        print(price_data['product']['attributes']['instanceType'])
