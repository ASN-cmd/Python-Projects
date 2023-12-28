import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))

if(timestamp >=0 and timestamp <12):
    print("Goodmorning Sir")
elif(timestamp >= 12 and timestamp < 18):
    print("GoodAfternoon Sir")
else:
    print("GoodEvening Sir")

