import time
import sys

def panque(panques=267):
	i=0
	j = True
	while(True):
		time.sleep(0.001)
		print((i*" ")+"PANQUE MEU QUEIXO")
		
		i = i+1 if j else i-1
		if i == panques:
			j=False
		elif i == 0:
			j=True

panque(int(sys.argv[1]))

