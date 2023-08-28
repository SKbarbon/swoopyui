import socketserver


def get_free_port () -> int:
    with socketserver.TCPServer(("localhost", 0), None) as s:
        free_port = s.server_address[1]
    
    return free_port