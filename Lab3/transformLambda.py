from __future__ import print_function
import base64
import json

print('Loading function')


def lambda_handler(event, context):
    output = []
    for record in event['records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['data']) + "\n"
        output_record = {
        'recordId': record['recordId'],
        'result': 'Ok',
        'data': base64.b64encode(payload)
        }

        output.append(output_record)

    return {'records': output}
