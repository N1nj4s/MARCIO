import json

def save_keys(public_key, private_key, public_filename="chave_publica.cpa", private_filename="chave_privada.csa"):
    """
    Salva as chaves pública e privada em arquivos.
    """
    with open(public_filename, "w") as pub_file:
        json.dump(public_key, pub_file)
    
    with open(private_filename, "w") as priv_file:
        json.dump(private_key, priv_file)

def load_key(filename):
    """
    Carrega uma chave RSA de um arquivo.
    """
    with open(filename, "r") as file:
        key = json.load(file)
    return tuple(key)

if __name__ == "__main__":
    public_key = (65537, 3233)  # Exemplo de chave pública
    private_key = (2753, 3233)  # Exemplo de chave privada
    save_keys(public_key, private_key)
    print("Chaves salvas!")
    
    loaded_public_key = load_key("chave_publica.cpa")
    loaded_private_key = load_key("chave_privada.csa")
    print("Chave pública carregada:", loaded_public_key)
    print("Chave privada carregada:", loaded_private_key)
