from bluetooth import *

tones = ["alarm-a", "alarm-b", "alarm-c"]

def run_cmd(socket, cmd):
	if(cmd.find('set_clock_time') != -1):
		socket.send("Input time in string format of ss:mm:hh:dd:mm:yy\n")
		socket.send(">>\n")
		data = socket.recv(1024)
	elif (cmd.find('set_alarm_time') != -1):
		socket.send("Input the alarm time in string format of mm:hh\n")
		socket.send(">>\n")
		data = socket.recv(1024)
	elif (cmd.find('set_alarm_tone') != -1):
		socket.send("Please input the name of an alarm tone")
		socket.send(">>\n")
		data = socket.recv(1024)
	elif (cmd.find('get_alarm_tones') != -1):
		for tone in tones:
			socket.send("Alarm Tones available:\n")
			socket.send(tone + "\n")

port = 2


server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",port))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "4cc9159d-8a9a-4436-86c4-92bde11e2603"

advertise_service( server_sock, "Control",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
                    )

while True:
	try:
		print("Waiting for client to connect on " + str(port))

		phone, phone_info = server_sock.accept()
		print("Accepted connection from " + str(phone_info))

		phone.send("Welcome to Natures Alarm control\n\r")
		phone.send("Please use the following commands to set up the natures alarm\n\r")
		phone.send("set_clock_time\n")
		phone.send("set_alarm_time\n")
		phone.send("set_alarm_tone\n")
		phone.send("get_alarm_tones\n")

		while True:
			phone.send(">>\n")
			cmd = phone.recv(1024)
			run_cmd(phone, cmd)

	except btcommon.BluetoothError:
		print "Phone diconnected"
		phone.close()
		pass

	except KeyboardInterrupt:
		print "Closing sockets cleanly"
		phone.close()
		server_sock.close()
		raise

