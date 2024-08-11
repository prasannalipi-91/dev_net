from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H_%M")
print("Current Time =", current_time)


