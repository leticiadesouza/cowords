import click
import re
import subprocess

from toolMsl.read_pdfs import read_all_pdfs


@click.command()
@click.argument('path')
@click.option('-r', is_flag=True, help="Recursive execution to many files")
def init(path, r):
    if r:
        print("Executando muitos arquivos de maneira recursiva")
        read_all_pdfs(path)
    else:
        process = subprocess.Popen(['pdf2txt.py', path],
                                   universal_newlines=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        stdout = process.communicate()[0]
        text = stdout.replace("\n", " ")
        text = text.replace("\t", " ")
        text = re.sub(' +', ' ', text)
        text = text.lower()
        palavras = text.split()

        contagem = {}

        for palavra in palavras:
            contagem[palavra] = 0

        for palavra in palavras:
            if palavra not in ['de', 'na', 'no', 'as', 'o', 'os', '.', 'para', 'um', 'uma', 'em', 'dos', 'da', 'com', 'a', ',', 'que', '-', '–',
                               'e', 'você', 'do']:
                contagem[palavra] += 1

        maior = 0
        chave = ""

        sorted_words = {k: v for k, v in sorted(contagem.items(), key=lambda item: item[1])}
        i=1
        for key in sorted_words:
            if sorted_words[key] > 10:
                print(f'{i} - {key}: {sorted_words[key]}')
                i+=1
        # for palavra in palavras:
        #     if contagem[palavra] > maior:
        #         maior = contagem[palavra]
        #         chave = palavra
        #
        # print(chave+ " = " + str(maior))

        print(len(palavras))