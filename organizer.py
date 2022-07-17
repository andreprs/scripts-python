import os
import shutil

USER = os.getlogin()
DOWNLOAD_FOLDER = f'C:\\Users\\{USER}\\Downloads'
FOLDERS = ['Imagens', 'Videos', 'Docs', 'Compactados', 'Dev', 'Executaveis']
EXTENSIONS = {
    'imagens': ['.jpg', '.jpeg', '.png', '.gif', '.img', '.psd', '.tga', '.tif',
                '.tiff', '.msp', '.pic', '.pbm', '.bmp', '.ico', '.raw', '.pcx',
                '.svg'],

    'videos': ['.mp4', '.mov', '.wmv', '.avi', '.mpeg', '.webm', '.mkv', '.m4v'],
    
    'docs': ['.pdf', '.txt', '.doc', '.docx', '.ppt', '.xls', '.odt', '.csv',
             '.log', 'wpd', '.xlsx', '.md', '.tex'],
    
    'compactados': ['.zip', '.tar', '.rar', '.tar.gz', '.7z', '.gz', '.iso'],
    
    'dev': ['.py', '.css', '.js', '.json', '.c', '.cc', '.cs', '.java', '.go',
            '.r', '.R', '.rb', '.pl', '.html', '.sh'],
    
    'executaveis': ['.apk', '.exe', '.msi', '.bat', '.bin', '.jar']
}


def criar_pastas():
    print('Criando pastas necessárias...')
    for folder in FOLDERS:
        try:
            os.mkdir(f'{DOWNLOAD_FOLDER}\\{folder}')
            print(f'{DOWNLOAD_FOLDER}\\{folder} criada com sucesso!')
        except FileExistsError:
            print(f'Pasta {DOWNLOAD_FOLDER}\\{folder} já existe.')


def mover_arquivos():
    for root, dirs, files in os.walk(DOWNLOAD_FOLDER):
        for file in files:
            full_path = f'{root}\\{file}'
            _, extension = os.path.splitext(file)
            
            for key in EXTENSIONS:
                if extension in EXTENSIONS[key]:
                    new_path = f'{DOWNLOAD_FOLDER}\\{key.capitalize()}'
                    
                    try:
                        shutil.move(full_path, new_path)
                        continue
                    
                    except Exception as erro:
                        pass
                
    print('\nArquivos movidos com sucesso!')


def apagar_pastas():
    for root, dirs, files in os.walk(DOWNLOAD_FOLDER):
        for dir in dirs:
            caminho = f'{DOWNLOAD_FOLDER}\\{dir}'
            
            if dir not in FOLDERS and len(os.listdir(caminho)) == 0:
                os.rmdir(caminho)
    
    print('\nPastas desnecessárias excluídas!')


criar_pastas()
mover_arquivos()
apagar_pastas()
print('\nOrganização completa!')