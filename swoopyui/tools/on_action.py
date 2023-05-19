import threading




def on_view_action (function, args):
    threading.Thread(target=function, args=[*args], daemon=True).start()
    return True