from drive_auth import get_drive_client

if __name__ == "__main__":
    drive = get_drive_client()
    print("Login successful, Google Drive connected!")
