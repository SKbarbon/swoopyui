from swoopyui import app, View, ScrollView
import swoopyui
import time
import sys

print(sys.platform)


def main (view:View):
    s = ScrollView (scroll_mode="v")
    view.add(s)

    vs = swoopyui.Stack(stack_type=swoopyui.VSTACK)
    s.add(vs); s.update()

    for i in range (150):
        vs.add(swoopyui.Text(f"{i}"))
    
    vs.update()


swoopyui.app(target=main)