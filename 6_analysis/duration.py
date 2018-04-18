import json
import time
from pprint import pprint

#----------Read Json File
def getListFromFile(filename):
	with open(filename) as data_file:
		listData = json.load(data_file)

	return listData;

def getDuration():
	list_conv = getListFromFile("../files/conv_obj_all_c.txt")
	id_num_conv = []
	for i in range(0,94):
		id_num_conv.append(i)
	
	#0=5min, 1=15min, 2=0.5h, 3=1h, 4=>2h, 5=>3h, 6=>6h, 7=>12h, 8=>1day, 9=>1w
	l_count_duration = []
	for i in range(0,11):
		l_count_duration.append(0)
	
	l_count_conv = []
	for i in range(0,93):
		l_count_conv.append(0)
	
	w, h = 11,93;
	l_conv_duration = [[0 for x in range(w)] for y in range(h)]

	i = 0
	for data in list_conv["conv"]:
		for d in data["conversation"]:
			n = d["count"]
			if n>1:
				i+=1			
				t_list = []
				for c in d["data"]:				
					c_time = c["time"]
					t_list.append(c_time)					
					t = time.gmtime(float(c["time"]))
				t_min = float(min(t_list))
				t_max = float(max(t_list))				
				duration = t_max - t_min			
				minutes, seconds = divmod(duration, 60)
				#print n, n-2
				if minutes<=5:
					l_count_duration[0]+=1
					l_conv_duration[n-2][0]+=1
				elif minutes>5 and minutes<=15:
					l_count_duration[1]+=1
					l_conv_duration[n-2][1]+=1
				elif minutes>15 and minutes<=30:
					l_count_duration[2]+=1
					l_conv_duration[n-2][2]+=1
				elif minutes>30 and minutes<=60:
					l_count_duration[3]+=1
					l_conv_duration[n-2][3]+=1
				elif minutes>60 and minutes<=120:
					l_count_duration[4]+=1
					l_conv_duration[n-2][4]+=1
				elif minutes>120 and minutes<=180:
					l_count_duration[5]+=1
					l_conv_duration[n-2][5]+=1
				elif minutes>180 and minutes<=360:
					l_count_duration[6]+=1
					l_conv_duration[n-2][6]+=1
				elif minutes>360 and minutes<=720:
					l_count_duration[7]+=1
					l_conv_duration[n-2][7]+=1
				elif minutes>720 and minutes<=1440:
					l_count_duration[8]+=1
					l_conv_duration[n-2][8]+=1
				elif minutes>1440 and minutes<=10080:
					l_count_duration[9]+=1
					l_conv_duration[n-2][9]+=1
				elif minutes>1080:
					l_count_duration[10]+=1
					l_conv_duration[n-2][10]+=1
				l_count_conv[n-2]+=1
				#print i, n, minutes

	pprint(l_count_duration)
	pprint(l_conv_duration)
	pprint(l_count_conv)

if __name__ == '__main__':
	getDuration()