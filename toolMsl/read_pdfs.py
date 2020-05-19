import os
import subprocess
import re

from toolMsl.utils.excluded_words import excluded_words


class PdfReader:

    def __init__(self):
        self.files_count = 0
        self.total_count = 0
        self.words_count = {}
        self.excluded_words = excluded_words

    def read_all_pdfs(self, path):
        result = {}
        for root, dirs, files in os.walk(path):  # iterating folders
            for file in files:  # iterating files in a folder
                if file.endswith(".pdf"):
                    if self.files_count == 5:
                        break
                    self.files_count += 1
                    print(self.files_count)
                    file_path = os.path.join(root, file)
                    abspath = os.path.abspath(file_path)
                    process = subprocess.Popen(['pdf2txt.py', abspath],
                                               universal_newlines=True,
                                               stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                    stdout = process.communicate()[0]
                    # text pre processing
                    text = stdout.replace("\n", " ")
                    text = text.replace("\t", " ")
                    text = re.sub(' +', ' ', text)
                    text = text.lower()
                    # text = text.encode("ascii", "ignore")

                    palavras = text.split()

                    for palavra in palavras:
                        if not self.has_numbers(palavra):
                            self.words_count[palavra] = 0

                    for palavra in palavras:
                        if palavra not in self.excluded_words:
                            if not self.has_numbers(palavra):
                                self.words_count[palavra] += 1
                                self.total_count += 1

                    maior = 0
                    chave = ""

                    for palavra in palavras:
                        if not self.has_numbers(palavra):
                            if self.words_count[palavra] > maior:
                                maior = self.words_count[palavra]
                                chave = palavra

    def has_numbers(self, inputString):
        return bool(re.search(r'\d', inputString))