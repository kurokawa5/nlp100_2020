# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
text_p = "パトカー"
text_t = "タクシー"

ans = ""
for i in range(len(text_p)):
    ans += text_p[i] + text_t[i]

print(ans)