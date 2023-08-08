from flask import Flask, request, send_file
import socketserver
import tempfile
import threading
import logging
import shutil
import os
import sys

from .api.process_requests import ProcessRequest
from .tools.run_target import run_the_target
from .tools.run_swiftUI import run_swiftUI_app
from .tools.run_swiftUI_ios import prepare_swiftUI_for_ios
from .tools.pyinstaller_check import is_run_on_pyinstaller
from .view import View
     
     
def run_swiftUI_on_new_process (PORT, tmp_dir):
    if not os.path.isdir (tmp_dir) and "swoopyui-ios" not in sys.argv:
        print("Cannot found the temp dir.")
        os._exit(0)
    if "swoopyui-ios" in sys.argv:
        prepare_swiftUI_for_ios(port=PORT)
    else:
        run_swiftUI_app(PORT, tmp_dir)

class app:
    """This is the main function of the app, the function that will run the app and show the window"""
    def __init__(self, target, base_name="__main__") -> None:
        self.__main_view = View(app=self)
        self.__target_function = target
        self.__base_name = base_name
        self.__host()

    def __host (self):
        flask_app = Flask(self.__base_name)

        # Set the logging level to ignore warnings
        log = logging.getLogger('werkzeug')
        log.setLevel(logging.ERROR)

        self.__all_waited_updates = []
        self.__update_number = 0


        @flask_app.route("/", methods=["POST"])
        def index ():
            return ProcessRequest({}, 
                                  request_name="/", 
                                  all_waited_updates=self.__all_waited_updates,
                                  update_number=self.__update_number
                                ).process_get_updates()
        

        @flask_app.route("/get_assets")
        def get_assets ():
            path = request.values['path']
            if os.path.isfile (path):
                return send_file (path)
            else:
                return "error"


        @flask_app.route("/start_the_target_function")
        def start_the_target_function ():
            if "swoopyui-ios" in sys.argv:
                run_the_target(self.__target_function, [self.__main_view], self)
            else:
                threading.Thread(target=run_the_target, args=[self.__target_function, [self.__main_view], self], daemon=True).start()
            return ""
        
        @flask_app.route("/client_side_update", methods=["POST"])
        def client_side_update():
            ProcessRequest({}, request_name="/client_side_update", all_waited_updates=[], main_view=self.__main_view, update_number=self.__update_number).process_client_side_update(request=request)
            return ""

        
        @flask_app.route("/close_the_app")
        def close_the_app ():
            # Remove the temporary dir
            if os.path.isdir (self.current_tmp_dir):
                shutil.rmtree(self.current_tmp_dir)
            # exit the script.
            os._exit(0)

        with socketserver.TCPServer(("localhost", 0), None) as s:
            free_port = s.server_address[1]
            self.app_port = free_port
        
        if is_run_on_pyinstaller():
            self.current_tmp_dir = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
        else:
            if not "swoopyui-ios" in sys.argv:
                self.current_tmp_dir = tempfile.mkdtemp()
        
        if "swoopyui-ios" in sys.argv:
            run_swiftUI_on_new_process(PORT=free_port, tmp_dir="")
        else:
            threading.Thread(target=run_swiftUI_on_new_process, args=[free_port, self.current_tmp_dir]).start()

        flask_app.run(port=free_port)
    
    def set_for_the_next_update_get (self, action_name:str, action_content:dict):
        self.__update_number = self.__update_number + 1
        cont = {"action":f"{action_name}", "action_content":action_content, "update_number":self.__update_number}
        self.__all_waited_updates.append(cont)