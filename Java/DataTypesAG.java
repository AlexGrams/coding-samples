/**
 * Write a description of class DataTypesAG here.
 *
 * @author Alex Grams
 * @version 9-17-20
 */
import java.util.Random;
import java.util.Scanner;

public class DataTypesAG
{
    public void dataTypesTest()
    {
        // Testing different data types
        int myGrade =  96;
        long cityPopulation = 325467984379L;
        byte ageInYears = 100;
        float salesTax = 0.05f;
        double interestRate = 0.812;
        double avogadroNumber = +6.022E23;
        char finalGrade = 'F';
        boolean isEmpty = true;

        System.out.println("myGrade is " + myGrade);
        System.out.println("cityPopulation is " + cityPopulation);
        System.out.println("ageInYears is " + ageInYears);
        System.out.println("salesTax is " + salesTax);
        System.out.println("interestRate is " + interestRate);
        System.out.println("avogadroNumber is " + avogadroNumber);
        System.out.println("finalGrade is " + finalGrade);
        System.out.println("isEmpty is " + isEmpty);
    }

    public void literals()
    {
        System.out.println("One potato\nTwopotatoes\n");
        System.out.println("\tTabs can make the output easier to read");
        System.out.println("She said, \"Java is fun\"");
    }

    /*
     * Escape chars examples \n, \t, \b, \\
     */
    public void diamond()
    {
        System.out.println("  \\/");
        System.out.println(" \\\\//");
        System.out.println("\\\\\\///");
        System.out.println("///\\\\\\");
        System.out.println(" //\\\\");
        System.out.println("  /\\");
    }

    public void constants()
    {
        // Testing constant values
        final char ZORRO = 'Z';
        final double PI = 3.14159;
        final int DAYS_IN_LEAP_YEAR = 366;

        System.out.println("ZORRO is: " + ZORRO);
        System.out.println("PI is: " + PI);
        System.out.println("DAYS_IN_LEAP_YEAR is: " + DAYS_IN_LEAP_YEAR);
    }

    public void mathOperators()
    {
        // Find cost of lunch
        double salad = 5.95;
        double water = 0.89;
        System.out.println("The cost of lunch is $" + (salad + water));
        System.out.println(salad + water + " is the cost of lunch");
        System.out.println("" + salad * 2 + " is this correct as well?");

        // Calculate age in certain year;
        int targetYear = 2025;
        int birthYear = 2005;
        System.out.println("Your age in " + targetYear + " is " + (targetYear - birthYear));

        // Total calories in a bunch of apples
        int caloriesPerApple = 127;
        int numberOfApples = 3;
        System.out.println("The total calories of the apples is " + (caloriesPerApple * numberOfApples));
    }

    public void escape1()
    {
        System.out.println(" ");
        System.out.println(" qqq ");
        System.out.println(" qqq ");
        System.out.println(" qqq ");
        System.out.println(" qqq ");
        System.out.println(" qqq ");
    }

    public void escape2()
    {
        System.out.println("What is the differnce between \na' and a \"? Or between a \" and a \\\"?\n");
        System.out.println("One is what we see when we're typing our program.\nThe other is what appears on the \"console.\"");
    } 

    public void loop1()
    {  //sjsjsj
        //Use to run statements multiple times
        for(int n = 0; n<12; n++ )
        {
            System.out.println("Hi " + n + " times");
        }
    }

    public void loop2()
    {
        Random rrr = new Random();
        int num;

        //Use to run statements multiple times
        for(int n = 0; n<10; n++ )
        {
            num = rrr.nextInt(10);
            System.out.print(num + " ");
        }
        System.out.println();
    }

    // Write a method that prints 10 ages for a group of people. Make the age typical high school
    // students 14 to 18
    public void highSchoolAge()
    {
        Random rng = new Random();
        
        for (int i = 0; i < 10; i++)
        {
            System.out.println(rng.nextInt(5) + 14);
        }
    }

    public void read1()
    { //sect 4.3 sjsj
        Scanner in = new Scanner(System.in);
        int amy, ben, mac; //ages

        //Prompt the user for information
        System.out.print("Amy's age: "); 
        amy = in.nextInt();

        System.out.print("Ben's age: "); 
        ben = in.nextInt(); 
        
        System.out.print("Mac's age: ");
        mac = in.nextInt();

        double avg = (amy + ben + mac) / 3.0;
        System.out.println("Average age = " + avg);      
        //System.out.printf ("or about 1234");
        System.out.printf("or about %.2f", avg);
        System.out.println();
    }

    public void read2( )
    {
        for(int n=0; n<3; n++)
        {
            //qqq
            System.out.println();
        }
    }

    // Given a double, print the number of quarters
    public void numQuarters(double amt)
    {
        System.out.println((int)(amt / 0.25));
    }

    public int numDimes(double amt)
    {
        return 1234;
    }
    
    public void quartersLoop()
    {
        Scanner in = new Scanner(System.in);
        Random rng = new Random();
        int n;
        
        System.out.print("How many loops: ");
        n = in.nextInt();
        
        for(int i = 0; i < n; i++)
        {
            double money = 50.00 + rng.nextDouble() * 50.0;
            numQuarters(money);
        }
    }
}
