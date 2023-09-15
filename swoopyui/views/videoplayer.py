from .subview import SubView



class VideoPlayer (SubView):
    """A view that displays content from a player and a native user interface to control playback."""
    def __init__(self, link:str, width:int=250, height:int=250) -> None:
        super().__init__()

        self.link : str = link
        self.width : int = width
        self.height : int = height

        self.vdata.update({
            "name" : "AV_VideoPlayer",
            "props" : {
                "link" : link,
                "width" : self.width,
                "height" : self.height
            }
        })
    

    def play (self):
        """Begins playback of the current video."""
        if self.main_view != None:
            self.main_view.subview_reverse_event({
                "action" : "change_video_state",
                "new_video_state" : "play",
                "parent_id" : self.id
            })
    
    
    def puase (self):
        """Pauses playback of the current video."""
        if self.main_view != None:
            self.main_view.subview_reverse_event({
                "action" : "change_video_state",
                "new_video_state" : "puase",
                "parent_id" : self.id
            })
    

    def change_video_link (self, new_link:str, same_position:bool):
        """Replace and change the current video link with a new one without pushing a new subview update.
        
        This is usefull when you just want to replace the video with an edited version, or for example when you just want to change a
        high-quality video link with a low-quality video link.

        the `same_position` arguments make the video replace the link, then continue playing the video from the same last duration position.
        """
        self.link = str(new_link)
        self.vdata['props']['link'] = str(new_link)
        if self.main_view != None:
            self.main_view.subview_reverse_event({
                "action" : "change_video_link",
                "new_link" : str(new_link),
                "same_position" : bool(same_position),
                "parent_id" : self.id
            })
    
    def change_videoplayer_bounds (self, width:int, height:int):
        """Change the video player width and height without pushing a new update 
        event for this subview"""
        self.width = int(width)
        self.height = int(height)
        self.vdata['props'].update({
            "width" : int(width),
            "height" : int(height)
        })
        if self.main_view != None:
            self.main_view.subview_reverse_event({
                "action" : "resize",
                "width" : int(width),
                "height" : int(height),
                "parent_id" : self.id
            })