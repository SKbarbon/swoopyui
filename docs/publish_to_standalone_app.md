# Publish into standalone application

## Platforms
### MacOS
Soon.

### iOS, iPadOS, macOS (Designed for iPad) and VisionOS (Designed for iPad).
You can publish your swoopyui project into a standalone iOS, iPadOS, macOS(Designed for iPad) and VisionOS (Designed for iPad) platforms. One way to do this is by using the [xcode swoopyui iOS template](https://github.com/swoopyui/SwoopyuiTemplate-iOS).

**Usage**
1. Create python venv (important!).

First, start with creating a python Virtual Environment becuase we will use it later!. You can use this command to create one:
```zsh
python -m venv venv
```

activate the venv:
mac, linux:
```zsh
source /path/to/venv/bin/activate
```
window:
```shell
\path\to\venv\Scripts\activate.bat
```

2. Install `swoopyui` library.

Install the `swoopyui` library inside the `venv`. You can use this command for that:
```zsh
pip install swoopyui --upgrade
```

3. Open `xcode`, then clone the template.

Open `xcode`, then in the splash window (The one that show xcode icon), click on `Clone Git Repository..` Button, then paste `https://github.com/swoopyui/SwoopyuiTemplate-iOS` in the text field.


4. In the xcode editor window, focus on the left inspector.

In the xcode editor window, Specifically in the left inspector, focus on the `Package Dependencies` section, then exand the `Python-iOS` package. Open these folder to reach the the `site-packages` folder, to reach it follow this path: `Sources/PythonSupport/lib/python3.9/site-packages`, then right-click on it and click the menu element `Show in Finder`. Then a finder window will opens.

<img width="1728" alt="Screenshot 2023-08-29 at 4 46 45 PM" src="https://github.com/SKbarbon/swoopyui/assets/86029286/2bd75232-886a-4877-9aac-b62fdc50c970">

5. Go to python venv, and copy all `site-package` content.

Go to the python venv you created, then open the `site-package` folder, you can reach it at path: `venv/lib/python3.x/site-packages/`. Copy all the content, then go to the folder you just open from xcode, paste everything there.

6. Clear the dirt.

Now search on the content you just pasted for any files that ends with format `.so`, you can do this by searching in finder by entering `so` in the search feild. Delete any file that have this format and not matching `_sqlite3.cpython-39-darwin.so`.

7. Create your app folder.

In where you pasted everything, create a new folder named `swoopyui_app`. Then here put all of your scripts. Your app will be called as a module, so make sure you run your app from the `__init__.py` file of your `swoopyui_app`.

8. Now run your app!.

Finally, you can run your iOS application. Everything must work. If you have any issues at running your app, please make an [issue](https://github.com/SKbarbon/swoopyui/issues) and we will help ya.