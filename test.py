import swoopyui


def main (view:swoopyui.View):
    view.add(swoopyui.Text("Hello, world!"))

swoopyui.app(target=main)