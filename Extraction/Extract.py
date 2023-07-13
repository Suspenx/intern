from collections import defaultdict
import csv
import re
# import nltk
#  nltk.download('punkt')
from nltk import FreqDist, word_tokenize

class Extract:
    def __init__(self) -> None:
        self.labels = ["Gender", "Age", "Address",  "Phone", "Name"]

    def extract_phone_number(self, text=None):
        if text is None:
            return
        
        r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        phone_numbers = r.findall(text)
        return [re.sub(r'\D', '', number) for number in phone_numbers][0]

    def get_data(self, file_path=None)->None:
        docs = []
        if file_path is None:
            return docs
        try:
            with open(file=file_path, mode='r', encoding='utf8') as o_file:
                data = csv.reader(o_file, delimiter=',', quotechar='|')
                for row in data:
                    text = row[0].strip()
                    label= row[1].strip()
                    if label in self.labels:
                            docs.append((text, label))
        except Exception as e:
             print("An error occured when try to get data....")
        return docs

    def clean_text(self, text="", label=""):
         try:
              if text == "" or label == "":
                return
              if len(text) < 3:
                return
            
              cleaned_text = text.strip()

              if label == "Phone":
                  cleaned_text = cleaned_text.replace("+", "")
                  cleaned_text = self.extract_phone_number(text=cleaned_text)
              return cleaned_text


              
         except Exception as e:
              print("An error occured when cleaning data...")
              return []

    def frequency_distribution_test(self, docs=None):
         tokens = defaultdict(list)
         for doc in docs:
              doc_label = doc[1]
              doc_text = doc[0]
              doc_text = self.clean_text(doc_text, label=doc_label)
              if doc_text:
                doc_tokens = word_tokenize(doc_text)
                tokens[doc_label].extend(doc_tokens)

         for category_label, category_tokens, in tokens.items():
              print(category_label)
              fd=FreqDist(category_tokens)
              print(fd.most_common(40))




if __name__ == '__main__':
    extractor = Extract()
    data = extractor.get_data(file_path="data.csv")
    extractor.frequency_distribution_test(docs=data)

