
/**
 * Creates an NxN matrix using a 1D array consisting of the numbers 
 * 1 through N^2 and allows the user to scramble their order.
 *
 * @author Alex Grams
 */
import java.util.Random;

public class NxNMatrix
{
    private int[] array;
    private int rows;
    
    public NxNMatrix(int size)
    {
        array = new int[size * size];
        rows = size;
        
        for (int i = 0; i < array.length; i++)
        {
            array[i] = i + 1;
        }
    }
    
    // Returns a String containing all elements in the matrix ordered by row and column
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
    
    // Prints this matrix
    public void printMe()
    {
        System.out.println(toString());
    }
    
    // Returns the sum of all elements in row r
    public int addRow(int r)
    {
        int sum = 0;
        
        for (int i = rows * r; i < rows * (r + 1); i++)
        {
            sum += array[i];
        }
        
        return sum;
    }
    
    // Returns the sum of all elements in column c
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
    
    // Returns the sum of all digits from top left to bottom right
    public int addDiag1()
    {
        int sum = 0;
        
        for (int i = 0; i < array.length; i += rows + 1)
        {
            sum += array[i];
        }
        
        return sum;
    }
    
    // Returns the sum of all digits from top right to bottom left
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
