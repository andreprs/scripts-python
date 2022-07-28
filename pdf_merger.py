import os
import PyPDF2
import sys


def merge_files(path) -> None:
    '''
    Faz a junção do arquivos PDF que existem na pasta informada.
    
        Parameters:
            path (str): Caminho completo da pasta onde os arquivos PDF estão (arquivos que precisam ser mesclados)
    '''
    
    new_pdf = PyPDF2.PdfFileMerger()
    count = 0
    
    for item in os.listdir(path):
        if 'merged' in item:
            count += 1
            
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            _, extension = os.path.splitext(file)
            
            if extension.lower() in '.pdf' and 'merged' not in file:  # ignorando arquvios que tenham 'merged' no nome
                pdf_file = open(full_path, 'rb')
                new_pdf.append(pdf_file)

    if count == 0:
        with open(f'{path}\merged_files.pdf', 'wb') as new_file:
            new_pdf.write(new_file)

    else:
        with open(f'{path}\merged_files({count + 1}).pdf', 'wb') as new_file:  # não sobrescreve o arquivo já existente
            new_pdf.write(new_file)


if __name__ == '__main__':
    argument = sys.argv
    number_of_arguments = len(argument)

    if number_of_arguments <= 1:
        print('\nFaltando argumento: informe o caminho completo dos arquivos.')
        sys.exit()
        
    elif number_of_arguments > 2:
        print('\nMuitos argumentos: passe somente um caminho completo para os arquivos.')
        sys.exit()

    FILES_PATH = argument[1]  # caminho da pasta onde os arquivos pdf estão
    path_exists = os.path.exists(FILES_PATH)

    if path_exists:
        merge_files(FILES_PATH)
        print(f'\nPDF gerado com sucesso no em: {FILES_PATH}')
    else:
        print('\nO caminho informado não existe. Informe o caminho correto.')
        sys.exit()
