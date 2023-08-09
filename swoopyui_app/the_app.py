import swoopyui


def app (view:swoopyui.View):
    def on_clicked (cls):
        operation = str(cls.text)
        if operation == "+": number.text = str(int(number.text) + 1)
        elif operation == "-": number.text = str(int(number.text) - 1)
        hstack.update()
    
    hstack = swoopyui.Stack(swoopyui.HSTACK)
    view.add(hstack)

    number = swoopyui.TextField("1")
    hstack.add(swoopyui.Button("+", on_click=on_clicked, width=30, height=30))
    hstack.add(number)
    hstack.add(swoopyui.Button("-", on_click=on_clicked, width=30, height=30))
    hstack.update()