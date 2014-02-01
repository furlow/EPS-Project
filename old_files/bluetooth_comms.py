from bluetooth import *

port = 5
backlog = 1

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",port))
server_sock.listen(backlog)

uuid = "df0677bc-5f0b-45e4-8207-122adee18805"

try:
	advertise_service( server_sock, "alarm",
   		service_id = uuid,
		service_classes = [ uuid, SERIAL_PORT_CLASS],
		profiles = [SERIAL_PORT_PROFILE])

	print "waiting for connection..."
	client_sock, client_info = server_sock.accept()
	print "Accepted connection from ", client_info

	print "waiting for data..."
	data = client_sock.recv(1024)
	print "received", data
	client_sock.send ("data sent")

except keyboardInterrupt:
	stop_advertising (server_sock)	
	client_sock.close()
	server_sock.close()
