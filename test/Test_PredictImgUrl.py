import http.client
import urllib.request, urllib.parse, urllib.error
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
    'Content-Type': 'application/json',
    'Prediction-key': '{subscription key}',
}

params = urllib.parse.urlencode({
    # Request parameters
    'iterationId': 'iteration#1',
    'application': 'Test_PredictImgUrl.py',
})

body = {"Url": "https://theartmad.com/wp-content/uploads/2015/02/Cute-Baby-Monkeys-3.jpg"}

json_body = json.dumps(body)
try:
    if USING_HTTPS:
        conn = http.client.HTTPSConnection(IPAddr, port=PORT_NUMBER, context=ssl._create_unverified_context())
    else:
        conn = http.client.HTTPConnection(IPAddr, port=PORT_NUMBER)
    conn.request("POST", "/tncapi/v1.0/Prediction/11111111/url?{!s}".format(params), json_body, headers)
    response = conn.getresponse()
    data = response.read()
    json_response = json.loads(data)
    predictions = json_response.get('Predictions')
    if len(predictions) >= 1:
        for pred in predictions:
            print("I'm [{!s}] sure this is a {!s}.".format(pred.get('Probability'), pred.get('Tag')))
    conn.close()
except Exception as e:
    print("[Error {0}] {1}".format(e.errno, e.strerror))
