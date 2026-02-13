import os

def processar_arquivos_mat(diretorio='.'):
    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            if nome_arquivo.startswith('mat_'):
                caminho_arquivo = os.path.join(raiz, nome_arquivo)
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as f:
                        conteudo = f.read()

                    conteudo_modificado = conteudo.replace('.rgba16', '')

                    if conteudo != conteudo_modificado:
                        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                            f.write(conteudo_modificado)
                        print(f"Arquivo modificado: {caminho_arquivo}")
                    else:
                        print(f"Nenhuma mudança: {caminho_arquivo}")

                except Exception as e:
                    print(f"Erro ao processar {caminho_arquivo}: {e}")

def remover_extensao_rgba16(diretorio='.'):
    for raiz, _, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            if nome_arquivo.endswith('.rgba16'):
                caminho_antigo = os.path.join(raiz, nome_arquivo)
                novo_nome = nome_arquivo[:-7]  # Remove ".rgba16"
                caminho_novo = os.path.join(raiz, novo_nome)

                try:
                    os.rename(caminho_antigo, caminho_novo)
                    print(f"Renomeado: {caminho_antigo} -> {caminho_novo}")
                except Exception as e:
                    print(f"Erro ao renomear {caminho_antigo}: {e}")

if __name__ == '__main__':
    processar_arquivos_mat()
    remover_extensao_rgba16()
