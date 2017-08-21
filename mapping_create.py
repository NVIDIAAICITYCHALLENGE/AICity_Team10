f=open('/data/team10/datasets/aic480-darknet/val/val.txt','r')
e=open('mapping_480valgl.txt','w')
for i,j in enumerate(f.readlines()):
	a=j.strip().split('/')
	#b=a[6]
	b=a[7]
	for l in b:
		e.write(l)
	e.writelines('\n')
