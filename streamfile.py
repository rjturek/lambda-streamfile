from __future__ import print_function

import boto3
import botocore

import json

print('............. Loading function ...............')


#conn = S3Connection('AKIAJVIDFQIDLODBK5IA', 'lKQ7WokY7+RKU1cHAZsvywRHtwibbg0kJ+OcsFVp')

def lambda_handler(event, context):
    print('bbbbbbbbbbbbbbbbbbbbbb')
    print("Received event: " + json.dumps(event, indent=2))
    print("File uploaded = " + event['Records'][0]['s3']['object']['key'] + " to S3")
    print('EEEEEEEEEEEEEEEEEEEEEE')

    s3 = boto3.resource('s3')
    # bucket = s3.Bucket('skynetdatafiles')

    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print(key.key)

    return "hey there done"
    #raise Exception('Something went wrong')

##
