import threading
from time import sleep
from bluetooth import *

class bluetooth_comms(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)

        self.data = data
        
        port = 5
        backlog = 1
            
        self.server_sock=BluetoothSocket( RFCOMM )
        self.server_sock.bind(("",port))
        self.server_sock.listen(backlog)

	self.client_sock = BluetoothSocket( RFCOMM)

        uuid = "df0677bc-5f0b-45e4-8207-122adee18805"
        
        advertise_service( self.server_sock, "alarm",
                            service_id = uuid,
                            service_classes = [ uuid, SERIAL_PORT_CLASS],
                            profiles = [SERIAL_PORT_PROFILE])

    def run(self):

	try:
        

		while(True):

			print "waiting for connection..."
            		self.client_sock, client_info = self.server_sock.accept()
			
			print "Accepted connection from ", client_info
            		print "waiting for data..."
            		raw_data = self.client_sock.recv(1024)

            		self.data[0] = int(raw_data[0:4])
            		self.data[1] = int(raw_data[5:9])
            		self.data[2] = int(raw_data[10])
                        self.data[3]= int(raw_data[12])
            		self.client_sock.send ("data sent")
            		print self.data
			self.client_sock.close()

	except KeyboardInterrupt:
		self.stop()

    def stop(self):
	self.keepalive = False
        stop_advertising (self.server_sock)
	self.client_sock.close()
        self.server_sock.close()
