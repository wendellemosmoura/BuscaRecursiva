import os

arquivos = []
for root, dirnames, filenames in os.walk(r'D:\Músicas'):
    for filename in filenames:
        if filename.__contains__("ABBA") and filename.endswith('mp3'):
            arquivos.append(os.path.join(root, filename))
for arquivo in arquivos:
    print(arquivo)
print(f'Foram encontrados {len(arquivos)} arquivos')
