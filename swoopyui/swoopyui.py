from flask import Flask, request
import socketserver
import random
import threading
import multiprocessing
import sys
import os

from .protocol import onClientRequestUpdate
from .tools.run_target import run_the_target
from .tools.run_swiftUI import run_swiftUI_app
from .view import View


def run_swiftUI_on_new_process (PORT):
    run_swiftUI_app(PORT)

class app:
    """This is the main function of the app, the function that will run the app and show the window"""
    def __init__(self, target) -> None:
        self.__main_view = View(app=self)
        self.__target_function = target
        self.__host()

    def __host (self):
        flask_app = Flask(__name__)
        self.__all_waited_updates = []
        self.__update_number = 0


        @flask_app.route("/", methods=["POST"])
        def index ():
            if self.__all_waited_updates == []:
                return onClientRequestUpdate(
                    self.__update_number, 
                    "", 
                    {"empty":True}).load_as_dict()
            else:
                next_update = self.__all_waited_updates[0]
                action_name = next_update["action"]
                action_content = next_update["action_content"]
                update_number = next_update["update_number"]
                del self.__all_waited_updates[0]
                return onClientRequestUpdate(
                    update_number, 
                    action_name, 
                    action_content).load_as_dict()

        @flask_app.route("/start_the_target_function")
        def start_the_target_function ():
            threading.Thread(target=run_the_target, args=[self.__target_function, [self.__main_view], self], daemon=True).start()
            return ""
        
        @flask_app.route("/close_the_app")
        def close_the_app ():
            os._exit(0)

        with socketserver.TCPServer(("localhost", 0), None) as s:
            free_port = s.server_address[1]
        
        multiprocessing.Process(target=run_swiftUI_on_new_process, args=[free_port]).start()
        flask_app.run(port=free_port)
    
    def set_for_the_next_update_get (self, action_name:str, action_content:dict):
        self.__update_number = self.__update_number + 1
        cont = {"action":f"{action_name}", "action_content":action_content, "update_number":self.__update_number}
        self.__all_waited_updates.append(cont)