
def run_swiftUI_app (port):
    import subprocess
    # Start the subprocess and capture its output
    swiftUI_app_path = str(__file__).replace("tools/run_swiftUI.py", "assets/swoopyui.app/Contents/MacOS/")
    run_command = r"./swoopyui"
    subprocess.run(f"cd {swiftUI_app_path}\n{run_command} {port}", shell=True)