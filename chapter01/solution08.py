"""
Implement a function cipher that converts a given string with the specification:

 - Every alphabetical lowercase letter c is converted to a letter whose ASCII code is (219 - [the ASCII code of c])
 - Keep other letters unchanged

Use this function to cipher and decipher an English message.
"""
def cipher(s: str) -> str:
    # 変換後の文字列を格納する変数
    result = ""
    # 文字列 s の各文字を処理する
    for c in s:
        # 英小文字の場合は変換する
        if c.islower():
            result += chr(219 - ord(c))
        # その他の文字はそのまま出力する
        else:
            result += c
    return result

# 暗号化
encrypted = cipher("Hello, World!")
print(encrypted)  # => Hvww, Dqgry!

# 復号化
decrypted = cipher(encrypted)
print(decrypted)  # => Hello, World!
