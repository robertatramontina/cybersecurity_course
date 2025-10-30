from hash import hash_password, check_password
from ip import mask_ip
from email import corporativo_email

def main() -> None:
    """
    Função principal que recolhe os dados e apresenta os resultados.
    """
    password = input("Digite a sua password: ")
    email = input("Digite o seu email: ")
    ip = input("Digite o seu IP: ")

    hashed = hash_password(password)
    corporativo = corporativo_email(email)
    ip_mask = mask_ip(ip)

    print("\n=== RESULTADOS ===")
    print(f"Hash SHA-256: {hashed}")
    print(f"Email corporativo: {corporativo}")
    print(f"IP mascarado: {ip_mask}")

if __name__ == "__main__":
    main()
