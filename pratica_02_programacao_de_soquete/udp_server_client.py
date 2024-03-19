import socket

UDP_IP = "172.16.127.39"
UDP_PORT = 5005
MESSAGE = b"estou enviando uma mensagem"
 
print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
print(type(MESSAGE))

# msg_bytes = MESSAGE.encode("utf-8")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
msg, client = sock.recvfrom(5005)
print('Mensagem retornada: ', msg)
print('Client: ', client)
