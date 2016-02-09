from __future__ import print_function

import time
import json
import requests

print('............. Loading function ...............')

def lambda_handler(event, context):
    print('Function Start .................')

    print("Received event: " + json.dumps(event, indent=2))
    print("event type:", type(event))
    print(event)

    fileUploaded = event['Records'][0]['s3']['object']['key']
    print(fileUploaded, "uploaded to S3")

    if fileUploaded.startswith("etf"):
        r = requests.get("https://s3.amazonaws.com/skynetdatafiles/" + fileUploaded)
        print(r.text)
        gatewayUrl = "http://skynet.elasticbeanstalk.com/services/stream/publish/skynet-morningstar-feed"
        lineslist = r.text.split('\n')

        num_rows = len(lineslist) - 1

        print("number of data rows:", num_rows)

        row_index = 0
        for line in lineslist:
            row_index = row_index + 1
            ext_line = str(row_index) + "," + str(num_rows) + "," + line

            if row_index > num_rows:
                # ext_line = "[EOF] filename: " + fileUploaded
                break

            print("aline:", ext_line)

            r = requests.post(gatewayUrl, data=ext_line, headers={'Connection':'close'})
            print("code", r.status_code)

            # time.sleep(.05)
    else:
        print("Not processing:", fileUploaded)


    print('Function End ...................')
    return "done"


# "key": "etf-2016-02-09.csv",
# "key": "etf-testSmall.csv",

testEvent = """
{
 "Records": [
 {
 "eventVersion": "2.0",
 "eventTime": "2016-02-09T13:08:23.321Z",
 "requestParameters": {
 "sourceIPAddress": "69.137.237.170"
 },
 "s3": {
 "configurationId": "0100e47e-f3f6-46d2-aedc-e7efc889a7c8",
 "object": {
 "eTag": "d140625bbfa3fca0a6cf07de7dae960d",
 "sequencer": "0056B9E4C718D8D0D8",
 "key": "etf-testSmall.csv",
 "size": 87099
 },
 "bucket": {
 "arn": "arn:aws:s3:::skynetdatafiles",
 "name": "skynetdatafiles",
 "ownerIdentity": {
 "principalId": "A3DKUO1WZYL8RN"
 }
 },
 "s3SchemaVersion": "1.0"
 },
 "responseElements": {
 "x-amz-id-2": "nI3fypF8mQGrUcNmGtOumSmHpjYSJ2uW8nuREgehCx2KxQ5kH6IH0SGLqDv/0BIE",
 "x-amz-request-id": "06BD05366FF3214F"
 },
 "awsRegion": "us-east-1",
 "eventName": "ObjectCreated:Put",
 "userIdentity": {
 "principalId": "AWS:AIDAJKCGBQKRN2I4T7R3S"
 },
 "eventSource": "aws:s3"
 }
 ]
}
"""

if __name__ == '__main__':
    lambda_handler(json.loads(testEvent), None)