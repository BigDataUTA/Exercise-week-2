import sklearn
from numpy import *
from sklearn.linear_model import Perceptron
f = open("vertigo_train.txt","rU")
fp = open("vertigo_predict.txt","rU")
fa = open("vertigo_answers.txt","rU")
x = f.read()
y = fp.read()
z = fa.read()
x = x + ' '
l_data = []
temp = []
l_class = []
count = 0
t_data = []
t_class = []
for i in y:
	i=i.replace('\n',' ')
	for a in i:
		if a != '' and a != ' ':
			if count <5:
				temp.append(int(a))
				count += 1
			if count == 5:
				t_data.append(temp)
				count = 0
				temp =[]
				break

for i in z:
	i=i.replace('\n',' ')
	if i != '' and i != ' ':
		t_class.append(int(i))
for i in x:
	i=i.replace('\n',' ')
	for a in i:
		if a != '' and a != ' ':
			if count == 0:
				l_class.append(int(a))
				count += 1
			elif count <6:
				temp.append(int(a))
				count += 1
			if count == 6:
				l_data.append(temp)
				temp = []
				count = 0
				break
p1 = Perceptron()
p1.fit(l_data,l_class)
answer1 = p1.predict(t_data)
answer2 =[]
neighbor = 0
for i in answer1:
	if i != '' and i != ' ':
		answer2.append(i)
c = 0.0
for i in range(len(t_class)):
	if t_class[i] == answer2[i]:
		c += 1
print "Perceptron: %s %% correct" % str(c/len(t_class)*100)


'''Nearest naighbor'''
def distance(t1,t2):
	d = 0
	for i in range(len(t1)):
		d += abs(t1[i]-t2[i])
	return d

answer3 = []
for i in range(len(t_class)):
	temp_d= []
	s_index = []
	for m in l_data:
		temp_d.append(distance(t_data[i],m))
	ss = array(temp_d)
	sortedindex = ss.argsort()
	for aaa in sortedindex:
		if aaa != '' and aaa != ' ':
			s_index.append(aaa)
	least_d = temp_d[s_index[0]]
	k = least_d
	h = 0
	while k <= least_d:
		classcount = {}
		voteclass = l_class[s_index[h]]
		classcount[voteclass] = classcount.get(voteclass,0) + 1
		h = h+ 1
		k = int(temp_d[s_index[h]])
		
	maxcount = 0
	for key, value in classcount.items():
		if value > maxcount:
			maxcount = value
			maxindex = key
	answer3.append(maxindex)
co = 0.0
for i in range(len(t_class)):
	if t_class[i] == answer3[i]:
		co += 1
print "Nearest neighbor: %s %% correct" % str(co/len(t_class)*100)
f.close()
fp.close()
fa.close()