x = input("入力: ")
y = 0
for z in x.lower():
    if z in 'aeiou':
        y += 1
print("出力: 母音数:",y)
