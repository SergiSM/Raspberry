from datetime import datetime, timedelta

dt_old = datetime.strptime("2017-05-17 10:00:00", "%Y-%m-%d %H:%M:%S")
file = open("file.csv", "r")
file_w = open("new.csv", "w")

for line in file:
    if len(line) < 40:
        try:
            data, hora, humitat, temperatura = line.split(";")
            dia, mes, anyy = data.split(".")
            hora, minut, segons = hora.split(":")

            if int(mes) <= 12 and int(mes) > 0 and int(dia) <= 31 and int(dia) > 0:
                dt_new = datetime(int(anyy), int(mes), int(dia), int(hora), int(minut), int(segons))
                diff = (dt_new-dt_old).total_seconds()
                if diff > 15:
                    dt_new = dt_old + timedelta(seconds=10)

                print(dt_new)
                dt_old = dt_new

                data, hora = str(dt_new).split(" ")
                file_w.write(str(data)+";"+str(hora)+";"+humitat+";"+temperatura)
        except:
            print("Error ")
