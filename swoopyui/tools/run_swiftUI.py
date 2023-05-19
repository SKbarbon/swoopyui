

def run_swiftUI_app (port):
    # return
    from .unzip_assets import unzip_file
    import subprocess
    import os
    # Start the subprocess and capture its output
    swiftUI_app_path = str(__file__).replace("tools/run_swiftUI.py", "assets/swoopyui.app/Contents/MacOS/")
    if not os.path.isdir (swiftUI_app_path):
        unzip_file (str(swiftUI_app_path).replace("swoopyui.app/Contents/MacOS/", "swoopyui.zip"), str(__file__).replace("tools/run_swiftUI.py", "assets/"))
    run_command = r"./swoopyui"

    subprocess.run(f"cd {swiftUI_app_path}\nchmod +x swoopyui\n{run_command} {port}", shell=True, stdout=None)