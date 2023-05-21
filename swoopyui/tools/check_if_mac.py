import sys



def is_device_a_mac ():
    if "darwin" in str(sys.platform):
        return True
    else:
        return False