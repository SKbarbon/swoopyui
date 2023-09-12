from .views.subview import SubView
from .protocol import onAddNewSubViewRequest, onUpdateSubviewProps


class View (object):
    def __init__(self, host_port, host_app_class) -> None:
        self.__host_app_class = host_app_class
        self.host_port = host_port

        self.platform = None #? The platform that running swiftUI.
        self.theme_mode = None #? The theme mode of the app, like light mode or dark mode.

        self.__subviews_history = [] #? All the subviews that have been added directly or not directly on currently connected swiftUI app.
        self.__last_id = 0
        self.__last_update_id = 0
        
        self.subviews = []
    
    def add (self, subview:SubView):
        """Add a new subview to the main view."""
        subview.respown(
            new_id=self.get_new_subview_id(),
            update_id=self.get_new_subview_update_id(),
            parent_view=self,
            main_view=self
        )
        self.subviews.append(subview)
        self.__subviews_history.append(subview)
        
        self.__add_to_next_update_requests(onAddNewSubViewRequest(subview=subview).raw)
        subview.update()
    
    def remove (self, subview:SubView):
        """Remove a subview from the swiftUI app."""
    
    def get_subview_by_id (self, subview_id:int):
        """This function will search for the subviewID in the subviews history.
        
        If there is no result it will return `None`.
        """
        for sbv in self.__subviews_history:
            if sbv.id == subview_id:
                return sbv
        return None
    

    def get_new_subview_id (self):
        self.__last_id = self.__last_id + 1
        return self.__last_id
    
    def get_new_subview_update_id (self):
        self.__last_update_id = self.__last_update_id + 1
        return self.__last_update_id

    
    def update (self, subview:SubView=None):
        if subview == None:
            pass
        else:
            subview.update_id = self.get_new_subview_update_id()
            subview.vdata['update_id'] = subview.update_id
            self.__add_to_next_update_requests(update_dict=onUpdateSubviewProps(subview=subview).raw)
    

    def add_to_subviews_history (self, subv:SubView):
        self.__subviews_history.append(subv)
    
    
    def process_client_events (self, event_dict:dict):
        if event_dict['action'] == "view_event":
            subview_id = int(event_dict['view_id'])
            subview_class = None
            for sbv in self.__subviews_history:
                sbv : SubView = sbv
                if int(sbv.id) == int(subview_id):
                    subview_class = sbv
                    break
            subview_class.on_event(event_dict['event_content'])
        
        elif event_dict['action'] == "startup_app_info":
            self.platform = event_dict['content']['platform']


    def subview_reverse_event (self, update_dict):
        """It when the subview request an event from the python side into the swift side."""
        self.__add_to_next_update_requests(update_dict=update_dict)


    def __add_to_next_update_requests(self, update_dict):
        """Add an update request to the client."""
        # print(update_dict)
        self.__host_app_class.next_get_updates_responses.append(update_dict)
    

    @property
    def next_updates (self):
        return self.__next_updates