import swoopyui

def main (view:swoopyui.View):
    view.add(swoopyui.Text("Hello!"))

swoopyui.app(target=main, view=swoopyui.AppMode.App)