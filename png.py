for i in range(2,1000):
	j=2
	while(j<=i):
		if(i==2 or i==3):
			print(i)
			break
		elif(i%j==0):
			break
		else:
			j=j+1
			if(j==i-1):
				print(i)