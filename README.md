#some common practice to refer
#example
num = 9996

s = [int(digit) for digit in str(num)]
print(s)
result_string = "".join(map(str, s))
print(result_string)
a=[1,2,3,4]
a="".join(map(str,a))
print(a)
