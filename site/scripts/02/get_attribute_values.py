#!/usr/bin/env python3

import boto3
import json

from pathlib import Path

# NOTE: This stores files in a sub-directory
# to get updated data, the files need to be
# removed. (if a file exists, the data isn't
# pulled again which made it easier to test
# during development. 


client = boto3.client('pricing')
paginator = client.get_paginator('get_attribute_values')

# response_iterator = paginator.paginate(
#     ServiceCode='A4B',
#     AttributeName='deploymentModel',
# )

# attr_values = []

# for page in response_iterator:
#     for attr_value in page['AttributeValues']:
#         attr_values.append(attr_value['Value'])
# print(attr_values)

with open('../01/service_list.json') as _json_in:
    service_data = json.load(_json_in)

for service in service_data['services']:
    print(service['ServiceCode'])
    service['attributes'] = []
    for attr_name in service['AttributeNames']:
        print(f"- {attr_name}")
        file_name = f"raw-data/{service['ServiceCode']}--{attr_name}.json"
        if not Path(file_name).is_file():
            response_iterator = paginator.paginate(
                ServiceCode=service['ServiceCode'],
                AttributeName=attr_name,
                PaginationConfig={ 
                    'MaxItems': 1000
                }
            )
            attr_values = []
            for page in response_iterator:
                for attr_value in page['AttributeValues']:
                    print(f"-- {attr_value['Value']}")
                    attr_values.append(attr_value['Value'])
            attr_values.sort(key=lambda x: x.lower())

            payload = {
                "service_code": service['ServiceCode'],
                "attribute": attr_name,
                "attribute_values": attr_values
            }

            # print(payload)

            with open(file_name, 'w') as _json_out:
                json.dump(payload, _json_out)


