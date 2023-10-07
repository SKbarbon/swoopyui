import swoopyui, time


def main (view:swoopyui.View):
    def on_resize (cls:swoopyui.GeometryReader):
        vp.change_videoplayer_bounds(width=cls.width, height=cls.height)

    gm = swoopyui.GeometryReader(on_resize=on_resize)
    view.add(gm)

    vp = swoopyui.VideoPlayer(link="http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
    gm.add([vp])

    time.sleep(0.5)
    if gm.width != None:
        vp.change_videoplayer_bounds(gm.width, gm.height)

swoopyui.app(target=main)