#modules communication réseau
import socket #pour connecter, envoyer et recevoir de la data
import select #gérer les connexions

serveur = socket.socket() #créa serveur, on instancie socket
host, port = "127.0.0.1", 5000 #assigne valeur pour host et port
serveur.bind((host, port)) #liage du host + port
serveur.listen(4) #prendre l'info avec 4 user max
client_connected = True #var + true, en attente d'un user
socket_objj = [serveur] #contenant du socket

print("En attente de connexion utilisateur...")

while client_connected: #ma boucle qui tourne en attente de connexion user, stop seulement si client_connected = False

    liste_lu, liste_accesrite, exception = select.select(socket_objj, [], socket_objj)

    for socket_obj in liste_lu: #parcours chaque sockets en lecture

        if socket_obj is serveur: #si le socket est du serv alors accept
            client, adresse = serveur.accept()
            socket_objj.append(client) #ajout à mon objet

        else: #si non
            data_recu = socket_obj.recv(128).decode("utf-8")

            if data_recu:
                print(data_recu)
