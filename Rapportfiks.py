filname = "rapport.csv" #Filen som skal sorteres, husk å endre navnet slik at det stemmer
f = open(filname)
f.readline() #Bli kvitt første linje som bare inneholder

guests = []
for line in f:
    values = line.split(",")

    if values[0] == '"':
        values[0] = values[0][1:-1]
    if values[0].lower() not in guests and values[2] != "Moderator": #Sjekker at eleven ikke er i listen eller moderator
        guests.append(values[0].lower())

print(guests)