from flask import request, Flask



def swoopyui_host_setup (flask_app:Flask, target_function, client_view):
    @flask_app.route("/start_target_function")
    def start_target_function ():
        target_function(client_view)
        return '{"ok":true}'
    
    @flask_app.route("/get_updates")
    def get_updates():
        updts = list(client_view.next_updates)
        client_view.next_updates.clear()
        print(updts)
        return {
            "updts" : updts
        }
    
    @flask_app.route("/push_update")
    def push_update():
        return ""