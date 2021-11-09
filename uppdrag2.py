import os #Importingin av OS

#variable för anävndarmenyn
x = 0 

# while statement för att skapa menyn
while True:

    #kod för att köra clear och rensa upp UI
    def clear(): os.system('cls')
    clear()

    #Meny utskrift
    print('Huvudmeny')
    print('*********')
    print('1. Bilmärken')
    print('2. Reservdelar')
    print('3. Service bokning\n')
    print('4. Avsluta programmet\n')

    #Användarens val
    x=int(input("Skriv in ditt val: "))

    #Vid val av första menyn
    if x==1:
        clear()
        print("Bilmärken")
        input("Tryck enter för att komma tillbaka till menyn")

    #Val av meny 2
    elif x==2:
        clear()
        print("Reservdelar")
        input("Tryck enter för att komma tillbaka till menyn")

    #Val av meny 3 
    elif x==3:
        clear()
        print("Service bokning")
        input("Tryck enter för att komma tillbaka till menyn")

    #Val att avsluta programmet
    elif x==4:
        clear()
        print("Du har valt att avsluta programmet")
        input("Tryck enter för att avsluta programmet")
        break

    #Fel hantering/felmeddelande vid fel inmatning av användare
    else:
        clear()
        print("Du valde ett ej giltigt alternativ. vänligen försök igen.")
        input("Tryck enter för att komma tillbaka till menyn")

#Avslutnings meddelande
print("Programmet avslutas")