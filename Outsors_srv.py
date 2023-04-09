import Srv

HOST = "192.168.44.22"  # Standard loopback interface address (localhost)
PORT = 20004  # Port to listen on (non-privileged ports are > 1023)

Srv.run(HOST, PORT)
