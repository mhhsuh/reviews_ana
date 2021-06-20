data = []
counts = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		counts += 1
		if counts % 10000 == 0:
			print(len(data))
	print(len(data))
print('file read done, total ', len(data), 'data')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('average is', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
#	print(good)
print('total', len(d), 'message include good')
print(good[0])
