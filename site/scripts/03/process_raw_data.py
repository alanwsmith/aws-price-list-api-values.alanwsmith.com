#!/usr/bin/env python3

import json
import os

with open('../01/service_list.json') as _service_list_file:
    service_data = json.load(_service_list_file)
    for service in service_data['services']:
        service['attributes'] = []
        for attr_name in service['AttributeNames']:
            new_attribute = {
                'name': attr_name,
                'values': []
            }
            file_path = os.path.join(
                '..', 
                '02', 
                'raw-data', 
                f"{service['ServiceCode']}--{attr_name}.json"
            )
            with open(file_path) as _attr_data:
                attr_data = json.load(_attr_data)
                for attr_value in attr_data['attribute_values']:
                    new_attribute['values'].append(attr_value)
            service['attributes'].append(new_attribute)
        service.pop('AttributeNames', None)

with open('serivce_data.json', 'w') as _service_data_output:
    json.dump(service_data, _service_data_output, sort_keys=True, indent=2)

