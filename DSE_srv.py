import Srv

HOST = "192.168.44.22"  # Standard loopback interface address (localhost)
PORT = 20003  # Port to listen on (non-privileged ports are > 1023)

# https://temofeev.ru/info/articles/rukovodstvo-po-programmirovaniyu-soketov-na-python-klient-server-i-neskolko-soedineniy/
Srv.run(HOST, PORT)
quit()
