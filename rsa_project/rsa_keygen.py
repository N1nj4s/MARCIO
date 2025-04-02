import random
from miller_rabin import generate_large_prime
from rsa_utils import mod_inverse

def generate_rsa_keys(bit_length=128):
    """
    Gera um par de chaves RSA (pública e privada).
    """
    # Gerar dois números primos grandes
    p = generate_large_prime(bit_length // 2)
    q = generate_large_prime(bit_length // 2)
    
    while p == q:
        q = generate_large_prime(bit_length // 2)
    
    # Calcular n e phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Escolher um expoente público e tal que seja coprimo com phi_n
    e = 65537  # Valor comum para e
    while phi_n % e == 0:
        e = random.randrange(3, phi_n, 2)  # Garante que e seja ímpar
    
    # Calcular d como o inverso modular de e mod phi_n
    d = mod_inverse(e, phi_n)
    
    # Retorna a chave pública e privada
    public_key = (e, n)
    private_key = (d, n)
    
    return public_key, private_key

if __name__ == "__main__":
    pub, priv = generate_rsa_keys()
    print("Chave pública:", pub)
    print("Chave privada:", priv)
