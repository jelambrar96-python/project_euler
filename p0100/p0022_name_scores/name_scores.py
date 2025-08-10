from tqdm import tqdm 


def name_scores(list_names):
    suma = 0
    for i, item in tqdm(enumerate(list_names,start=1)):
        score = sum((ord(c) - 64) for c in item)
        suma += (score * i)
    return suma


if __name__ == '__main__':
    data = None
    with open('names.txt') as f:
        data = f.read()
    data = data.replace('"', '').strip().split(",")
    data.sort()
    print(name_scores(data))
