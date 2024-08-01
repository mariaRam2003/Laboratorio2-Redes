import java.util.ArrayList;

public class Main{
    public static void main(String[] args){
        ArrayList<int[]> testCases = new ArrayList<>(9);
        // sin errores
        testCases.add(new int[] {1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1});
        testCases.add(new int[] {1, 0, 1, 1, 0, 1});
        testCases.add(new int[] {1, 1, 0, 1, 0, 1, 0, 1, 1});

        // un error
        testCases.add(new int[] {1, 0, 0, 0, 1, 0, 1, 1, 1});
        testCases.add(new int[] {0, 1, 0, 1, 1, 0, 0});
        testCases.add(new int[] {1, 0, 0, 0, 1, 1, 0, 1, 0, 1});

        // dos errores
        testCases.add(new int[] {0, 1, 0, 1, 0, 1, 0, 1, 0});
        testCases.add(new int[] {1, 1, 1, 1, 1, 1});
        testCases.add(new int[] {1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1});

        for (int i = 0; i < testCases.size(); i++){
            System.out.println("~~~~~~~~~~~ TEST CASE " + String.valueOf(i + 1) + "~~~~~~~~~~~");
            int[] message = testCases.get(i);
            Reciever reciever = new Reciever(message);
        }
    }
}