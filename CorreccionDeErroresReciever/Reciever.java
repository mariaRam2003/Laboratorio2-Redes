import java.util.Arrays;

public class Reciever{
    int[] message;
    int parityQuantity;

    public Reciever(int[] message){
        this.message = message;
        this.parityQuantity = this.getParityBitNumber(this.message);
        run();
    }

    private void run(){
        int parityNo = this.parityQuantity;
        Integer[] parityBits = new Integer[parityNo];  // We alocate the memory for the parity bits in the array

        for (int i = 0; i < parityNo; i++){
            int parity_index = (int) Math.pow(2, i);
            int parityBit = this.calculateParityBits(this.message, parity_index);
            parityBits[i] = parityBit;
        }
        System.out.println("Mensaje obtenido: ");
        System.out.print(Arrays.toString(this.message));
        System.out.println("");

        int errorIndex = this.checkMatch(parityBits);
        if ((xor(this.message)== 0) & (errorIndex != 0)){
            System.out.println("Multiple errors");
        }else if ((errorIndex - 1) >= this.message.length){
            System.out.println("Multiple errors");
        }else if (errorIndex == 0){
            System.out.println("No error");
        }else{
            int errorBit = this.message[errorIndex - 1];
            System.out.println("El error esta en el indice: " + String.valueOf(errorIndex) + "\n");

            // We flip the bit
            if (errorBit == 1){
                this.message[errorIndex - 1] = 0;
            }else{
                this.message[errorIndex - 1] = 1;
            }

            // we print the corrected version
            System.out.print("La version corregida del mensaje es: ");
            for (int i = 0; i < this.message.length; i++){
                System.out.print(this.message[i]);
            }
            System.out.println("");
        }

//        for (int i = 0; i < parityBits.length; i++){
//            System.out.println(parityBits[i]);
//        }
    }

    public static int xor(int[] message){
        int result = 0;
        for (int bit : message) {
            result ^= bit;
        }
        return result;
    }

    public static boolean isPowerOfTwo(int n){
        return (n & (n - 1)) == 0;
    }

    public int checkMatch(Integer[] parityBits){
        // TODO: revisame
        int errorBit = 0;

        for (int i = 0; i < this.parityQuantity; i++){
            int power = (int) Math.pow(2, i);
            int actualParity = parityBits[i];
            int messageParityBit = this.message[power - 1]; // we substract one because index are zero based

            if (actualParity != messageParityBit) {
                errorBit = errorBit + power;
            }
        }

        return errorBit;
    }

    public int getParityBitNumber(int[] encodedMessage){
        int encoded_len = encodedMessage.length;
        int r_no = 0;
        int index = 0;

        while (r_no < encoded_len){
            r_no = (int) Math.pow(2, index);
            index++;
        }

        return index - 1;
    }

    public int calculateParityBits(int[] encodedMessage, int parityBitNo){
        if (!isPowerOfTwo(parityBitNo)){
            throw new RuntimeException("parity bit number must be a power of 2\n");
        }

        int index = parityBitNo - 1;
        boolean toCheck = false;
        int count = 0;
        int count_ones = 0;

        while (index < encodedMessage.length){
            if (count % parityBitNo == 0){
                toCheck = !toCheck;
            }

            if (toCheck){
                if (isPowerOfTwo(index + 1)){

                }else if (encodedMessage[index] == 1){
                    count_ones++;
                }
            }

            index++;
            count = (count + 1) % parityBitNo;
        }

        return count_ones % 2;
    }




}