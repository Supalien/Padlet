import pandas as pd
from pandas.compat import StringIO
import re


class Padlet:
    def __init__(self, data, splitter="~"):
        self.names, self.answers, self.questions = [pd.read_csv(StringIO(col)) for col in data.split(splitter)]
        self.names = [Card(self.names["Subject"][i], self.names["Body"][i]) for i in range(len(self.names))]
        self.answers = [Card(self.answers["Subject"][i], self.answers["Body"][i]) for i in range(len(self.answers))]
        self.questions = [Card(self.questions["Subject"][i], self.questions["Body"][i]) for i in range(len(self.questions))]

    def status(self):
        msg = (
        f"Names: {len(self.names)} Cards.\n"
        f"Answers: {len(self.answers)} Cards.\n"
        f"Questions: {len(self.questions)} Cards.")
        return msg

class Card:
    def __init__(self, author, content):
        self.content = content.replace("<div>", "").replace("</div>", "")\
            .strip()[::-1]
        self.author = self.userlize(author)

    def __repr__(self):
        return f"{self.author}: {self.content}"

    def userlize(self, user):
        if user == "עלום שם": return user
        try:
            user = re.search(r"[uU][\\\/](.+)$", user).group(1)
        except:
            print(user)
        return f"/u/{user}"


def load(path, splitter="~"):
    f = open(path, encoding="utf-8-sig")
    data = f.read()
    f.close()
    return Padlet(data, splitter)
