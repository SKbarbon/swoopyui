from swoopyui import app, View, Stack
import swoopyui
import time


def main (view:View):
    s = Stack(stack_type=swoopyui.VSTACK)
    view.add(s)

    for i in range (20):
        s.add(swoopyui.Text(f"{i}", size=14, bold=True))
    
    s.update()


swoopyui.app(target=main)