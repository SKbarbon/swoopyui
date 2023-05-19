




class onClientRequestUpdate:
    def __init__(self, update_number, action_name, action_content) -> None:
        self.update_number = update_number
        self.action_name = action_name
        self.action_content = action_content
    
    def load_as_dict (self):
        return {
            "update_number" : self.update_number,
            "action" : {
                "name" : str(self.action_name),
                "content" : self.action_content
            }
        }


class ClientSideUpdate:
    def __init__(self, dict) -> None:
        self.update_name = dict["update_name"]
        self.content = dict["content"]