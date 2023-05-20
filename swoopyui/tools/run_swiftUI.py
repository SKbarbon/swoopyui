from .unzip_assets import unzip_file
import requests
import tempfile
import shutil
import subprocess
import os

def run_swiftUI_app (port, tmp_dir):
    # return
    from .unzip_assets import unzip_file
    import subprocess
    import os

    # Create a temporary directory.

    temp_dir = tmp_dir

    # Generate the path that the app will be in.
    zip_path = str(__file__).replace("tools/run_swiftUI.py", "assets/swoopyui.zip")

    new_app_path = os.path.join(temp_dir, "swoopyui.app/")

    unzip_file (zip_path=zip_path, destination_path=temp_dir)

    # Start the subprocess to run the app

    executble_of_the_app = os.path.join(new_app_path, "Contents/MacOS/")

    run_command = r"./swoopyui"
    subprocess.run(f"cd {executble_of_the_app}\nchmod +x swoopyui\n{run_command} {port}", shell=True, stdout=None)

    # delete the temp after done using the app
    print(temp_dir)
    shutil.rmtree(temp_dir)