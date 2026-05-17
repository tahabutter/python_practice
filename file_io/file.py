f = open("sample.txt", "r+")
res = f.write("Hey there")
print(res)  # 6
f.close()