from rsa_keygen import generate_rsa_keys
from rsa_file_manager import save_keys, load_key
from crypt import encrypt_message, save_encrypted_message
from rsa_decrypt import decrypt_message, load_encrypted_message

def main():
    while True:
        print("\n==== Sistema RSA ====")
        print("1. Gerar chaves RSA")
        print("2. Criptografar mensagem")
        print("3. Decriptografar mensagem")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            public_key, private_key = generate_rsa_keys()
            save_keys(public_key, private_key)
            print("Chaves RSA geradas e salvas com sucesso!")
        
        elif escolha == "2":
            public_key = load_key("chave_publica.cpa")
            message = input("Digite a mensagem para criptografar: ")
            encrypted = encrypt_message(message, public_key)
            save_encrypted_message(encrypted)
            print("Mensagem criptografada e salva em 'mensagem.cript'.")
        
        elif escolha == "3":
            private_key = load_key("chave_privada.csa")
            encrypted_message = load_encrypted_message()
            decrypted = decrypt_message(encrypted_message, private_key)
            print("Mensagem decriptografada:", decrypted)
        
        elif escolha == "4":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
