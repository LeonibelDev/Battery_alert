import psutil
from pathlib import Path
import winsound
import time

# path of the sound
sound = Path("sound/wrong-answer-129254.wav")

while True:
	
	# validate if battery percent is greater than 95
	if psutil.sensors_battery()[0] > 95:
		
		# play sound five times
		for x in range(0, 5):
		
			winsound.PlaySound(str(sound), winsound.SND_FILENAME)
			time.sleep(0.2)

		exit()