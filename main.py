from src import nfc
import time

while True:
    try:
        reader = nfc.Reader()
        uid = reader.get_uid()
        if uid is not None:
            print("Qurilmaning UID:", uid)

    except:
        time.sleep(0.1)
