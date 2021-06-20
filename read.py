data = []
counts = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		counts += 1
		if counts % 1000 == 0:
			print(len(data))
	print(len(data))
print('file read done, total ', len(data), 'data')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('average is', sum_len/len(data))



