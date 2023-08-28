from .subview import SubView




class Label (SubView):
    """
    A standard label for user interface items, consisting of an icon with a title.
    
    You can browse all the available icons on:
    [Apple SF symbols](https://developer.apple.com/sf-symbols/)
    """
    def __init__(self, content:str="Hello, label!", icon_name:str="globe.europe.africa", color:str="primery", icon_color:str="primery", size:int=18, icon_size:int=18) -> None:
        super().__init__()

        self.content : str = content
        self.icon_name : str = icon_name
        self.color : str = color
        self.icon_color : str = icon_color
        self.size : int = size
        self.icon_size : int = icon_size

        self.vdata.update({
            "name" : "TheLabelView",
            "props" : {
                "content" : self.content,
                "icon_name" : self.icon_name,
                "color" : self.color,
                "icon_color" : self.icon_color,
                "size" : self.size,
                "icon_size" : self.icon_size
            }
        })
    
    def update(self):
        self.vdata.update({
            "name" : "TheLabelView",
            "props" : {
                "content" : self.content,
                "icon_name" : self.icon_name,
                "color" : self.color,
                "icon_color" : self.icon_color,
                "size" : self.size,
                "icon_size" : self.icon_size
            }
        })
        return super().update()