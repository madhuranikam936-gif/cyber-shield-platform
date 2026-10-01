import socket

def get_open_ports():
    ports = []

    for port in [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)

        try:
            s.connect(("127.0.0.1", port))
            ports.append(port)
        except:
            pass

        s.close()

    return ports