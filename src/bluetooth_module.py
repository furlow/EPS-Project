import threading
from bluetooth import *


# *** bluetooth_comms ***
# This class deals with the bluetooth communications with the phone application
# it inherits from the threading.Thread class this allows it to be run along
# side other threads.
class bluetooth_comms(threading.Thread):
    def __init__(self, data):
        threading.Thread.__init__(self)

        self.data = data
        
        port = 5
        backlog = 1
            
        self.server_sock = BluetoothSocket( RFCOMM )
        self.server_sock.bind( ("", port) )
        self.server_sock.listen( backlog )


        self.client_sock = BluetoothSocket( RFCOMM )

        uuid = "df0677bc-5f0b-45e4-8207-122adee18805"
        
        advertise_service( self.server_sock, "alarm",
                           service_id = uuid,
                           service_classes = [ uuid, SERIAL_PORT_CLASS],
                           profiles = [SERIAL_PORT_PROFILE])
    
    # This is the code run in parellel to the thread its called from
    # it will continually run until a keyboard interrupt or if it's
    # killed from the main thread
    def run(self):
        try:
            while(True):

                print "waiting for connection..."
                self.client_sock, client_info = self.server_sock.accept()
                print "Accepted connection from ", client_info
                    
                print "waiting for data..."
                raw_data = self.client_sock.recv(1024)

                self.data.set_time( int(raw_data[0:4]) )
                self.data.set_alarm_time ( int(raw_data[5:9]) )
                self.data.set_alarm = ( int(raw_data[10]) )
                self.data.set_light( int(raw_data[12]) )
                self.client_sock.send ("Data Received")

                print self.data

                self.client_sock.close()

        except KeyboardInterrupt:
            self.stop()

    #Function to safely stop the bluetooth communications
    def stop(self):
        self.keepalive = False
        stop_advertising (self.server_sock)
        self.client_sock.close()
        self.server_sock.close()

# *** app_data ***
# Is a class to encapsulate the application data sent form the mobile app
class app_data():
    def __init__(self):
        self.__time
        self.__alarm_time
        self.__alarm_control
        self.__light_control

    def set_time(self, time):
        self.__time = time
        #Set the actual system time here and then time modules can be used

    def set_alarm_time(self, alarm_time):
        self.__alarm_time = alarm_time

    def set_alarm_status(self, control):
        self.__alarm_control = control

    def set_light_status(self, control):
        self.__alarm_control = control
    
    def time(self):
        return self.__time
    #Set the actual system time here and then time modules can be used
    
    def alarm_time(self):
        return self.__alarm_time
    
    def alarm_status(self):
        return self.__alarm_control
    
    def light_status(self):
        return self.__alarm_control

    def print_settings():
        print "Time is", self.__time
        print "Alarm is set for ", self.__alarm_time
        print "Alarm is ",  self.__alarm_control
        print "Light is ", self.__light_control
