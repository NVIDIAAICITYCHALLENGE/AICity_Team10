import os
path="/workspace/result/480/results_480_new_valgl"
ls=os.listdir(path)
count=0
for i in ls:
	if os.path.isfile(os.path.join(path,i)):
		count+=1
print "file:"+str(count)
