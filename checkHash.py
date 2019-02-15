import time
import hashlib
count = 0



t_end = time.time() + 15
while time.time() < t_end:
        hashlib.sha256("HA")
        count += 1

print(count/15)
