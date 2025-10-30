def corporativo_email(email: str, dominio: str = "empresa.pt") -> bool:
    """
    Verifica se o email pertence ao domínio corporativo.
    :param email: Endereço de email a validar.
    :param dominio: Domínio corporativo padrão (empresa.pt)
    :return: True se o email for corporativo, False caso contrário.
    """
    return email.endswith(f"@{dominio}")
