import sys
from googleapiclient.discovery import build
from google_auth_util import get_creds

# Function to create a new Google Sheet

def create_sheet(title, credentials_path, token_path):
    creds = get_creds(credentials_path, token_path, [])
    service = build('sheets', 'v4', credentials=creds)

    # Create a new spreadsheet
    spreadsheet_body = {
        'properties': {'title': title},
        'sheets': [
            {'properties': {'title': 'Accounts'}},
            {'properties': {'title': 'Contacts'}},
            {'properties': {'title': 'Quotes'}},
            {'properties': {'title': 'Orders'}},
            {'properties': {'title': 'Products'}},
            {'properties': {'title': 'Inventory'}}
        ]
    }
    spreadsheet = service.spreadsheets().create(body=spreadsheet_body).execute()
    return spreadsheet['spreadsheetId']

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: python sheets_create.py <title> <credentials_path> <token_path>')
        sys.exit(1)
    title = sys.argv[1]
    credentials_path = sys.argv[2]
    token_path = sys.argv[3]
    sheet_id = create_sheet(title, credentials_path, token_path)
    print(f'New sheet created with ID: {sheet_id}')