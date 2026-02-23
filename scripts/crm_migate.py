import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

def authenticate():
    with open('/home/mhernandez/clawd/secrets/google/token.json') as f:
        d = json.load(f)
        creds = Credentials(token=d['token'], refresh_token=d['refresh_token'],
                            token_uri=d['token_uri'], client_id=d['client_id'],
                            client_secret=d['client_secret'])
        creds.refresh(Request())
    return creds

def read_legacy_data(sheet_id, credentials):
    service = build('sheets', 'v4', credentials=credentials)
    legacy_data = {}
    tabs = ['Accounts', 'Contacts', 'Quotes', 'Orders', 'Products']
    for tab in tabs:
        result = service.spreadsheets().values().get(spreadsheetId=sheet_id,
                                                     range=tab).execute()
        legacy_data[tab] = result.get('values', [])
    return legacy_data

def get_or_create_new_sheet(new_sheet_name, credentials):
    drive_service = build('drive', 'v3', credentials=credentials)
    page_token = None
    while True:
        response = drive_service.files().list(q="name='{}' and mimeType='application/vnd.google-apps.spreadsheet'".format(new_sheet_name),
                                              fields='files(id,name)',
                                              pageToken=page_token).execute()
        if response.get('files', []):
            return response.get('files')[0]['id']  # Return existing sheet ID
        else:
            # Create a new sheet if not found
            body = {'properties': {'title': new_sheet_name}}
            sheet = drive_service.files().create(body=body,
                                                 fields='id').execute()
            return sheet['id']

def write_data_to_new_sheet(new_sheet_id, legacy_data, credentials):
    service = build('sheets', 'v4', credentials=credentials)
    for tab, data in legacy_data.items():
        body = {'values': data}
        service.spreadsheets().values().update(spreadsheetId=new_sheet_id,
                                                range=tab,
                                                valueInputOption='RAW',
                                                body=body).execute()
        print(f'Wrote {len(data)} rows to {tab}.')

def main():
    # Read from legacy CRM sheet
    legacy_sheet_id = '1NyYihFTchiur_Nrj5Vz0LSxw1PP4aY6ttctn4G2cT4E'
    creds = authenticate()
    legacy_data = read_legacy_data(legacy_sheet_id, creds)
    new_sheet_id = get_or_create_new_sheet('TruSample CRM Master', creds)
    write_data_to_new_sheet(new_sheet_id, legacy_data, creds)

if __name__ == '__main__':
    main()