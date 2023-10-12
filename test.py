import swoopyui, threading, time

def main (view:swoopyui.View):
    def cl (cls:swoopyui.TextButton):
        print("clicked!")
        lis.add([swoopyui.Text("HAHA")])
        cls.content = "clicked."
        cls.update()
    
    lis = swoopyui.List()
    view.add(lis)
    lis.add([swoopyui.TextButton("CLick me!", on_click=cl)])

swoopyui.app(target=main, view=swoopyui.AppMode.MenuBarExtra)