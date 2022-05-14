
import sessionRa

import socket
import time
import cryptocode


#generando Encabezado de Servidor
mensaje =  sessionRa.encabezadoServer()

#enviando peticion Socket Remota
sock = sessionRa.petition(mensaje,"stun2.l.google.com",19302)

#Generando identificador de sesión
sessionSocket = sessionRa.createSession()


#Esperando descripción de red remota
DescripcionRemota = input("IpRemote:")

#Decodificando descripción remota de mi amigo
ipRemoteDecode =  sessionRa.sessionFriendDecode(DescripcionRemota)


#Imprimiendo descripción remota
print(ipRemoteDecode)

#Trasladamos socket a una conexión independiente con la descripción de red
sock =  sessionRa.conexion(ipRemoteDecode,sock)




def decodeFriend(data):
    #decodificamos lo bytes recibidos en una lista
    listaIn =  list(data)
    print(listaIn)


# loop
while True:    

    #aquí podemos enviar datos a mi amigo
    sock.send(bytearray(sessionSocket))

    #aquí recibimos los datos de mi amigo
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

    #un ejemplo de decodificación de datos recibidos
    decodeFriend(data)

    #tiempo de retardo cada ciclo
    time.sleep(1)
    






