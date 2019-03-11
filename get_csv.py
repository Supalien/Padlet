def get(path="Padlet.csv", splitter="~"):
    import urllib.request as r
    url = "https://padlet.com/padlets/ykw34s1diddu/exports/list.csv"
    r.urlretrieve(url, path)
    make_ready(path, splitter)
    return path


def make_ready(file, splitter):
    f = open(file, encoding="utf-8-sig")
    data = f.read()
    f.close()
    names = "שם המשחק"
    answers = "\"\"\nקלפי תשובות"
    questions = "\"\"\nקלפי שאלות"
    data = data\
    .replace(names, "", 1)\
    .replace(answers, splitter)\
    .replace(questions, splitter)
    f = open(file, "w", encoding="utf-8-sig")
    f.write(data[:-4])
    f.close()
