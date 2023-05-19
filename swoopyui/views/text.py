from ..tools.on_action import on_view_action


class Text (object):
    def __init__(self, text, foreground_color="black", background_color="white", on_hover=None) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__text = text
        self.__foreground_color = foreground_color
        self.__background_color = background_color
        self.on_hover = on_hover
    

    def get_dict_content (self):
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "Text",
            "text" : self.__text,
            "fgcolor" : self.__foreground_color,
            "bgcolor" : self.__background_color
        }

    def respown (self, new_id=None, mother_view=None, parent=None):
        if new_id == None: return
        if mother_view == None: return
        if parent == None: return

        if self.__id == None:
            self.__id = new_id
            self.__last_view_id = new_id
        
        if self.__mother_view == None:
            self.__mother_view = mother_view
        
        if self.__parent_view == None:
            self.__parent_view = parent
    
    def view_action (self, action_data):
        action_name = action_data['action_name']
        if action_name == "on_hover":
            hover_state = action_data['hover_state']
            on_view_action(self.on_hover, [self, {"state":hover_state}])
    
    @property
    def id (self):
        return self.__id

    @property
    def text (self): return self.__text

    @text.setter
    def text (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__text = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id
    
    @property
    def foreground_color (self): return self.__foreground_color

    @foreground_color.setter
    def foreground_color (self, value):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        self.__foreground_color = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id