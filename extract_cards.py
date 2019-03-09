import pandas as pd
from pandas.compat import StringIO


class Padlet:
    def __init__(self, data, splitter="~"):
        self.names, self.answers, self.questions = data.split(splitter)
        self.names, self.answers, self.questions = (pd.read_csv(StringIO(col)) for col in self.replacer())

    def replacer(self):
        names = self.names.replace("שם המשחק\n", "", 1)
        answers = self.answers.replace("קלפי תשובות\n", "", 1)
        questions = self.questions.replace("קלפי שאלות\n", "", 1)
        return (names, answers, questions)


def load(path, splitter="~"):
    f = open(path, encoding="utf-8-sig")
    data = f.read()
    f.close()
    return Padlet(data, splitter)
