import requests


def install_file(url, output_path):
    try:
        # Send a GET request to download the file
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors

        with open(output_path, 'wb') as file:
            file.write(response.content)  # Save the file locally

        print(f"File downloaded and installed successfully at: {output_path}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while downloading the file: {e}")
        return False

def run_swiftUI_app (port):
    # return
    from .unzip_assets import unzip_file
    import subprocess
    import os

    # Start the subprocess and capture its output
    swiftUI_app_path = str(__file__).replace("tools/run_swiftUI.py", "assets/swoopyui.app/Contents/MacOS/")
    zip_path = str(__file__).replace("tools/run_swiftUI.py", "assets/swoopyui.zip")
    github_zip_url = "https://raw.githubusercontent.com/SKbarbon/swoopyui/main/swoopyui/assets/swoopyui.zip"
    if not os.path.isdir (swiftUI_app_path):
        if not os.path.isfile (zip_path):
            print("WARNING: swiftUI client is not found!")
            print("installing swiftUI client app from github ..")
            result_of_installing = install_file(github_zip_url, zip_path)
            if result_of_installing == True:
                print("installing swiftUI client is done!")
            else:
                print("Cannot install swiftUI client!")
                os._exit(0)
        unzip_file (str(swiftUI_app_path).replace("swoopyui.app/Contents/MacOS/", "swoopyui.zip"), str(__file__).replace("tools/run_swiftUI.py", "assets/"))
    run_command = r"./swoopyui"

    subprocess.run(f"cd {swiftUI_app_path}\nchmod +x swoopyui\n{run_command} {port}", shell=True, stdout=None)