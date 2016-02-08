from __future__ import print_function

import json
import requests

print('............. Loading function ...............')

def lambda_handler(event, context):
    print('Function Start .................')
    print("Received event: " + json.dumps(event, indent=2))

    fileUploaded = event['Records'][0]['s3']['object']['key'] + " to S3"
    print(fileUploaded)
    print('Function End ...................')

    if fileUploaded == "yummyfood.csv":
        r = requests.get("https://s3.amazonaws.com/skynetdatafiles/yummyfood.csv")
        print(r.text)

    return "File contents streamed to Data Pipe Gateway"
