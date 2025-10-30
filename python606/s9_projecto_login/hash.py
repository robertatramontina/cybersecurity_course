import hashlib

def hash_password(password: str) -> str:
    """
    Devolve o hash SHA-256 da password recebida.
    :param pwd: Password em texto simples.
    :return: Hash SHA-256 da password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(password: str, password_hash: str) -> bool:
    """
    Verifica se a password corresponde ao hash fornecido.
    :param pwd: Password em texto simples.
    :param pwd_hash: Hash SHA-256 armazenado.
    :return: True se coincidir, False caso contrário.
    """
    return hashlib.sha256(password.encode()).hexdigest() == password_hash
