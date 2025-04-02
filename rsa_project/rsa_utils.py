def extended_gcd(a, b):
    """
    Algoritmo de Euclides estendido para encontrar o inverso modular.
    Retorna (gcd, x, y) onde gcd é o maior divisor comum de a e b,
    e x, y são os coeficientes de Bézout, tal que ax + by = gcd.
    """
    if a == 0:
        return b, 0, 1
    else:
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

def mod_inverse(a, m):
    """
    Calcula o inverso modular de a módulo m.
    Retorna x tal que (a * x) % m == 1, ou None se não existir.
    """
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverso modular não existe
    else:
        return x % m
