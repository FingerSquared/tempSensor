import time
import sys
import serial

arduino = serial.Serial('/dev/tty.usbmodem621', 9600)

target = open('temperature.tsv', 'w')
target.write('temp\ttime\n')
target.close()

temps = []
output = 0
averageLength = 20

arduino.readline()

def printToFile(status):
	target = open('temperature.tsv', 'a')
	status = "%.2f\t%s\n" % (status, time.strftime('%H:%M:%S'))
	target.write(status)
	print '===============%s============' % status
	target.close()

while True:
	if len(temps) < averageLength:
		status = arduino.readline()
		print '%r' % status[:5]
		temps.append(float(status[:5]))
		time.sleep(0.1)
		#print len(temps)
	else:
		output = 0
		for tmp in temps:
			output += tmp
		del temps[:]
		output = output/averageLength
		printToFile(output)