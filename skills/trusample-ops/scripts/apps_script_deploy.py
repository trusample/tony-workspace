import sys
sys.path.insert(0, '/home/mhernandez/clawd/skills/trusample-ops/scripts')
from googleapiclient.discovery import build
from google_auth_util import get_creds

CREDS_PATH = '/home/mhernandez/clawd/secrets/google/credentials.json'
TOKEN_PATH = '/home/mhernandez/clawd/secrets/google/token.json'
PROJECT_ID = '1yDT7YEpAVx3OUnSBjxqTgd4OyS0XKaV0-RX4R-dnOI6vcHG2SFzSVK0e'

creds = get_creds(CREDS_PATH, TOKEN_PATH, [])
svc = build('script', 'v1', credentials=creds)

version_resp = svc.projects().versions().create(
    scriptId=PROJECT_ID,
    body={'description': 'Fix getCurrentUser handler'}
).execute()
print('Version created:', version_resp)
version_number = version_resp.get('versionNumber')

deployments = svc.projects().deployments().list(scriptId=PROJECT_ID).execute()
print('Deployments:', deployments)

for d in deployments.get('deployments', []):
    dep_id = d.get('deploymentId')
    config = d.get('deploymentConfig', {})
    if config.get('versionNumber') and dep_id:
        update_resp = svc.projects().deployments().update(
            scriptId=PROJECT_ID,
            deploymentId=dep_id,
            body={'deploymentConfig': {'versionNumber': version_number, 'manifestFileName': 'appsscript', 'description': 'Fix getCurrentUser'}}
        ).execute()
        print('DONE — deployment updated:', update_resp)
        break
