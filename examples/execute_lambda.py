# -*- coding: utf-8 -*-
import json, sys
from boto3 import client

lb = client('lambda')

try:
  lambda_name = sys.argv[1]
except IndexError as err:
  print(err)
  print('Você precisa informar o nome da lambda')
  sys.exit()

print('Invocando lambda: %s' % (lambda_name))

payload = { "message": "Testando funcão" }

response = lb.invoke(FunctionName=lambda_name,Payload=json.dumps(payload))
responseDict = json.loads(response['Payload'].read().decode('utf-8'))

print(json.dumps(responseDict, indent=2))
