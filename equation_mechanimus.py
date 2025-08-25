print("Geben Sie die Anzahl der Variablen ein (1-7)")
anzahl_variablen = int(input())

if anzahl_variablen < 1 or anzahl_variablen > 7:
    print("Ungültige Anzahl von Variablen. Bitte geben Sie eine Zahl zwischen 1 und 7 ein.")
    anzahl_variablen = int(input())
else:
    print("Gültige Anzahl von Variablen:", anzahl_variablen)
    
    if anzahl_variablen == 1:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung = input()
        print(f"Ihre Gleichung: {gleichung}")
    
    elif anzahl_variablen == 2:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung1 = input("Gleichung 1: ")
        gleichung2 = input("Gleichung 2: ")
        print(f"Ihre Gleichungen: {gleichung1} und {gleichung2}")
    
    elif anzahl_variablen == 3:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung1 = input("Gleichung 1: ")
        gleichung2 = input("Gleichung 2: ")
        gleichung3 = input("Gleichung 3: ")
        print(f"Ihre Gleichungen: {gleichung1}, {gleichung2} und {gleichung3}")
    
    elif anzahl_variablen == 4:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung1 = input("Gleichung 1: ")
        gleichung2 = input("Gleichung 2: ")
        gleichung3 = input("Gleichung 3: ")
        gleichung4 = input("Gleichung 4: ")
        print(f"Ihre Gleichungen: {gleichung1}, {gleichung2}, {gleichung3} und {gleichung4}")
   
    elif anzahl_variablen == 5:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung1 = input("Gleichung 1: ")
        gleichung2 = input("Gleichung 2: ")
        gleichung3 = input("Gleichung 3: ")
        gleichung4 = input("Gleichung 4: ")
        gleichung5 = input("Gleichung 5: ")
        print(f"Ihre Gleichungen: {gleichung1}, {gleichung2}, {gleichung3}, {gleichung4} und {gleichung5}")
   
    elif anzahl_variablen == 6:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung1 = input("Gleichung 1: ")
        gleichung2 = input("Gleichung 2: ")
        gleichung3 = input("Gleichung 3: ")
        gleichung4 = input("Gleichung 4: ")
        gleichung5 = input("Gleichung 5: ")
        gleichung6 = input("Gleichung 6: ")
        print(f"Ihre Gleichungen: {gleichung1}, {gleichung2}, {gleichung3}, {gleichung4}, {gleichung5} und {gleichung6}")
    
    elif anzahl_variablen == 7:
        print("Geben Sie Ihre Gleichung ein:")
        gleichung1 = input("Gleichung 1: ")
        gleichung2 = input("Gleichung 2: ")
        gleichung3 = input("Gleichung 3: ")
        gleichung4 = input("Gleichung 4: ")
        gleichung5 = input("Gleichung 5: ")
        gleichung6 = input("Gleichung 6: ")
        gleichung7 = input("Gleichung 7: ")
        print(f"Ihre Gleichungen: {gleichung1}, {gleichung2}, {gleichung3}, {gleichung4}, {gleichung5}, {gleichung6} und {gleichung7}")

    #Gleichungen loesen (Gauß-Algorithmus)