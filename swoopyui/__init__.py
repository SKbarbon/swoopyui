from .tools.check_if_mac import is_device_a_mac
if not is_device_a_mac():
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