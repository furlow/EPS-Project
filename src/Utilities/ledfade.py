from time import sleep

start = 0
end = 100
direction = 1

f = open('/dev/pi-blaster', 'w+')

try:
	while(1):

		for dc in range(start,end, direction):
			dc_f = float(dc) / 100
			s = '27=' + str(dc_f) + '\n'
			f.write(s)
			f.flush()
			sleep(1)
		temp = start
		start = end
		end = temp
		direction = direction * -1

except KeyboardInterrupt:
	f.close()
