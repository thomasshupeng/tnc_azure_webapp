"""
File Name: Test_PredictImage.py
v 1.0

This program tests the RESTful API (PredictImage) for TNC project

7/1/2018
Shu Peng
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
import ssl
import socket

USING_HTTPS = True
HOST_NAME = 'shpengD3'

IPAddr = socket.gethostbyname(HOST_NAME)
PORT_NUMBER = 5000
if USING_HTTPS:
    PORT_NUMBER = 443
headers = {
    # Request headers
    'Content-Type': 'multipart/form-data',
    'Prediction-key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': 'iteration#2',
    'application': 'Test_PredictImage.py',
})

test_file = "L-LJS17-EBF-0045.JPG"

try:
    with open(test_file, 'rb') as f:
        if USING_HTTPS:
            conn = http.client.HTTPSConnection(IPAddr, port=PORT_NUMBER, context=ssl._create_unverified_context())
        else:
            conn = http.client.HTTPConnection(IPAddr, port=PORT_NUMBER)

        conn.request("POST", "/tncapi/v1.0/Prediction/11111111/image?{!s}".format(params), body=f.read(), headers=headers)
        response = conn.getresponse()
        data = response.read()
        json_response = json.loads(data)
        predictions = json_response.get('Predictions')
        if len(predictions) >= 1:
            for pred in predictions:
                print("I'm [{!s}] sure this is a {!s}.".format(pred.get('Probability'), pred.get('Tag')))
        conn.close()

except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
