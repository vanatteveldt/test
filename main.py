import datetime
with open("test.txt", "w") as f:
    f.write(datetime.datetime.now().isoformat())
