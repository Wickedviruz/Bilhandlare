import os

#kod för att köra clear och rensa upp UI
def clear(): os.system('cls')

#Lägga till bilar i "databasen" (textfilen cars)
def addcar():
    clear() # Rensar consolen för att det skall se rent ut
    print("Lägg till bilar")
    märke = input("Vilket bilmärke är det? ")
    modell = input("Vilken modell av " + märke + " är det? ")
    årsmodell = int(input('Vilken årsmodell är det? '))
    kilometer = int(input('Hur många kilometer har den gått? '))
    clear()
    print("Bilen du lagt in är: ")
    print("Tillverkare: " + märke + " || " "Modell: " + modell + " || " "Tillverkninsår: " + str(årsmodell) + " || " "Mätarställning: " + str(kilometer))
    yn=input("Vill du spara den? ja/nej ")
    # fråga om man vill spara bilen eller inte
    if yn=="ja":
        file=open("cars.txt", "a")
        file.write("Tillverkare: " + märke + " || " "Modell: " + modell + " || " "Tillverkninsår: " + str(årsmodell) + " || " "Mätarställning: " + str(kilometer) +"\n")
        file.close #Stänger öppnad fil
        clear()
        input("Bil tillagd, Tryck 'ENTER' för att komma tillaka till huvudmenyn")

    #Nej svar och bilen sparas ej till textfilen
    elif yn=="nej":
        clear()
        print("Okej bilen är ej sparad")
        input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

    #Vid felinmatning av nummer
    else:
        error()

#Visa alla bilar och dess info ifrån filen "cars.txt"
def showcar():
    clear() # Rensar consolen för att det skall se rent ut
    print("********************************")
    print("Här är alla bilar i erat lager: ")
    print("********************************")
    file=open("cars.txt", "r") #öppnar filen cars.txt i läga "r"
    print(file.read())
    file.close #Stänger öppnad fil
    input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

# function för att lägga till köpare i "databasen" (textfilen user)
def buyer():
    clear() # Rensar consolen för att det skall se rent ut
    print("Lägg till köpare")
    förnamn = input("Förnamn: ")
    efternamn = input("Efternamn: ")
    telnr = int(input("Telefon nummer: "))
    adress = input("Adress: ")
    clear()
    print("Kundens information:")
    print("Förnamn: " + förnamn + " || " "Efternamn: " + efternamn + " || " "Telefon nummer: " + str(telnr) + " || " "Adress: " + adress)
    yn=input("Vill du spara kunden? ja/nej")

    if yn=="ja":
        file=open("buyer.txt",mode="a") #öppnar filen buyer.txt i läga "a"
        file.write("Förnamn: " + förnamn + " || " "Efternamn: " + efternamn + " || " "Telefon nummer: " + str(telnr) + " || " "Adress: " + adress +"\n")
        file.close #Stänger öppnad fil
        clear()
        input("Köpare tillagd i systemet! Tryck 'ENTER' för att komma tillaka till huvudmenyn")
    
    elif yn=="nej":
        clear()
        print("Okej kunden är ej sparad")
        input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

    #Vid felinmatning av nummer
    else:
        error()  

def showbuyer():
    clear() # Rensar consolen för att det skall se rent ut
    print("************************")
    print("Här är alla era kunder: ")
    print("************************")
    file=open("buyer.txt", "r") #öppnar filen buyer.txt i läga "r"
    print(file.read())
    file.close #Stänger öppnad fil
    input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

# function för att lägga till personal i "databasen" (textfilen user)
def addstaff():
    clear() # Rensar consolen för att det skall se rent ut
    print("Lägg till personal")
    förnamn = input("Förnamn: ")
    efternamn = input("Efternamn: ")
    adress = input("Adress: ")
    telnr = int(input("Telefon nummer: "))
    persnr =(input("Personnummer: "))
    månadslön = int(input("Månadslön: "))
    clear()
    print("Ny anställds information:")
    print("Förnamn: " + förnamn + " || " "Efternamn: " + efternamn + " || " "Adress: " + adress + " || " "Telefon nummer: " + str(telnr) + " || " "Person nummer: " + (persnr) +" || " "Månadslön: " + str(månadslön))
    yn=input("Vill du spara denna anställda? ja/nej")
    if yn=="ja":
        file=open("staff.txt",mode="a") #öppnar filen staff.txt i läga "a"
        file.write("Förnamn: " + förnamn + " || " "Efternamn: " + efternamn + " || " "Adress: " + adress + " || " "Telefon nummer: " + str(telnr) + " || " "Person nummer: " + (persnr) +" || " "Månadslön: " + str(månadslön) +"\n")
        file.close #Stänger öppnad fil
        clear() # Rensar consolen för att det skall se rent ut
        input("Personal tilllagd i systemet! Tryck 'ENTER' för att komma tillaka till huvudmenyn")
    
    elif yn=="nej":
        clear()
        print("Okej kunden är ej sparad")
        input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

    #Vid felinmatning av nummer
    else:
        error() 

# function för att visa all personal
def showstaff():
    clear() # Rensar consolen för att det skall se rent ut
    print("*********************")
    print("Här är eran personal: ")
    print("*********************")
    file=open("staff.txt", "r") #öppnar filen staff.txt i läga "r"
    print(file.read())
    file.close #Stänger öppnad fil
    input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

#Funktion vid val av ej giltigt alternativ
def error():
    clear()
    print("Du valde ett ej giltigt alternativ!")
    input("Tryck 'ENTER' för att komma tillaka till huvudmenyn")

while True:

    #Meny utskrift
    clear() # Rensar consolen för att det skall se rent ut
    print('**************************')
    print('**Bilfirma firmware v1.0**')
    print('**************************\n')
    print('1. Hantera bilar')
    print('2. Hantera kunder')
    print('3. Hantera personal\n')
    print('4. Avsluta programmet\n')

    #Användarens val
    User_Choice=input('Skriv in ditt val: ')

    #Val för att visa menyn för att lägga till bilar och visa bilar
    if User_Choice== "1":
        clear() # Rensar consolen för att det skall se rent ut
        print('**************************')
        print('**Bilfirma firmware v1.0**')
        print('**************************\n')
        print('1. Lägg till bil')
        print('2. Lagerförda bilar\n')

        #Användarens val
        User_Choice1=input('Skriv in ditt val: ')

        #Val för att gå till "function" addcar
        if User_Choice1=="1":
            addcar()
        
        #Val för att gå till functionen showcar
        elif User_Choice1=="2":
            showcar()

        #Error handler vid val av ej giltigt alternativ
        else:
            error()
        
    #Val för att lägga till köpare och visa köpare
    elif User_Choice== "2":
        clear() # Rensar consolen för att det skall se rent ut
        print('**************************')
        print('**Bilfirma firmware v1.0**')
        print('**************************\n')
        print('1. Lägg till köpare')
        print('2. Lista över köpare\n')

        #Användarens val
        User_Choice2=input('Skriv in ditt val: ')

        #Val för att gå till "function" buyer
        if User_Choice2=="1":
            buyer() #kallelse till functionen buyer
        
        #Val för att gå till functionen showbuyer
        elif User_Choice2=="2":
            showbuyer() #kallelse till functionen showbuyer

        #Error handler vid val av ej giltigt alternativ
        else:
            error()

    #Val för att lägga till och visa personal
    elif User_Choice== "3":
        clear() # Rensar consolen för att det skall se rent ut
        print('**************************')
        print('**Bilfirma firmware v1.0**')
        print('**************************\n')
        print('1. Lägg till ny personal')
        print('2. Lista över personal\n')

        #Användarens val
        User_Choice3=input('Skriv in ditt val: ')

        #Val för att gå till "function" addstaff
        if User_Choice3=="1":
            addstaff()#kallelse till functionen staff
        
        #Val för att gå till functionen showstaff
        elif User_Choice3=="2":
            showstaff() #kallelse till functionen showstaff

        #Error handler vid val av ej giltigt alternativ
        else:
            error()

    #Val att avsluta programmet
    elif User_Choice== "4":
        clear() # Rensar consolen för att det skall se rent ut
        print("Du har valt att avsluta programmet")
        input("Tryck enter för att avsluta programmet")
        break # break för att ta sig ur loopen

    else:
        error()

#Avslutnings meddelande
print("Programmet avslutas")