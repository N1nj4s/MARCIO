import random

def is_prime(n, k=40):
    """
    Teste de primalidade de Miller-Rabin.
    Parâmetros:
    - n: número a ser testado
    - k: número de iterações do teste (quanto maior, mais preciso)
    Retorna True se n for primo, False caso contrário.
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    
    # Escreve n-1 como 2^r * d, com d ímpar
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Realiza o teste k vezes
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # a^d % n
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

def generate_large_prime(bit_length=64):
    """
    Gera um número primo aleatório com o número de bits especificado.
    """
    while True:
        candidate = random.getrandbits(bit_length) | 1  # Garante que seja ímpar
        if is_prime(candidate):
            return candidate
