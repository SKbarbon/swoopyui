class View:
    def __init__(self, app):
        self._app = app
        self._next_id = 0  # The next view ID.
        self.sub_views_history = []  # This will store all sub_views, even from the other subviews.
        self.sub_views = []

    def update(self, sub_view=None):
        if sub_view is not None:
            action_content = {"new_view_content": sub_view.get_dict_content()}
            self._app.set_for_the_next_update_get(action_name="update_view", action_content=action_content)

    def add(self, view):
        view.respown(new_id=self.get_new_view_id(), mother_view=self, parent=self)
        action_content = {"new_view_content": view.get_dict_content()}
        self._app.set_for_the_next_update_get(action_name="add_view", action_content=action_content)
        self.sub_views_history.append(view)
        self.sub_views.append(view)

    def clear(self):
        for sub_view in self.sub_views:
            action_content = {"view_id": sub_view.id}
            self._app.set_for_the_next_update_get(action_name="delete_view", action_content=action_content)

    def delete(self, view):
        """Delete a sub-view from the view."""
        action_content = {"view_id": view.id}
        self._app.set_for_the_next_update_get(action_name="delete_view", action_content=action_content)

        for i, v in enumerate(self.sub_views_history):
            if v.id == view.id:
                del self.sub_views_history[i]
                break

    def get_new_view_id(self):
        """Generate a new view ID for the current and next view."""
        self._next_id += 1
        current = self._next_id
        self._next_id += 1
        return current

    def manage_on_view_action(self, action_content: dict):
        view_id = action_content['view_id']
        for view in self.sub_views_history:
            if view.id == view_id:
                view.view_action(action_content)
                break
