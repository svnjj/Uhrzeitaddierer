#Hier wird eine Funktion definiert welche zu einer Uhrzeit eine ANzahl Minuten addiert.
def uhrzeit_minuten_addieren(stunden, minuten, summand):
    neueMinuten=minuten+summand 
    while neueMinuten >=60:
        stunden=stunden+1
        neueMinuten=neueMinuten-60
    if stunden >= 24:
           stunden=stunden-24
    print(str(stunden) +":" +str(neueMinuten))
            
uhrzeit_minuten_addieren(17, 32, 8) # 17:32 + 8 Min = 17:40
uhrzeit_minuten_addieren(19, 7, 63) # 19:07 + 63 Min = 20:10
uhrzeit_minuten_addieren(16, 10, 1111) # 16:10 + 1111 Min = 10:41