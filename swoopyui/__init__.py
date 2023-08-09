from .tools.check_platform import is_device_a_ios, is_device_a_mac
if is_device_a_mac() or is_device_a_ios():
    pass
else:
    raise Exception ("Your device is not a mac. So cannot use this library.")

from .swoopyui import app

from .view import View

from .views.text import Text
from .views.button import Button
from .views.navigationview import NavigationView
from .views.navigationstack import NavigationStack
from .views.navigationlink import NavigationLink
from .views.textfield import TextField
from .views.stack import Stack, VSTACK, HSTACK, ZSTACK
from .views.scrollview import ScrollView
from .views.spacer import Spacer
from .views.list import List
from .views.image import Image
from .views.webview import WebView
from .views.animatedview import AnimatedView
from .views.icon import Icon
from .views.navigationsplitview import NavigationSplitView

from .views.shapes.circle import Circle