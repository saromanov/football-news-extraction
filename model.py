import nltk

class Model:
    def __init__(self, text):
        self.text = text

    def _stopwords(self):
        return nltk.corpus.stopwords.words('english')

    def _tagging(self):
        pass

    def run(self):
        if len(self.text) == 0:
            raise Exception("Text is empty")

        for sent in nltk.sent_tokenize(self.text):
            tokenizer = [word for word in  nltk.RegexpTokenizer(r'\w+').tokenize(sent) \
                        if word not in self._stopwords() or word not in [',', '.', ""]]
            tagging = nltk.pos_tag(tokenizer)
            for chunk in nltk.ne_chunk(tagging):
                print(chunk)