from .subview import SubView



class Text (SubView):
    def __init__ (self, content:str, color:str="primery",  size:int=18):
        super().__init__()

        self.content : str = content
        self.color : str = color
        self.size : str = size

        self.vdata.update({
            "name" : "Text",
            "props" : {
                "content" : self.content,
                "color" : self.color,
                "size" : self.size
            }
        })

    
    def update (self):
        self.vdata.update({
            "name" : "Text",
            "props" : {
                "content" : self.content,
                "color" : self.color,
                "size" : self.size
            }
        })
        super().update()