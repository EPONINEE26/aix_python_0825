a = '1,123만원'
print(a[:-1])
print(a[:-2])
print(a[:-1])
print(a[-2:])
print(a[-1])
a_int = int(a[:-2].replace(",",""))
print(a_int)