from .subviewparent import SubViewParent



class Menu (SubViewParent):
    """A control for presenting a menu of actions."""
    def __init__(self, title:str="") -> None:
        super().__init__()


        self.title : str = title

        self.vdata.update({
            "name" : "Menu",
            "props" : {
                "title" : self.title
            }
        })
    
    def update(self):
        self.vdata.update({
            "name" : "Menu",
            "props" : {
                "title" : self.title
            }
        })
        return super().update()