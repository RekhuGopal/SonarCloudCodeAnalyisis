import os
import requests
import sys

TOKEN= str(sys.argv[1])
OWNER= str(sys.argv[2])
REPO= str(sys.argv[3])
Workflow_Name= str(sys.argv[4])
parameter1= str(sys.argv[5])
parameter2 = str(sys.argv[6])

print( "the toke value is")
def trigger_workflow(Workflow_Name,parameter1,parameter2):

      headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
      }

      data = {
        "event_type": Workflow_Name,
        "client_payload": {
          'parameter1': parameter1,
          'parameter2': parameter2
        }
      }

      responseValue=requests.post(f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches",json=data,headers=headers)
      print(responseValue.content)

trigger_workflow(Workflow_Name,parameter1,parameter2)