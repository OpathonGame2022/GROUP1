import hashlib
group = "GROUP1"
S1 = group
S2 = hashlib.md5(S1.encode(encoding='UTF-8')).hexdigest()

md5_32 = S2
md5_16 = md5_32[8:24]
print("md5_32:",md5_32)
print("md5_16:",md5_16)