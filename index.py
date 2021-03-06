# -*- coding: utf-8 -*-

import os, sys
# Allow import modules by /site-packages
sys.path.append(os.getcwd() + '/site-packages')

import json
from watson_developer_cloud import ConversationV1

def searchOnWatson(message):
  conversation = ConversationV1(
    username="53fe22a5-1110-4e73-ae06-ddf8b3209b64",
    password="H0kQ2okyrezF",
    version="2018-07-10"
  )
  workspace_id = "7473ff72-cda0-489f-84b7-ec06509f3fc5"
  response = conversation.message(
    workspace_id=workspace_id,
    input={ "text": message }
  )

  return response.get_result()


def handler(event, context):
  message = event['message'] if 'message' in event else None

  watsonResponseText = None
  qnamakerResponseText = None
  if message:
    watsonResponse = searchOnWatson(message)
    if len(watsonResponse['output']['text']) > 0:
      watsonResponseText = watsonResponse['output']['text'][0]

    if 'kb_search' in watsonResponse['context']:
      print(2)

    print(watsonResponse['output']['text'][0])

  return {
    "statusCode": 200,
    "body": json.dumps({ "watson_response_text": watsonResponseText, 'qna_maker_text': qnamakerResponseText })
  }

# payload = {
#   'message': 'Qual é a localizacao do lugar?'
# }

# print(json.dumps(handler(payload, None), indent=2))
