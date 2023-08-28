



class SubView (object):
    """The parent class of all subview's subclassess."""
    def __init__(self) -> None:
        self.__id = -1
        self.__parent_view = None
        self.__main_view = None

        self.update_id = -1

        self.vdata = {
            "ID" : self.__id,
            "update_id" : self.update_id,
            "name" : "None",
            "props" : {},
            "sub_views" : []
        }

    
    def respown (self, new_id:int, update_id:int, parent_view, main_view):
        self.__id = new_id
        self.update_id = update_id
        self.__parent_view = parent_view
        self.__main_view = main_view

        self.vdata['ID'] = new_id
        self.vdata['update_id'] = update_id
    
    def update (self):
        if self.parent_view == None or self.main_view == None:
            raise Exception("You must add this subview to the UI first.")
        self.vdata['ID'] = self.__id
        self.vdata['update_id'] = self.update_id

        self.main_view.update(self)


    @property
    def id (self):
        return self.__id
    
    @property
    def parent_view (self):
        return self.__parent_view
    
    @property
    def main_view(self):
        return self.__main_view