
/**
 * Performs operations on integer, double, and string ArrayLists
 * to demonstrate their functionality within Java
 * 
 * @author Alex Grams
 */
import java.util.ArrayList;
import java.util.Random;
public class ArrayListDemo
{
    private ArrayList<Integer> age;
    private ArrayList<Double>  gpa;
    private ArrayList<String>  str;
    
    //Constructor
    public ArrayListDemo()
    {
        age=new ArrayList<Integer>();
        gpa=new ArrayList<Double>();
        str=new ArrayList<String>();
    }

    // Adds random age from 10 to 99 to array of ages
    public void addRandomAge()
    {
        Random rng = new Random();
        
        age.add(rng.nextInt(90) + 10);
    }
  
    // Adds a random gpa from 0.00 to 4.00 to array of GPAs
    public void addRandomGPA()
    {
        Random rng = new Random();
        
        gpa.add(rng.nextInt(400) / 100.0);
    }

    // Adds three set names and one variable name to array of names
    public void addStr(String aWord)
    {
        str.add("James");
        str.add("Marcus");
        str.add("Bill");
        str.add( aWord );
    }

    // Adds multiple random ages to array of ages
    public void addRandomAge(int count)
    {
        for (int i = 0; i < count; i++)
        {
            addRandomAge();
        }
    }

    // Adds multiple random GPAs to array of GPAs
    public void addRandomGPA(int count)
    {
        for (int i = 0; i < count; i++)
        {
            addRandomGPA();
        }
    }

    /*    
    Return the count of all the even ages 
    in the array list. 
     */
    public int evenAges() 
    {     
        int count = 0;
        for( int each : age ) 
        {
            if(each%2==0)
            {
                count++;
            }
        }
        return count;
    }

    // Removes an age at index from age array
    public void deleteAge(int index)
    {
        if (index < 0 || index >= age.size())
        {
            return;
        }
            
        age.remove(index);
    }
    
    // Adds age at index of array
    public void addAgeAtIndex(int index, int newAge)
    {
        age.add(index, newAge);
    }
    
    // Finds index of first occurence of n, returns -1 if not in arrayList
    public int ageIndexOf(int n)
    {
        for (int i = 0; i < age.size(); i++)
        {
            if (age.get(i) == n)
            {
                return i;
            }
        }
        
        return -1;
    }
    
    // Prints size of age, GPA, and string arrays
    public void printSize()
    {
        System.out.println("\nage: "+age.size());
        System.out.println("gpa: "+gpa.size());
        System.out.println("str: "+str.size());
        
    }
    
    // Prints all elements of age, GPA, and string ArrayLists
    public void printAllArrayList()
    {
        System.out.println("\nAGE arraylist:  "+age);
        System.out.println("GPA arraylist:  "+gpa);
        System.out.println("STR arraylist:  "+str);
    }

}
