from typing import Literal
from ..tools.on_action import on_view_action


VSTACK = 'v'
HSTACK = 'h'
ZSTACK = 'z'

StackType = Literal['v', 'h', 'z']

class Stack (object):
    """A view that arranges its subviews in a vertical/horizontal line or overlay and align them in same axes."""
    def __init__(self, stack_type:StackType=VSTACK, on_appear=None) -> None:
        self.__last_view_id = None # This is used becuase swiftUI will not know that this updated without it
        self.__id = None
        self.__mother_view = None
        self.__parent_view = None

        self.__stack_type = stack_type
        self.__subviews = []
        self.on_appear = on_appear
    
    def get_dict_content (self):
        all_sub_views = []
        for sv in self.__subviews:
            all_sub_views.append(sv.get_dict_content())
        return {
            "last_view_id" : self.__last_view_id,
            "view_id" : self.__id,
            "vname" : "Stack",
            "stack_type" : self.__stack_type,
            "sub_views" : all_sub_views
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
    

    def add (self, *sub_view):
        """Add a new subview to be inside this StackView."""
        if self.__mother_view == None:
            raise Exception("Cannot add sub-views while this view not have an active mother view.")
        
        for subv in sub_view:
            subv.respown (new_id=self.__mother_view.get_new_view_id(), mother_view=self.__mother_view, parent=self)
            self.__mother_view.sub_views_history.append(subv)
            self.__subviews.append(subv)
    

    def update (self):
        """Update the StackView, You mostly wont use it, except after `.add` function."""
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id

        self.__parent_view.update()
    
    def view_action (self, action_data):
        action_name = action_data['action_name']
        if action_name == "on_appear":
            on_view_action(self.on_appear, [self])
        
    
    @property
    def id (self):
        return self.__id
    
    @property
    def stack_type (self):
        return self.__stack_type
    
    @stack_type.setter
    def stack_type (self, value:StackType):
        if self.__mother_view == None:
            raise Exception("Cannot change the sub_view property while its not on the screen.")
        
        if str(value).lower() not in ["v", "h", "z"]:
            raise ValueError (f"stack_type must be a 'VSTACK', 'HSTACK' or 'ZStack'. But you did pass a {value}:{type(value)}.")

        self.__stack_type = value
        self.__id = self.__mother_view.get_new_view_id()
        self.__mother_view.update(self)
        self.__last_view_id = self.__id