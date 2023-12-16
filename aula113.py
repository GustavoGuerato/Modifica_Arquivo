import os
import shutil

caminho_original = r'C:\Users\NOTE\Downloads\Telegram Desktop'
caminho_novo = r'C:\Users\NOTE\Downloads\Teste'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_filepath = os.path.join(root, file)
        new_filepath = os.path.join(caminho_novo, file)

        if '.jpg' in file:
            shutil.copy(old_filepath, new_filepath)
            print(f'Arquivo {file} Copiado com sucesso')
        if '.jpg' in file:
            os.remove(new_filepath)
            print(f'Arquivo {file} Removido com sucesso')
