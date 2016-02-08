from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
    print('BBBBBBBBBBBBBBBBBBBBBB')
    print("Received event: " + json.dumps(event, indent=2))
    print("File uploaded = " + event['Records'][0]['s3']['object']['key'] + " from git")
    print('EEEEEEEEEEEEEEEEEEEEEE')
    return "hey there"
    #raise Exception('Something went wrong')

#
