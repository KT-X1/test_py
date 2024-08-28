def is_palindrome(y):
    y = y.lower().replace(" ", "")
    if y == y[::-1]:
        return "回文です"
    else:
        return "回文ではありません"
x = input("入力:")
print(is_palindrome(x))