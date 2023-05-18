




class Text (object):
    def __init__(self, text) -> None:
        self.__id = None
        self.text = text
    

    def get_dict_content (self):
        return {
            "view_id" : self.__id,
            "vname" : "Text",
            "text" : self.text
        }

    def respown (self, new_id=None):
        if new_id == None: pass
        if self.__id == None:
            self.__id = new_id
        else:
            pass