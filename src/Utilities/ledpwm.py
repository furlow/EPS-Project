from time import sleep

for dc in range(1,101):
	dc_f = float(dc) / 100
	f = open('/dev/pi-blaster', 'w')
	f.write('27=' + str(dc_f))
	print('27=' + str(dc_f) + '\n')
	f.close()
	sleep(1)
