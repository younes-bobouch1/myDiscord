#lorsqu'il y'a connexion au chat, ce fichier est execute

import socket

client_socket = socket.socket()
host, port = "127.0.0.1", 5000 #assigne valeur pour host et port (identique au réseau)
client_socket.connect((host, port)) #connexion au serveur
pseudo = input("Quel est votre pseudo ?")

if __name__ == "__main__":

    while True:

        msg = input(f"{pseudo} > ")
        client_socket.send(f"{pseudo} > {msg}".encode("utf-8"))