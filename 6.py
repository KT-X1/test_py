x = [1, 2, 2, 3, 4, 4, 5]
y = []
for z in x:
    if z not in y:
        y.append(z)
print("入力:", x)
print("出力:", y)