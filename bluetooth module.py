# thread_bluetooth_comms.py
import threading
import time
import bluetooth from *


# THIS ISNT COMPLETED YET... THIS IS THE BIT I DONT UNDERSTAND SOZ

class thread_bluetooth_comms(threading.Thread):
    def bluetooth_comms():
            
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
                    
    #		client_sock, client_info = server_sock.accept()
    #		print "Accepted connection from ", client_info

                    print "waiting for data..."
                    
    #		data = client_sock.recv(1024)

                    data = "1910;1912;1;0";
                    current_time = data[0:4];
                    alarm_time = data[5:9];
                    alarm = data[10];
                    light = data[12];
    #		client_sock.send ("data sent")
                    List = [int(current_time),int(alarm_time),int(alarm),int(light)]
                    
                    print List
                    
            except keyboardInterrupt:
                    
                    stop_advertising (server_sock)        
                    client_sock.close()
                    server_sock.close()
                    
            return List
