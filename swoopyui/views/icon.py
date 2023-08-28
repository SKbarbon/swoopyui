from .subview import SubView




class Icon (SubView):
    """
    A standard label for user interface items, consisting of an icon with a title.
    
    You can browse all the available icons on:
    [Apple SF symbols](https://developer.apple.com/sf-symbols/)
    """
    def __init__(self, icon_name:str="globe.europe.africa", icon_color:str="primery", icon_size:int=18) -> None:
        super().__init__()

        self.icon_name : str = icon_name
        self.icon_color : str = icon_color
        self.icon_size : int = icon_size

        self.vdata.update({
            "name" : "Icon",
            "props" : {
                "icon_name" : self.icon_name,
                "icon_color" : self.icon_color,
                "icon_size" : self.icon_size
            }
        })
    
    def update(self):
        self.vdata.update({
            "name" : "Icon",
            "props" : {
                "icon_name" : self.icon_name,
                "icon_color" : self.icon_color,
                "icon_size" : self.icon_size
            }
        })
        return super().update()