import os
import subprocess
import re


def read_all_pdfs(path):
    result = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                print('--------------------------------------------------------------------------------------')
                file_path = os.path.join(root, file)
                abspath = os.path.abspath(file_path)
                process = subprocess.Popen(['pdf2txt.py', abspath],
                                           universal_newlines=True,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                stdout = process.communicate()[0]
                text = stdout.replace("\n", " ")
                text = text.replace("\t", " ")
                text = re.sub(' +', ' ', text)

                palavras = text.split()

                contagem = {}

                for palavra in palavras:
                    contagem[palavra] = 0

                for palavra in palavras:
                    if palavra not in ['de', 'o', '.', 'para', 'um', 'uma', 'em', 'dos', 'da', 'com', 'a', ',', 'que', '-', '–',  'e', 'você', 'do']:
                        contagem[palavra] += 1

                maior = 0
                chave = ""

                for palavra in palavras:
                    if contagem[palavra] > maior:
                        maior = contagem[palavra]
                        chave = palavra

                print(chave + " = " + str(maior))

                print(len(palavras))
