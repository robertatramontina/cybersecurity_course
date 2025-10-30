from typing import Dict
from dados_teste import registos
from analise_teste import contar_falhas_por_ip
from relatorio_teste import gerar_relatorio

def main() -> None:
    contagem = contar_falhas_por_ip(registos)
    gerar_relatorio(contagem)

"""
A função main engloba e chama as demais função
a serem executadas na ordem desejada.
"""

if __name__ == "__main__":
    main()