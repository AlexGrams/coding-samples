
/**
 * Write a description of class NxNAG here.
 *
 * @author Alex Grams
 * @version 11-24-20
 */
import java.util.Random;

public class NxNAG
{
    private int[] array;
    private int rows;
    
    public NxNAG(int size)
    {
        array = new int[size * size];
        rows = size;
        
        for (int i = 0; i < array.length; i++)
        {
            array[i] = i + 1;
        }
    }
    
    public String toString()
    {
        String result = "";
        
        for (int i = 0; i < array.length; i++)
        {
            result += array[i] + " ";
            if (i % rows == rows - 1)
            {
                result += "\n";
            }
        }
        
        return result;
    }
    
    public void printMe()
    {
        System.out.println(toString());
    }
    
    public int addRow(int r)
    {
        int sum = 0;
        
        for (int i = rows * r; i < rows * (r + 1); i++)
        {
            sum += array[i];
        }
        
        return sum;
    }
    
    public int addCol(int c)
    {
        int sum = 0;
        
        for (int i = c; i < array.length; i += rows)
        {
            sum += array[i];
        }
        
        return sum;
    }
    
    // Shakes array by swapping position of each element in array
    public void shake()
    {
        int swapPos = 0;
        Random rng = new Random();
        
        for (int i = 0; i < array.length; i++)
        {
            swapPos = rng.nextInt(array.length);
            
            if (swapPos != i)
            {
                array[i] += array[swapPos];
                array[swapPos] = array[i] - array[swapPos];
                array[i] -= array[swapPos];
            }
        }
    }
    
    // Adds digits from top left to bottom right
    public int addDiag1()
    {
        int sum = 0;
        
        for (int i = 0; i < array.length; i += rows + 1)
        {
            sum += array[i];
        }
        
        return sum;
    }
    
    // Adds digits from top right to bottom left
    public int addDiag2()
    {
        int sum = 0;
        
        for (int i = rows - 1; i < array.length - 1; i += rows - 1)
        {
            sum += array[i];
        }
        
        return sum;
    }
}
