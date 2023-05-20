import subprocess
import os
import shutil
from .unzip_assets import unzip_file

def run_swiftUI_app(port, tmp_dir):
    temp_dir = tmp_dir
    print(f"tmp exist: {os.path.isdir(temp_dir)}")

    zip_path = str(__file__).replace("tools/run_swiftUI.py", "assets/swoopyui.zip")
    new_app_path = os.path.join(temp_dir, "swoopyui.app/")

    unzip_file(zip_path=zip_path, destination_path=temp_dir)

    executable_of_the_app = os.path.join(new_app_path, "Contents/MacOS/swoopyui")
    chmod_command = ["chmod", "+x", executable_of_the_app]

    subprocess.run(chmod_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    run_command = [executable_of_the_app, str(port)]
    subprocess.run(run_command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(temp_dir)
    shutil.rmtree(temp_dir)