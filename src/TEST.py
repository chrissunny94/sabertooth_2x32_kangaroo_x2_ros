from pysabertooth import Sabertooth

saber = Sabertooth('/dev/ttyACM0', baudrate=115200, address=128, timeout=0.1)

# drive(number, speed)
# number: 1-2
# speed: -100 - 100
count = 1
while(count<1000):
	saber.drive(1, 100)
	saber.drive(2, 100)
	count=count+1
saber.stop()
