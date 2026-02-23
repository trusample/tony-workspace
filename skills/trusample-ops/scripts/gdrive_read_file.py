import sys
from googleapiclient.discovery import build
from google_auth_util import get_creds

def read_file(file_id):
    # Get credentials
    creds = get_creds('/home/mhernandez/clawd/secrets/google/credentials.json','/home/mhernandez/clawd/secrets/google/token.json',[])
    # Build Drive API service
    service = build('drive', 'v3', credentials=creds)
    # Call the Drive API to get the file content
    request = service.files().get_media(fileId=file_id)
    file_content = request.execute()  # Reading file content
    return file_content.decode('utf-8')  # Decode to string

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python gdrive_read_file.py <file_id>')
        sys.exit(1)
    file_id = sys.argv[1]
    content = read_file(file_id)
    print(content)