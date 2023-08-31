import psutil
import winsound
import time
from pathlib import Path
from win10toast import ToastNotifier

# path of the sound
sound = Path("sound/wrong-answer-129254.wav")

while True:
	
	# validate if battery percent is greater than 95
	if psutil.sensors_battery()[0] > 95:
		
		toast = ToastNotifier()
		toast.show_toast(
			"Reminder 🔋",
			f"Battery percent is {psutil.sensors_battery()[0]}%",
			duration=1,
			threaded=True
			)
		# play sound five times
		for x in range(0, 5):
		
			winsound.PlaySound(str(sound), winsound.SND_FILENAME)
			time.sleep(0.2)

		exit()