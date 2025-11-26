import os
import gdown
import zipfile

def download_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_folder = os.path.join(project_root, "data")

    zip_filename = "data.zip"
    zip_path = os.path.join(project_root, zip_filename)

    # Checking if data folder exists
    if os.path.exists(data_folder):
        print("Data folder already exists at : ", data_folder)
        return
    # Downloading
    file_id = "10LJNkJvxs3Mxd0eqjWxBQIFDE5EBMJJ9"
    url = f'https://drive.google.com/uc?id={file_id}'

    print("Downloading data from Google Drive... (it may take a while)")

    try:
        gdown.download(url, zip_path, quiet=False)
        print("Download completed successfully ! \n Now extracting...")

        # Extraction
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(project_root)
        print("Data extracted to : ", project_root)

        os.remove(zip_path)

    except Exception as e:
        print(f"Download failed (good luck, you can download it manually) : {e}")

    