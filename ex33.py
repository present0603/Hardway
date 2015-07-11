# -*- coding: utf-8 -*-

i = 0
numbers = []

while i < 6:
	print "꼭대기에서 i는 %d" % i
	numbers.append(i)

	i = i + 1
	print "숫자는 이제: ", numbers
	print "바닥에서 i는 %d" % i


print "숫자: "

for num in numbers:
	print num


def test_while(num):
	nums = []
	k = 0
	while k < num:
		nums.append(k)
		k += 1
	return nums

print "****************************"

for j in test_while(10):
	print j