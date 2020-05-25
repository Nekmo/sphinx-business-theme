from __future__ import print_function
import pickle
import os
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
import mimetypes
from googleapiclient.http import MediaFileUpload

SCOPES = [
    'https://www.googleapis.com/auth/drive',
]
DIRECTORY = os.path.expanduser('~/.config/google-drive/')


mimetypes.init()


class GoogleDrive:
    def __init__(self):
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)
        credentials = None
        token_file = os.path.join(DIRECTORY, 'token.pickle')
        credentials_file = os.path.join(DIRECTORY, 'credentials.json')
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(token_file):
            with open(token_file, 'rb') as token:
                credentials = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            elif not os.path.lexists(credentials_file):
                raise OSError('Download credentials.json file to {}.\n'
                              'More help: '
                              'https://developers.google.com/drive/api/v3/quickstart/python'.format(credentials_file))
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, SCOPES)
                credentials = flow.run_local_server()
            # Save the credentials for the next run
            with open(token_file, 'wb') as token:
                pickle.dump(credentials, token)
        self.service = build('drive', 'v3', credentials=credentials)

    def find_file(self, filename, folder=None):
        q = "name='{}' and trashed=False".format(filename)
        if folder:
            q += " and '{}' in parents".format(folder)
        results = self.service.files().list(
            pageSize=1, fields="nextPageToken, files(id, name)",
            # includeItemsFromAllDrives=True,
            q=q).execute()
        files = iter(results['files'])
        return next(files, None)

    def upload(self, local_file, remote_file='', folder=None, overwrite=True):
        remote_file = remote_file or os.path.basename(local_file)
        file_metadata = {'name': remote_file}
        if folder:
            file_metadata['parents'] = [folder]
        media = MediaFileUpload(local_file, mimetype=mimetypes.MimeTypes().guess_type(local_file)[0])
        current_file = self.find_file(remote_file, folder) if overwrite else None
        if current_file:
            file = self.service.files().update(fileId=current_file['id'],
                                               media_body=media,
                                               fields='id').execute()
        else:
            file = self.service.files().create(body=file_metadata,
                                               media_body=media,
                                               fields='id').execute()
        return file.get('id')
