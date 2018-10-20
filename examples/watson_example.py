import json
from watson_developer_cloud import ConversationV1

conversation = ConversationV1(
  username="53fe22a5-1110-4e73-ae06-ddf8b3209b64",
  password="H0kQ2okyrezF",
  version="2018-07-10"
)

workspace_id = "7473ff72-cda0-489f-84b7-ec06509f3fc5"

response = conversation.message(
  workspace_id=workspace_id,
  input={ "text": "Ola" }
)

print(response.result)
