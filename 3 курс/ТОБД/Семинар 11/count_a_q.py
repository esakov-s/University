from collections import Counter

def count_a_q(file, queue):
    with open(file) as fp:
        text = fp.read().lower()
    res = Counter(text)["a"]
    print(file, res)
    queue.put(res)
