from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def get_drive_client():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Opens browser for login
    drive = GoogleDrive(gauth)
    return drive
