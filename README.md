# O que são esses scripts?
Esses scripts feitos em python servem como parte dos meus estudos 
da linguagem. Neles tento automatizar algumas tarefas ou criar 
funcionalidades. Conforme eu for aprendendo mais e ganhando mais 
experiência irei atulizando os códigos ou postando uma segunda 
versão (isso pode me ajudar a ver minha evolução ao escrever os 
códigos).

## Organizer.py (Organizador)
Esse script faz uma organização da pasta de **Downloads** do usuário
separando os arquivos em pastas de acordo com a extensão dos
arquvios. Além disso as pastas que ficaram vazias ("desnecessárias")
são excluídas.

## Pdf_merger.py (Juntar arquivos PDF)
Esse script junta arquivos PDF que estão na pasta (incluindo subpastas)
do caminho passado como parâmetro. O arquivo gerado terá o nome de 
**merged_files.pdf** (arquivos que tenham *merged* no nome serão ignorados).

Esse script utiliza um módulo que não vem por padrão no python, sendo assim
necessário instalá-lo. É possível insatalar o módulo usando:

```
python -m pip install pypdf2
```

Por padrão a instalação é feita na pasta de em que o python foi instalado.
É recomendável que a instalação seja feita em um ambiente virtual.

### Funcionamento 
A ordem em que os arquivos serão adicionados no arquivo gerado será de
acordo com a classificação de nome do arquivo, ou seja, em ordem alfabética
ou em ordem crescente caso o arquivo tenha número no começo do nome. Sendo
assim, caso uma ordem seja necessário, preste atenção na nomeação dos 
arquivos.