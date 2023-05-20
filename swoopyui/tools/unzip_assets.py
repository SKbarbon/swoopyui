import zipfile


def unzip_file(zip_path, destination_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(destination_path)
    except FileNotFoundError:
        print("The specified file does not exist.")
    except zipfile.BadZipFile:
        print("The specified file is not a valid ZIP archive.")