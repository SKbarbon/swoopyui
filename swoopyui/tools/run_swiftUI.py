import subprocess
import os
import shutil
import requests
from .unzip_assets import unzip_file
from .pyinstaller_check import is_run_on_pyinstaller

def run_swiftUI_app(port, tmp_dir, view_mode):
    # get the current temporary folder.
    temp_dir = tmp_dir

    # Prepare paths
    zip_file_name = "swoopyui.zip"
    if view_mode == "app":
        zip_file_name = "swoopyui.zip"
    elif view_mode == "agent":
        zip_file_name = "swoopyui_agent.zip"
    elif view_mode == "menu_bar_extra":
        zip_file_name = "swoopyui_menubarextra.zip"
    else:
        print(f"Warning: There is no app mode named '{view_mode}'. Running as 'app' mode.")
        zip_file_name = "swoopyui.zip"

    zip_path = str(__file__).replace("tools/run_swiftUI.py", f"assets/{zip_file_name}")
    new_app_path = os.path.join(temp_dir, "swoopyui.app/")

    if is_run_on_pyinstaller():
        # install the zip file from github
        url = "https://raw.githubusercontent.com/SKbarbon/swoopyui/main/swoopyui/assets/swoopyui.zip"
        path_of_installed_zip = os.path.join(temp_dir, "app_zip_file")
        with open(path_of_installed_zip, "wb") as f:
            f.write(requests.get(url).content)
        zip_path = path_of_installed_zip

    # unzip the app on the temporary folder
    unzip_file(zip_path=zip_path, destination_path=temp_dir)

    # prepare the commands
    executable_of_the_app = os.path.join(new_app_path, "Contents/MacOS/swoopyui")
    chmod_command = ["chmod", "+x", executable_of_the_app]

    # run the `chmod` command
    subprocess.run(chmod_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # run the command the will start the swiftUI app
    run_command = [executable_of_the_app, str(port)]
    subprocess.run(
        run_command, 
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL,
        env={
            "host_port" : str(port)
        }
    )

    # Remove the temporary dir.
    if os.path.isdir (temp_dir):
        shutil.rmtree(temp_dir)