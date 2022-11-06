import hashlib
name = "XIALIWEI"
S1 = "%s2425"%name
S2 = hashlib.md5(S1.encode(encoding='UTF-8')).hexdigest()

S2_last_letters = S2[-1]
I1 = int(S2_last_letters,16)
I2 = I1+5
I3 = I2%5
I4 = I3+1
print("name:",name)
print("S1:",S1)
print("S2:",S2)
print("S2_last_letters:",S2_last_letters)
print("I1:",I1)
print("I2:",I2)
print("I3:",I3)
print("I4:",I4)

print("Just for fun.")