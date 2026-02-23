import sys
sys.path.insert(0,'skills/trusample-ops/scripts')
from googleapiclient.discovery import build
from google_auth_util import get_creds

creds = get_creds('secrets/google/credentials.json','secrets/google/token.json',[])
svc = build('drive','v3',credentials=creds)

folders = {'crm_code':'15PRihYbh_7qW7_Ltg_WkbZoP0i2-eGHH','Spreadsheets':'11R1C5gSWL-RZS2YmQlduY5RfNidv0Kzz','Templates':'1ORkzxSsXb3RYgrFmWPaxgyPv0g1P3Hjc'}

for name,fid in folders.items():
    res = svc.files().list(q=f"'{fid}' in parents",fields='files(id,name,mimeType)').execute()
    print(f'--- {name} ---')
    for f in res.get('files', []):
        print(f['name'], f['id'])
