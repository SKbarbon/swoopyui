"""
swoopyui is a python library that allow you to build swoopyui applications in python only!

Visit the github page:
[swoopyui github](https://github.com/SKbarbon/swoopyui)
"""
from .tools.check_platform import is_device_a_ios, is_device_a_mac
if is_device_a_mac() or is_device_a_ios():
    pass
else:
    print("WARNING: This platform is not supported for the development.")
    # raise Exception ("Your device is not a mac. So cannot use this library.")

from .swoopyui import app

from .view import View

from .views.text import Text
from .views.vstack import VStack
from .views.hstack import HStack
from .views.navigationsplitview import NavigationSplitView
from .views.button import Button
from .views.navigationlink import NavigationLink
from .views.textfield import TextField
from .views.scrollview import ScrollView, ScrollModeHorizontal, ScrollModeVertical
from .views.colorview import ColorView
from .views.spacer import Spacer
from .views.list import List
from .views.sheet import Sheet
from .views.elevatedbutton import ElevatedButton
from .views.textbutton import TextButton
from .views.label import Label
from .views.icon import Icon
from .views.contextmenu import ContextMenu
from .views.labeledbutton import LabeledButton
from .views.menu import Menu
from .views.scrollingtabview import ScrollingTabView
from .views.navigationstack import NavigationStack
from .views.videoplayer import VideoPlayer
from .views.geometryreader import GeometryReader
from .views.zstack import ZStack
# from .views.image import Image
# from .views.webview import WebView
# from .views.animatedview import AnimatedView

# shapes views
from .views.shapes.roundedrectangleshape import RoundedRectangleShape
