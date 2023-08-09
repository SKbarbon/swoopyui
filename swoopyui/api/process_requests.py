from ..protocol import onClientRequestUpdate
import json


class ProcessRequest:
    """Process the new requests that comes from the client"""
    def __init__(self, dict_data:dict, request_name:str, all_waited_updates, main_view=None, update_number=0) -> None:
        self.__all_waited_updates = all_waited_updates
        self.__main_view = main_view
        self.__update_number = update_number

    
    def process_get_updates (self):
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

    def process_client_side_update (self, request):
        """This will be called on client side update. Like when user click a button this will be called"""
        json_data = request.get_json()
        update_name = json_data.get('update_name')
        if update_name == "on_view_action":
            self.__main_view.manage_on_view_action(json_data.get("update_content"))