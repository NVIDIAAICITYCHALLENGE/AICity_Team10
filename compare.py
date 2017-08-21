import os
e=open('butong_480glval.txt','w')
def os_walker(folder):
	path=os.path.abspath(folder)
	for root,dirs,files in os.walk(path):
		if dirs:
			continue
	for f in files:
		yield f, os.path.abspath(os.path.join(root,f))
def compare(f1,f2):
	f1_list={f:p for f,p in os_walker(f1)}
	f2_list={f:p for f,p in os_walker(f2)}
	common={_:f1_list[_] for _ in f1_list if _ in f2_list}
	#print "common: ", common
	f1_specific={_:f1_list[_] for _ in f1_list if _ not in f2_list}
	for l in f1_specific:
        	e.write(l)
		e.writelines('\n')
	f2_specific={_:f2_list[_] for _ in f2_list if _ not in f1_list}
	#print "f2_specific", f2_specific
compare("/datasets/aic480/val/labels","/workspace/result/480/results_480_new_valgl")
