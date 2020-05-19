import json
import re

class ResultSerializer:
    def word_cloud_export(self, words):
        words_list = []
        all_words = []
        result = ''
        for key in words:
            result = result+str(key)+' '

            all_words.append(key)
        i = 0
        for key in words:
            words_list.append({"text": key, "value": words[key]})
            i += 1
            if i == 250:
                break
        with open('data.json', 'w') as outfile:
            json.dump(result, outfile)

        # with open('words.json', 'w') as outfile:
        #     json.dump(all_words, outfile)



