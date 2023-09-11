# Simple `swoopyui` app example.
In `swoopyui`, everything is simple. The app starts with an entry point we call it `target`. The target is a function that build the base of the app. 

This is a simple `hello, world` app: 

```python
from swoopyui import View, Text
import swoopyui

def main (view:View):
    view.add(Text("Hello, world!"))

swoopyui.app(target=main)
```


A target function named `main`. The target function creating a `Text` view that say `Hello, world!`.

Then finaly there is the `app` class, that takes the target function as an argument to call it as an entry point.