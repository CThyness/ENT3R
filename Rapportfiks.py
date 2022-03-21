filname = "rapport.csv" #Filen som skal sorteres, husk å endre navnet slik at det stemmer
f = open(filname)
f.readline() #Bli kvitt første linje som bare inneholder kategorinavn

guests = []
for line in f:
    values = line.split(",")

    if values[0] == '"': #Sjekker om navnet har fått " om seg og eventuelt fjerner det
        values[0] = values[0][1:-1]

    if values[0].lower() not in guests and values[2] != "Moderator": #Sjekker at eleven ikke er i listen eller moderator
        guests.append(values[0])

print(guests)