import os
import time
from pydrive.drive import GoogleDrive
from drive_auth import get_drive_client


WATCHED_FOLDER = "watched_folder"

def upload_to_drive(file_path, drive_folder_id, drive):
    file_name = os.path.basename(file_path)
    gfile = drive.CreateFile({"title": file_name, "parents": [{"id": drive_folder_id}]})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"Uploaded: {file_name}")

def main():
    drive = get_drive_client()

    folder_metadata = {
        "title": "Raspi Cloud Uploads",
        "mimeType": "application/vnd.google-apps.folder"
    }
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    drive_folder_id = folder['id']

    print(f"Google Drive Folder Created: {drive_folder_id}")

    uploaded_files = set()

    while True:
        for filename in os.listdir(WATCHED_FOLDER):
            file_path = os.path.join(WATCHED_FOLDER, filename)

            if filename not in uploaded_files and os.path.isfile(file_path):
                upload_to_drive(file_path, drive_folder_id, drive)
                uploaded_files.add(filename)

        time.sleep(5)  # Har 5 sec check karega

if __name__ == "__main__":
    main()
