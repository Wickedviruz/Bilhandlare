using System;

class MainClass
{
    public static void Main(string[] args)
    {

        //Variable för användares val
        int x = 0;

        while (true)
        {

            //Clear commando för att hålla UIt snyggt och rent
            Console.Clear();

            //Huvudmenyn
            Console.WriteLine("Huvudmeny");
            Console.WriteLine("**********");
            Console.WriteLine("1. Bilmärken");
            Console.WriteLine("2. Reservdelar");
            Console.WriteLine("3. Service bokning\n");
            Console.WriteLine("4. Avsluta program\n");

            //Användar input och konvertering 
            Console.WriteLine("Skriv in ditt val");
            x = Convert.ToInt32(Console.ReadLine());

            // If statements för att välja meny beroende på user input
            if (x == 1)
            {
                Console.Clear();
                Console.WriteLine("Bilmärken");
                Console.WriteLine("Tryck enter för att komma tillbaka till menyn");
                Console.ReadKey();
            }
            if (x == 2)
            {
                Console.Clear();
                Console.WriteLine("Reservdelar");
                Console.WriteLine("Tryck enter för att komma tillbaka till menyn");
                Console.ReadKey();
            }
            if (x == 3)
            {
                Console.Clear();
                Console.WriteLine("Service bokning");
                Console.WriteLine("Tryck enter för att komma tillbaka till menyn");
                Console.ReadKey();
            }

            //Val för att avsluta programmet
            if (x == 4)
            {
                Console.Clear();
                Console.WriteLine("Du har valt att avsluta programme");
                Console.WriteLine("Tryck enter för att avsluta programmet");
                Console.ReadKey();
                Console.Clear();
                Console.WriteLine("Programmeet har avslutats");
                break;
            }

            else
            {
                Console.WriteLine("Du valde ett ej giltigt alternativ. vänligen försök igen.");
                Console.WriteLine("Tryck enter för att komma tillbaka till menyn");
                Console.ReadKey();
            }
        }
    }
}