
#! The script that will start the python host and run the user's app.

# clear paths
import os, shutil
documents_dir_path = os.path.expanduser('~/Documents')
swoopyui_temp_dir = os.path.join(documents_dir_path, "swoopyui_temp")
if os.path.isdir(swoopyui_temp_dir):
    shutil.rmtree(swoopyui_temp_dir)

# Setup the tag so swoopyui library knows the platform.
import sys
sys.argv.append('swoopyui-ios')

# Start executing user's app.
import threading

def user_app_executer ():
    from swoopyui_app.main import main
    main()


user_app_executer()
print("Python end..")
