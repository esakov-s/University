from collections import Counter

def count_a(file):
    with open(file) as fp:
        text = fp.read().lower()
    res = Counter(text)["a"]
    print(file, res)
    return res
