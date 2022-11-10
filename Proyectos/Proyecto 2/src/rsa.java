import java.math.BigInteger;
import java.util.Random;

/**
 * Esta clase implementa el algoritmo RSA.
 * 
 * @author Victor Hugo Gallegos Mota
 * @author José Demian Jiménez
 * @author Carlos Cruz Rangel
 */

class rsa {
    // Para asegurar que la longitud del primo es de al menos 100 dígitos
    private int bitLength = 512;

    // Dos números primos aleatorios
    BigInteger p = BigInteger.probablePrime(bitLength, new Random());
    BigInteger q = BigInteger.probablePrime(bitLength, new Random());
    // n = p*q
    BigInteger n = p.multiply(q);
    // phi(n) = (p-1)*(q-1)
    private BigInteger phi = (p.subtract(BigInteger.ONE)).multiply(q.subtract(BigInteger.ONE));

    // e es un número primo relativo a phi(n)
    private BigInteger e_aux = BigInteger.probablePrime(bitLength / 2, new Random());
    // e tal que gcd(e,\phi(n)) = 1
    BigInteger e = e_aux.gcd(phi).equals(BigInteger.ONE) ? e_aux : e_aux.nextProbablePrime();
    // d tal que e*d = 1 mod \phi(n)
    BigInteger d = e.modInverse(phi);

    /**
     * Cifra el mensaje m con la clave pública (n,e)
     *
     * @param n Producto de los primos p y q
     * @param e Número primo tal que `gcd(e,\phi(n)) = 1`
     * @param m Mensaje a cifrar
     * @return Arreglo de bytes con el mensaje cifrado
     */
    public BigInteger[] encrypt(BigInteger n, BigInteger e, String m) {
        int length = m.length();
        BigInteger[] arr_r = new BigInteger[length];

        for (int i = 0; i < length; i++) { // Cifrar cada caracter
            arr_r[i] = BigInteger.valueOf((int) m.charAt(i)).modPow(e, n);
        }

        return arr_r;
    }

    /**
     * Descifra el mensaje m con la clave privada (n,d)
     *
     * @param n Producto de los primos p y q
     * @param d Número tal que e*d = 1 mod \phi(n)
     * @param m Arreglo de bytes con el mensaje cifrado
     * @return Mensaje descifrado
     */
    public String decrypt(BigInteger n, BigInteger d, BigInteger[] m) {
        int length = m.length;
        StringBuilder msg = new StringBuilder();

        for (int i = 0; i < length; i++) {
            msg.append((char) m[i].modPow(d, n).intValue());
        }

        return msg.toString(); // Regresar el mensaje descifrado
    }

    public static void main(String[] args) { // Metodo principal del programa
        // Creación de la instancia del cifrado RSA
        rsa rsa = new rsa();

        // Valor a usar en el cifrado y descifrado
        BigInteger n = rsa.n; // n = p*q
        BigInteger e = rsa.e; // e tal que gcd(e,\phi(n)) = 1
        BigInteger d = rsa.d; // d tal que e*d = 1 mod \phi(n)

        // Llave p y q
        System.out.println(String.format("Llave p = %s", rsa.p));
        System.out.println(String.format("Llave q = %s", rsa.q));
        System.out.println("--------------------------------");

        // N, e, d
        System.out.println(String.format("N = %s", n));
        System.out.println("--------------------------------");
        System.out.println(String.format("e = %s", e));
        System.out.println(String.format("d = %s", d));
        System.out.println("--------------------------------");

        // Mensaje a cifrar
        System.out.println("Mensaje a cifrar:");
        String msg = "niño";
        System.out.println(msg);

        System.out.println("--------------------------------");

        // Cifrar el mensaje
        BigInteger[] encryptedMessage = rsa.encrypt(n, e, msg);
        System.out.println("Mensaje cifrado:");
        for (BigInteger i : encryptedMessage) {
            System.out.print(i + " ");
        }
        System.out.println();
        System.out.println("--------------------------------");

        // Descifrar el mensaje
        String decryptedMessage = rsa.decrypt(n, d, encryptedMessage);
        System.out.println("Mensaje descifrado:");
        System.out.println(decryptedMessage);
    }

}