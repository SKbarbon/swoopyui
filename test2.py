import swoopyui



def main (view:swoopyui.View):
    ic = swoopyui.Icon()
    view.add(ic)

swoopyui.app(target=main, debug=True)