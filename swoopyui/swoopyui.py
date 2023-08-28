from .tools.swoopyui_host import swoopyui_host_setup
from .tools.check_platform import is_device_a_ios, is_device_a_mac
from .tools.run_target import run_the_target
from .tools.run_swiftUI_ios import prepare_swiftUI_for_ios
from .tools.get_free_port import get_free_port
from .view import View
from flask import Flask, request
import logging, threading



class app:
    def __init__(self, target, base_name="__main__", debug:bool=False) -> None:
        self.target_function = target
        self.base_name = base_name
        self.debug = debug

        self.host_port = get_free_port()
        self.next_get_updates_responses = []

        self.client_view = View(host_port=self.host_port, host_app_class=self)

        # start the host
        print("Host started..")
        self.host()

    def host (self):
        self.flask_app = Flask(self.base_name)
        flask_app = self.flask_app

        # Set the logging level to ignore warnings
        if self.debug == False:
            log = logging.getLogger('werkzeug')
            log.setLevel(logging.ERROR)
        
        @flask_app.route("/start_target_function")
        def start_target_function ():
            print("A swiftUI client connected..")
            threading.Thread(target=run_the_target, args=[self.target_function, [self.client_view]]).start()
            return '{"ok":true}'
        
        @flask_app.route("/get_updates")
        def get_updates():
            updts = list(self.next_get_updates_responses)
            self.next_get_updates_responses.clear()
            return {
                "updts" : updts
            }
        
        @flask_app.route("/push_update", methods=['POST'])
        def push_update():
            self.client_view.process_client_events(request.json)
            return ""
        

        if is_device_a_ios():
            prepare_swiftUI_for_ios(port=self.host_port)

        flask_app.run(host="localhost", port=self.host_port)