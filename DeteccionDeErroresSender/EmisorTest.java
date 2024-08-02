import java.util.Random;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class EmisorTest {
    @Test
    public void testFletcherChecksum() {
        // Casos de prueba
        List<Byte> data = Arrays.asList((byte)0b10101010, (byte)0b01010101);
        int[] expectedChecksum = {140, 0};
        int[] actualChecksum = Emisor.fletcherChecksum(data, 8);
        assertEquals(expectedChecksum[0], actualChecksum[0]);
        assertEquals(expectedChecksum[1], actualChecksum[1]);
    }
}

public class MessageGenerator {
    public static String generateBinaryMessage(int length) {
        StringBuilder sb = new StringBuilder(length);
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            sb.append(random.nextBoolean() ? '1' : '0');
        }
        return sb.toString();
    }

    public static String introduceError(String message, double errorRate) {
        char[] chars = message.toCharArray();
        Random random = new Random();
        for (int i = 0; i < chars.length; i++) {
            if (random.nextDouble() < errorRate) {
                chars[i] = chars[i] == '0' ? '1' : '0';
            }
        }
        return new String(chars);
    }
}
