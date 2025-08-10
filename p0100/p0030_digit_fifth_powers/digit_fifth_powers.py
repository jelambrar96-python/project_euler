from tqdm import tqdm


suma = sum(
    i
    for i in tqdm(range(2, 999_999))
    if i == sum(int(d) ** 5 for d in str(i))
)

print(suma) # 194979
