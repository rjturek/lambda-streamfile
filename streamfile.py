from __future__ import print_function

import json

print('Loading function')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print("File uploaded = " + event['Records'][0].s3.key + " from git")
    return "hey there"
    #raise Exception('Something went wrong')

#
