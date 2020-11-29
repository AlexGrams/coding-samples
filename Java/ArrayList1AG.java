
/**
 * Write a description of class ArrayList1YI here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 * 
 */
import java.util.ArrayList;
import java.util.Random;
public class ArrayList1AG
{
    //Instance variables, declare 3 arrayList
    private ArrayList<Integer> age;
    private ArrayList<Double>  gpa;
    private ArrayList<String>  str;
    private int[] age1;
    
    //Constructor
    public ArrayList1AG()
    {
        Random rrr = new Random();
        age=new ArrayList<Integer>();
        gpa=new ArrayList<Double>();
        str=new ArrayList<String>();
        age1 = new int[10];
    }

    public void addRandomAge()
    {
        Random rng = new Random();
        
        age.add(rng.nextInt(90) + 10);
    }
  
    public void addRandomGPA()
    {
        Random rng = new Random();
        
        gpa.add(rng.nextInt(400) / 100.0);
    }

    public void addStr(String aWord)
    {
        str.add("Alex");
        str.add("Jimin");
        str.add("Bill");
        str.add( aWord );
    }


    public void addRandomAge(int count)
    {
        for (int i = 0; i < count; i++)
        {
            addRandomAge();
        }
    }

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
    Hint: The % operator may be useful.
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

    public void deleteAge(int index)
    {
        if (index < 0 || index >= age.size())
        {
            return;
        }
            
        age.remove(index);
    }
    
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
    

    public void printSize()
    {
        System.out.println("\nage: "+age.size());
        System.out.println("gpa: "+gpa.size());
        System.out.println("str: "+str.size());
        
    }
    
    public void printAllArrayList()
    {
        System.out.println("\nAGE arraylist:  "+age);
        System.out.println("GPA arraylist:  "+gpa);
        System.out.println("STR arraylist:  "+str);
    }

}
