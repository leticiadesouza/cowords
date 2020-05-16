import re
import subprocess

process = subprocess.Popen(['pdf2txt.py', 'Zotero_Tutorial.pdf'],
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
    contagem[palavra] += 1

maior = 0
chave = ""

for palavra in palavras:
    if contagem[palavra] > maior:
        maior = contagem[palavra]
        chave = palavra

print(chave+ " = " + str(maior))

print(len(palavras))