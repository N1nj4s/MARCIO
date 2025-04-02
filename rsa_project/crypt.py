import json

def encrypt_message(message, public_key):
    """
    Criptografa uma mensagem usando a chave pública RSA.
    """
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def save_encrypted_message(encrypted_message, filename="mensagem.cript"):
    """
    Salva a mensagem criptografada em um arquivo.
    """
    with open(filename, "w") as file:
        json.dump(encrypted_message, file)

if __name__ == "__main__":
    public_key = (65537, 3233)  # Exemplo de chave pública
    message = input("Digite a mensagem para criptografar: ")
    encrypted = encrypt_message(message, public_key)
    save_encrypted_message(encrypted)
    print("Mensagem criptografada salva em mensagem.cript")
