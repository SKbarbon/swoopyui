



def is_run_on_pyinstaller ():
    import sys

    if getattr(sys, 'frozen', False):
        # Running from a PyInstaller executable
        return True
    else:
        # Running the script directly
        return False