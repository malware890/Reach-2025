#BASIC SERVER CODE
# import os
# import socket
# from twisted.cred.checkers import AllowAnonymousAccess
# from twisted.cred.portal import Portal
# from twisted.internet import reactor
# from twisted.protocols.ftp import FTPFactory, FTPRealm

# def run_ftp():
#     public_dir = os.path.abspath("./public")
#     print(f"Serving files from: {public_dir}")

#     portal = Portal(FTPRealm(public_dir), [AllowAnonymousAccess()])
#     factory = FTPFactory(portal)

#     reactor.listenTCP(2121, factory)
#     print(f"Server running at {socket.gethostbyname(socket.gethostname())}:2121")
#     reactor.run()

# run_ftp()

import os
import socket
from twisted.cred.checkers import AllowAnonymousAccess
from twisted.cred.portal import Portal
from twisted.internet import reactor
from twisted.protocols.ftp import FTPFactory, FTPRealm


class CustomFTPRealm(FTPRealm):
    def __init__(self, root):
        super().__init__(root)
        self.active_connections = 0

    def anonymousUserHome(self, avatarId):
        self.active_connections += 1
        print(f"Client connected. Active connections: {self.active_connections}")
        return super().anonymousUserHome(avatarId)


class CustomFTPFactory(FTPFactory):
    def __init__(self, portal):
        super().__init__(portal)

    def buildProtocol(self, addr):
        protocol = super().buildProtocol(addr)

        original_connectionMade = protocol.connectionMade
        original_connectionLost = protocol.connectionLost

        def custom_connectionMade():
            original_connectionMade()
            print(f"Connection made from: {addr.host}")

        def custom_connectionLost(reason):
            original_connectionLost(reason)
            realm = self.portal.realm
            if realm.active_connections > 0:
                realm.active_connections -= 1
                print(f"Active connections: {realm.active_connections}")
            else:
                print("Active connections was 0.")
            if realm.active_connections == 0:
                print("No active connections. Shutting down the server...")
                reactor.stop()

        protocol.connectionMade = custom_connectionMade
        protocol.connectionLost = custom_connectionLost
        return protocol


def run_ftp():
    public_dir = os.path.abspath("./public")
    print(f"Serving files from: {public_dir}")

    portal = Portal(CustomFTPRealm(public_dir), [AllowAnonymousAccess()])
    factory = CustomFTPFactory(portal)

    reactor.listenTCP(2121, factory)
    print(f"FTP Server running at {socket.gethostbyname(socket.gethostname())}:2121")
    reactor.run()

run_ftp()