# Hier wird eine Funktion definiert welche zu einer bestimmten Uhrzeit eine Anzahl Minuten addiert.
def uhrzeit_minuten_addieren(stunden, minuten, summand): # Die Variable "uhrzeit_minuten_addieren" wird definiert.
    neueMinuten=minuten+summand 
    while neueMinuten >=60: # Wenn die neuen Minuten (Minuten+Summand) über 60 liegen, muss ...
        stunden=stunden+1 # die Stunde mit eins addiert werden
        neueMinuten=neueMinuten-60 # die neuen Minuten mit sechzig subtrahiert werden
    if stunden >= 24: # Wenn die Stunden über vierundzwanzig sind dann ...
           stunden=stunden-24 # dann müssen die Stunden mit vierundzwanzig subtrahiert werden
    print(str(stunden) +":" +str(neueMinuten)) # Der Output soll wie folgt aussehend: Stunden:neue Minuten
            
uhrzeit_minuten_addieren(17, 32, 8) # Hier werden die Zahlen in der Reihenfolge Stunden, Minuten, Summand eingegeben.
uhrzeit_minuten_addieren(19, 7, 63) 
uhrzeit_minuten_addieren(16, 10, 1111) 