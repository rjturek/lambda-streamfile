from __future__ import print_function

import time
import json
import requests

print('............. Loading function ...............')

def lambda_handler(event, context):
    print('Function Start .................')
    print("Received event: " + json.dumps(event, indent=2))

    fileUploaded = event['Records'][0]['s3']['object']['key']
    print(fileUploaded, "uploaded to S3")

    if fileUploaded.startswith("etf"):
        r = requests.get("https://s3.amazonaws.com/skynetdatafiles/" + fileUploaded)
        print(r.text)
        gatewayUrl = "http://skynet.elasticbeanstalk.com/services/stream/publish/skynet-morningstar-feed"
        lineslist = r.text.split('\n')
        print("lineslist length:::", len(lineslist))
        for line in lineslist:
            print("aline:", line)
            r = requests.post(gatewayUrl, data=line, headers={'Connection':'close'})
            print("code", r.status_code)
            time.sleep(.2)
    else:
        print("Not processing:", fileUploaded)


    print('Function End ...................')
    return


if __name__ == '__main__':
    lambda_handler("aaa", "bbb")