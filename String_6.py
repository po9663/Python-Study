a = 10
print("{} {}\n".format(a,type(a)))

b= 5**(1/2)
print("5의 루트값은: {:8.5f}\n".format(b))

c = "hello"
q = c[::-1]
print(c[::2])
print(c[::-1])
print(q[3:5:]) 
print(c[2:5:])
print("\n")

d = 80.3
e = 95.7
f = 73.2
g = d+e+f
h = g/3
print("과목    점수")
print("------------")
print("국어: {:6.2f}".format(d))
print("영어: {:6.2f}".format(e))
print("수학: {:6.2f}".format(f))
print("총점: {:6.2f}".format(g))
print("평균: {:8.4f}\n".format(h))

i = "These_functions_cannot_be_used_with_complex_numbers."
j =  i.replace("_"," ")
k = "a"
l = "e"
m = "u"
n = " "
print("원래문장: {}".format(i))
print("수정한 문장: {}".format(j))
print("a는 %d번 나왔다."%i.count(k))
print("e는 %d번 나왔다."%i.count(l))
print("u는 %d번 나왔다."%i.count(m))
print("space는 %d번 나왔다."%j.count(n))
print("모두 대문자로 바꾸면: {}".format(j.upper()))

