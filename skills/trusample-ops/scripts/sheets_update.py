import sys
from googleapiclient.discovery import build
from google_auth_util import get_creds

# Function to add rows to a Google Sheet

def add_rows(sheet_id, credentials_path, token_path, tab_name, *rows):
    # Get credentials
    creds = get_creds(credentials_path, token_path, [])
    # Build service
    service = build('sheets', 'v4', credentials=creds)

    # Prepare the data to write
    body = {
        'values': [list(row) for row in rows]
    }

    # Update the specified range
    request = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=f'{tab_name}!A1',
        valueInputOption='RAW',
        body=body
    )
    response = request.execute()
    print(f'Response: {response.get("id")}')
    return response


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: python sheets_update.py --sheet-id SHEET_ID --credentials PATH --token PATH --add-rows TAB_NAME ROWS...')
        sys.exit(1)
    sheet_id = sys.argv[2]
    credentials_path = sys.argv[4]
    token_path = sys.argv[6]
    tab_name = sys.argv[8]
    rows = sys.argv[9:]
    add_rows(sheet_id, credentials_path, token_path, tab_name, *rows)  
    " ]"