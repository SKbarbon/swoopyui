# swoopyui preview
swoopyui provides a magical way to test your swoopyui project UI in your iOS, iPadOS, macOS and even visionOS by the feature named 'preview', simple hah :) ?

swoopyui preview feature allow you to instantly preview UI in the `swoopyui` app, its availble in the App Store:

<!-- [swoopyui in App Store]() -->
[swoopyui on TestFlight](https://testflight.apple.com/join/DwKcRV2p)

## How to start using the preview feature ?
1. Start by building your python swoopyui app, then append `for_preview=True` argument to the `app` class in the end. For example:

```python
import swoopyui

def main (view:swoopyui.View):
    view.add(swoopyui.Text("Hi, preview!"))

swoopyui.app(target=main, for_preview=True)
```

Then there will be a `flask` host log, with two host URLs. Pick the second URL

2. Install [swoopyui]() if you did not, then open it. Click on the `preview` tab page.

3. In the text field, enter the URL of the host, then click `Connect`. It will start the preview then. To cancle it, click `Stop preview` button.