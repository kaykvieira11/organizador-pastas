import os
import shutil

# 1. Indica a pasta de teste na area de t rabalho
pasta = os.path.join(os.path.expanduser('~'), 'Desktop', 'BAGUNCINHA')

print(f"Organizando arquivos em: {pasta} \n{'-' * 50}")


# 2. Passa por cada arquivo de dentro da pasta
for arquivo in os.listdir(pasta):
    # Pula se for uma pasta
    caminho_baguncinha = os.path.join(pasta, arquivo)
    if os.path.isdir(caminho_baguncinha):
        continue

    # Separa o nome da extensão
    nome, ext = os.path.splitext(arquivo)
    ext = ext.lower()

    # 3. Define a categoria baseada na extensão
    if ext in ['.pdf', '.txt', '.docx', '.xlsx']:
        nome_pasta = 'Documentos'
    elif ext in ['.jpg', '.jpeg', '.png', '.gif']:
        nome_pasta = 'Imagens'
    elif ext in ['.mp4', '.mkv', '.avi']:
        nome_pasta = 'Videos'
    else:
        nome_pasta = 'Outros'

    # 4. Cria o caminho da pasta de destino e garante que ela existe
    pasta_destino = os.path.join(pasta, nome_pasta)
    os.makedirs(pasta_destino, exist_ok=True)

    # 5. Move o arquivo para a sua nova pasta
    origem = os.path.join(pasta, arquivo)
    destino = os.path.join(pasta_destino, arquivo)
    
    shutil.move(origem, destino)
    print(f"Movido: {arquivo} ---> {nome_pasta}/")

print(f"{'-' * 50}\nOrganizado com sucesso!")

