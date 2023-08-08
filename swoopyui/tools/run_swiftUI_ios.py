import os, tempfile



def prepare_swiftUI_for_ios (port):
    documents_dir_path = os.path.expanduser('~/Documents')
    
    if not os.path.isdir(os.path.join(documents_dir_path, "swoopyui_temp")):
        os.mkdir(os.path.join(documents_dir_path, "swoopyui_temp"))
    
    swoopyui_connect_file_path = os.path.join(documents_dir_path, "swoopyui_temp", "swoopyui_connect.txt")
    open(swoopyui_connect_file_path, "w+", encoding="utf-8").write(f"{port}")