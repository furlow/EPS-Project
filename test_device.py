from bluetooth import *
import sys

server_info = find_service(uuid = '4cc9159d-8a9a-4436-86c4-92bde11e2603')


if(server_info == 0):
	print('Could not find the device that you were looking for')
	sys.exit(0)
else:
	print("Devices found")
	i=0
	for device in server_info:
		print(str(i) + ": " + device['name'])
		i += 1

input = int(raw_input('Select Device that you want to connect to:'))

server_info = server_info[input]

client=BluetoothSocket( RFCOMM )
client.connect( (server_info['host'], server_info['port']) )

try:
	while True:
		data = client.recv(1024)
		if(data.find('>>') > -1):
			client.send(raw_input('>>'))
		else:
			print data.rstrip()
except KeyboardInterrupt:
	print('closing socket')
	client.close()
except btcommon.BluetoothError:
	client.close()
	sys.exit(0)
