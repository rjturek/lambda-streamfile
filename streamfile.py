from __future__ import print_function
from boto.s3.connection import S3Connection

import json

print('............. Loading function ...............')

conn = S3Connection('AKIAJVIDFQIDLODBK5IA', 'lKQ7WokY7+RKU1cHAZsvywRHtwibbg0kJ+OcsFVp')

def lambda_handler(event, context):
    print('bbbbbbbbbbbbbbbbbbbbbb')
    print("Received event: " + json.dumps(event, indent=2))
    print("File uploaded = " + event['Records'][0]['s3']['object']['key'] + " from git")
    print('EEEEEEEEEEEEEEEEEEEEEE')
    return "hey there"
    #raise Exception('Something went wrong')

#
