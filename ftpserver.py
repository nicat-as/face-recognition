from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket

FTP_PORT = 2121
FTP_USER = 'nicat'
FTP_PASS = 'access2ftp'
FTP_DIR = 'image/'

def main():
    s= socket.gethostbyname(socket.gethostname())
    print(s)
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASS, FTP_DIR, perm = 'elradfmw')
    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = 'server is ready'
    address = (s, FTP_PORT)
    server = FTPServer(address, handler)
    server.serve_forever()

if __name__ == '__main__':
    main()