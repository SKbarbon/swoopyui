from .subview import SubView



class ColorView (SubView):
    def __init__(self, corner_radius:int=5, color:str="primery", width:int=100, height:int=100) -> None:
        super().__init__()

        self.corner_radius : int = corner_radius
        self.color : str = color
        self.width : int = width
        self.height : int = height
        
        self.vdata.update({
            "name" : " ColorView",
            "props" : {
                "corner_radius" : self.corner_radius,
                "color" : color,
                "width" : width,
                "height" : height
            }
        })
    

    def update(self):
        self.vdata.update({
            "name" : " ColorView",
            "props" : {
                "corner_radius" : self.corner_radius,
                "color" : self.color,
                "width" : self.width,
                "height" : self.height
            }
        })
        return super().update()