from ftplib import FTP

FTP_HOST = "127.0.1.1"
FTP_PORT = 2121
FTP_USER = "anonymous"
FTP_PASS = "anonymous" 

DOWNLOAD_DIR = "./public"

import os
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def download_all_files():
    try:
        ftp = FTP()
        ftp.connect(FTP_HOST, FTP_PORT)
        ftp.login(user=FTP_USER, passwd=FTP_PASS)

        files = ftp.nlst('.')
        print(f"Files available for download: {files}")

        for file_name in files:
            local_path = os.path.join(DOWNLOAD_DIR, file_name)
            with open(local_path, "wb") as local_file:
                print(f"Downloading {file_name}...")
                ftp.retrbinary(f"RETR {file_name}", local_file.write)
                print(f"{file_name} downloaded to {local_path}")

        ftp.quit()
        print("All files downloaded successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

download_all_files()
