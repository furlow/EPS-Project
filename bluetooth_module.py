import threading
from time import sleep
from bluetooth import *

class bluetooth_comms(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)

        self.data = data
        self.keepalive = True
        
        port = 5
        backlog = 1
            
       # self.server_sock=BluetoothSocket( RFCOMM )
       # self.server_sock.bind(("",port))
       # self.server_sock.listen(backlog)

       # uuid = "df0677bc-5f0b-45e4-8207-122adee18805"
        
       # advertise_service( self.server_sock, "alarm",
       #                     service_id = uuid,
       #                     service_classes = [ uuid, SERIAL_PORT_CLASS],
       #                     profiles = [SERIAL_PORT_PROFILE])

    def run(self):

        while(self.keepalive):

            print "waiting for connection..."
            sleep(2)
           # client_sock, client_info = self.server_sock.accept()
            print "Accepted connection from "#, client_info
            sleep(2)
            print "waiting for data..."
           # raw_data = client_sock.recv(1024)

            raw_data = "1910;1912;1;0";
            current_time = raw_data[0:4];
            alarm_time = raw_data[5:9];
            alarm = raw_data[10];
            light = raw_data[12];
            self.data[2] = 1 #all the above lines need to be changed to this format
            #client_sock.send ("data sent")
            #self.data = [int(current_time),int(alarm_time),int(alarm),int(light)]
            print self.data

        #stop_advertising (self.server_sock)
        #client_sock.close()
        #self.server_sock.close()

    #def stop(self):
    #    
    #    self.keepalive = False

