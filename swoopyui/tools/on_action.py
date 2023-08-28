from .check_platform import is_device_a_ios
import threading



def on_view_action (function, args):
    if function == None: return
    threading.Thread(target=function, args=[*args]).start()