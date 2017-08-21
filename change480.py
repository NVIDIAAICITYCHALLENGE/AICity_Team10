import os
import copy
dir_new="//workspace//result//480//results_480_new_valgl"
f=open('/data/team10/480valgl.txt','r')
with open('mapping_480valgl.txt','r') as k:
	path_filename={}
	for i,j in enumerate(k.readlines()):
		j=j.replace(".jpg",'')
		j=j.strip().split()
		ii=str(i+1)
		path_filename[ii]=" ".join(j[0:])
for i,j in enumerate(f.readlines()):
	a=j.strip().split()
	b=[]
	b=copy.deepcopy(a)
	b[5]=b[2]
	del b[6]
	count=a[0]
	filecount=path_filename.get(count)
	filename=filecount+".txt"
	e=open(dir_new+"//"+filename,'a')
	if a[1]=='2':
		b[0]='Car'
	elif a[1]=='3':
		b[0]='SUV'
	elif a[1]=='4':
		b[0]='SmallTruck'
	elif a[1]=='5':
		b[0]='MediumTruck'
	elif a[1]=='6':
		b[0]='LargeTruck'
	elif a[1]=='7':
		b[0]='Pedestrian'
	elif a[1]=='8':
		b[0]='Bus'
	elif a[1]=='9':
		b[0]='Van'
	elif a[1]=='10':
		b[0]='GroupOfPeople'
	elif a[1]=='11':
		b[0]='Bicycle'
	elif a[1]=='12':
		b[0]='Motorcycle'
	elif a[1]=='13':
		b[0]='TrafficSignal-Green'
	elif a[1]=='14':
		b[0]='TrafficSignal-Yellow'
	elif a[1]=='15':
		b[0]='TrafficSignal-Red'
	else: b[0]='DontCare'
	b[1]=int(float(a[3])) #xmin
	b1=int(b[1])
	if b1<0:
		b1=0
	elif b1>720:
		b1=720
	b[1]=str(b1)
	b[2]=int(float(a[4])) #ymin
	b2=int(b[2])
	if b2<0:
		b2=0
	elif b2>720:
		b2=720
	b[2]=str(b2)
	b[3]=int(float(a[5])) #xmax
	b3=int(b[3])
	if b3<0:
		b3=0
	elif b3>720:
		b3=720
	b[3]=str(b3)
	b[4]=int(float(a[6])) #ymax
	b4=int(b[4])
	if b4<0:
		b4=0
	elif b4>480:
		b4=480
	b[4]=str(b4)
	if b1>b3:
		continue
	if b2>b4:
		continue
	for l in b:
		e.write(l)
		e.write(' ')
	e.writelines('\n')
