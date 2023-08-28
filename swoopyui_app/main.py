from swoopyui import NavigationSplitView, Button
import swoopyui, time, random


def main (view:swoopyui.View):
    def on_p (cls):
        the_number.content = str(int(the_number.content)+1)
        the_number.update()
    
    def on_m (cls):
        the_number.content = str(int(the_number.content)-1)
        the_number.update()
    
    nav = NavigationSplitView("Demo")
    view.add(nav)

    hs = swoopyui.HStack()
    nav.add([hs])

    the_number = swoopyui.TextField("", content="1", resizeable=True)
    hs.add([
        swoopyui.ElevatedButton("+", color="white", bgcolor="black", width=40, height=40, on_click=on_p),
        the_number,
        swoopyui.ElevatedButton("-", color="white", bgcolor="black", width=40, height=40, on_click=on_m)
    ])