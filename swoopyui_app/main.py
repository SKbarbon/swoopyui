import swoopyui

def main (view:swoopyui.View):
    vid_link = view.create_asset_link("vv.mp4")

    vp = swoopyui.VideoPlayer(link=vid_link)
    view.add(vp)


swoopyui.app(target=main, base_name=__name__)