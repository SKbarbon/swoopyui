from ..tools.on_action import on_view_action


class NavigationLink:
    """A view that controls a navigation presentation."""
    def __init__(self, title="Navigate", on_navigate=None):
        self._last_view_id = None  # This is used because SwiftUI will not know that this updated without it
        self._id = None
        self._mother_view = None
        self._parent_view = None

        self.on_navigate = on_navigate
        self._title = title
        self._subviews = []
    
    def get_dict_content(self):
        all_sub_views = [sv.get_dict_content() for sv in self._subviews]
        return {
            "last_view_id": self._last_view_id,
            "view_id": self._id,
            "vname": "NavigationLink",
            "title": self._title,
            "sub_views": all_sub_views
        }
    
    def respown(self, new_id=None, mother_view=None, parent=None):
        if new_id is None or mother_view is None or parent is None:
            return

        if self._id is None:
            self._id = new_id
            self._last_view_id = new_id
        
        if self._mother_view is None:
            self._mother_view = mother_view
        
        if self._parent_view is None:
            self._parent_view = parent
    
    def add(self, *sub_views):
        if self._mother_view is None:
            raise Exception("Cannot add sub-views while this view does not have an active mother view.")
        
        for sub_view in sub_views:
            sub_view.respown(new_id=self._mother_view.get_new_view_id(), mother_view=self._mother_view, parent=self)
            self._mother_view.sub_views_history.append(sub_view)
            self._subviews.append(sub_view)

        self._id = self._mother_view.get_new_view_id()
        self._mother_view.update(self)
        self._last_view_id = self._id
    
    def view_action(self, action_data):
        action_name = action_data["action_name"]
        if action_name == "on_navigate":
            on_view_action(self.on_navigate, [self])
    
    def update(self):
        self._id = self._mother_view.get_new_view_id()
        self._mother_view.update(self)
        self._last_view_id = self._id
        self._parent_view.update()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if self._mother_view is None:
            raise Exception("Cannot change the sub_view property while it's not on the screen.")
        
        self._title = value
        self._id = self._mother_view.get_new_view_id()
        self._mother_view.update(self)
        self._last_view_id = self._id
