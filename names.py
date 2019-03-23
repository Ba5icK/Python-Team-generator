#Team generator by Rayan Crasta
import random

#importing team leader names
with open('C:/Users/BaSicK/Desktop/tldr.txt') as f:
    tldr = f.read().splitlines()

#importing team leader names
with open('C:/Users/BaSicK/Desktop/plr.txt') as f1:
    mbr=f1.read().splitlines()

ll=len(tldr)

for i in range(1,ll):
	l1=random.choice(tldr)
	print(l1)
	tldr.remove(str(l1))

	l2=random.choice(mbr)
	print(l2)
	mbr.remove(str(l2))

	l2=random.choice(mbr)
	print(l2)
	mbr.remove(str(l2))

	print('-------------')