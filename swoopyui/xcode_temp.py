import sys, zipfile, os, shutil


#! Get the args
terminal_args = sys.argv


#! Unzip the xcode template
mother_path_swoopyui = os.path.dirname(str(__file__))
assets_path = os.path.join(mother_path_swoopyui, "assets")

zip_file_path = os.path.join(assets_path, 'swoopyui_xcode_ios.zip')
extract_folder = '.'

# Open the ZIP file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all contents to the specified folder
    zip_ref.extractall(extract_folder)


# from_path= os.path.join("__MACOSX", "swoopyui_xcode_ios")
# shutil.copytree(from_path, "./swoopyui_xcode_ios2")
if os.path.isdir ("__MACOSX"):
    shutil.rmtree("__MACOSX")
