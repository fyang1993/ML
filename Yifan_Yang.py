import json
import sys
f = open('lax.json')
lax = json.load(f)


#define the input function
command_in= []
command = sys.argv[1]
command_in = command.split(' ')

#change all of the string in input command into lower case
command_in_new = []
for i in command_in:
	command_in_new.append(i.lower())
#print command_in_new


#change the time into right version and change the people number into int
time = []
number = 0
for i in range(0,len(lax["data"])):
	time = lax["data"][i][9]
	time = time.split('-')
	number = int(lax["data"][i][13])
	lax["data"][i][9] = time[0]
	lax["data"][i][13] = number
#print lax["data"][0]


#all the possible command elements
command_terminal_list = ['t1','t2','t3','t4','t5','t6','tbi']
#define dictionary
command_terminal_list_d = {"t1" : "Terminal 1","t2" : "Terminal 2","t3" : "Terminal 3","t4" : "Terminal 4","t5" : "Terminal 5","t6" : "Terminal 6","tbi" : "Tom Bradley International Terminal",}

command_time_list = ['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016']

command_type_list = ['arrival','depature']
#define dictionary
command_type_list_d = {"arrival" : "Arrival","depature" : "Depature"}

#verify which command elements are in the actual input command 
flage = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,len(lax["data"])):
	for n in command_in_new:
		if n in command_terminal_list:
			if n == "t1":
				flage[0] = 1
			elif n == "t2":
				flage[1] = 1
			elif n == "t3":
				flage[2] = 1
			elif n == "t4":
				flage[3] = 1
			elif n == "t5":
				flage[4] = 1
			elif n == "t6":
				flage[5] = 1
			elif n == "tbi":
				flage[6] = 1
		elif n in command_time_list:
			if n == "2006":
				flage[7] = 1
			elif n == "2007":
				flage[8] = 1
			elif n == "2008":
				flage[9] = 1
			elif n == "2009":
				flage[10] = 1
			elif n == "2010":
				flage[11] = 1
			elif n == "2011":
				flage[12] = 1
			elif n == "2012":
				flage[13] = 1
			elif n == "2013":
				flage[14] = 1
			elif n == "2014":
				flage[15] = 1
			elif n == "2015":
				flage[16] = 1
			elif n == "2016":
				flage[17] = 1
		elif n in command_type_list:
			if n == "arrival":
				flage[18] = 1
			elif n == "depature":
				flage[19] = 1
		else:
			print ("wrong command")
			break
#print flage

#loop in lax file to find the actual numbers
data_loop_1 = []
data_loop_2 = []
data_loop_3 = []
sum_all = 0
sum1 = 0
sum2 = 0
sum3 = 0
#loop to find terminal
for h in range(0,7):
	sum1 += flage[h]
if sum1 > 0:
	for n in range(0,7):
	    if flage[n] == 1:
		    for i in range(0,len(lax["data"])):
			    if lax["data"][i][10]==command_terminal_list_d[command_terminal_list[n]]:
			    	data_loop_1.append(lax["data"][i])
else:
	data_loop_1 = lax["data"]
#print len(data_loop_1)

#loop to find years
for a in range(7,18):
	sum2 += flage[a]
if sum2 > 0:
	for m in range(7,18):
		if flage[m] == 1:
			for l in range(0,len(data_loop_1)):
				if data_loop_1[l][9] == command_time_list[m-7]:
					data_loop_2.append(data_loop_1[l])
else:
	data_loop_2 = data_loop_1
#print len(data_loop_2)

#loop to find arrival or depature
for b in range(18,20):
	sum3 += flage[b]
if sum3 > 0:
	for k in range(18,20):
		if flage[k] == 1:
			for j in range(0,len(data_loop_2)):
				if data_loop_2[j][11] == command_type_list_d[command_type_list[k-18]]:
					data_loop_3.append(data_loop_2[j])
else:
	data_loop_3 = data_loop_2
#print len(data_loop_3)

for c in data_loop_3:
	sum_all += c[13]
print sum_all




				
				





			













