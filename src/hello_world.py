import datetime

print("Hello World")

with open("date.out", 'w') as file:
    file.write(datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"))