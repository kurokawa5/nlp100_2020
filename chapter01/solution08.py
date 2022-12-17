"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．

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
