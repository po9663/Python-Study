sample = "abcABCdEFaBCDeFAbC"
s1 = "abc"
s2 = sample.lower()
s3 = s2.find(s1)
s4 = s2.count(s1)
s5 = "def"
s6 = s2.find(s5)
s7 = s2.count(s5)
print("abc문자열 : %d 인덱스, %d 번 존재"%(s3,s4))
print("def문자열 : %d 인덱스, %d 번 존재"%(s6,s7))
