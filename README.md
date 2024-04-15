# RSA-Cryptography
 
**RSA implementation in Python**

RSA employs an asymmetric key encryption technique. This means that the encryption key used to secure a message is different from the decryption key, which is kept confidential and known only to the intended recipient. 

The computational hardness of this algorithm is prime factorization. To decrypt the messages, an adversary needs to recover the prime numbers p and q from the common modulus n = p ∗ q. 


**There are total of 8 functions in the code**

* **generate keypair:** This function accepts two distinct prime numbers and generates the public and private key pairs. The format is  ((n,e),(n,d)) where n is the common modulus, e is the public exponent, and d is the private exponent. If the input integers p and q are invalid, raise a exception. 

* **generate_public_exponent:** This is a helper function to help choose a public exponent. In real systems, there will be many choices for the value of e (public exponent). However, this function in the code is to compute the smallest value of e for a given k. 

* **modular_inverse:** This is a helper function to compute the modular inverse of an integer with respect to some arbitrary modulus. This is useful for computing the private exponent.

* **mod_exp:** A helper function with implementation of modular exponentiation and it implements an algorithm that performs the ”large mod” calculation 

* **gcd:** A helper function that computes the gcd of any two integers. This will be helpful when you choose the public exponent

* **isprime:** Checks if a given integer isprime. Returns true if prime,otherwise False

* **rsa_encrypt:** The RSA encryption function that encrypts a message using a public key. The input format of your message is integers. This function is not encrypting strings or other data types

* **rsa_decrypt:** The RSA decryption function that decrypts a message using a private key. The input and output will be integers

**NO external libraries used, including RSA, cryptography, or similar options**

**NO functions such as math.gcd for computing the gcd, pow for modular exponentiation and inverse, etc.**

**All the functions are implemented with standard math operations**