import json

def decrypt_message(encrypted_message, private_key):
    """
    Decripta uma mensagem usando a chave privada RSA.
    """
    d, n = private_key
    decrypted_message = ''.join(chr(pow(char, d, n)) for char in encrypted_message)
    return decrypted_message

def load_encrypted_message(filename="mensagem.cript"):
    """
    Carrega a mensagem criptografada de um arquivo.
    """
    with open(filename, "r") as file:
        encrypted_message = json.load(file)
    return encrypted_message

if __name__ == "__main__":
    private_key = (2753, 3233)  # Exemplo de chave privada
    encrypted_message = load_encrypted_message()
    decrypted = decrypt_message(encrypted_message, private_key)
    print("Mensagem decriptografada:", decrypted)
