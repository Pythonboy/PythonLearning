import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re

class InformationDrawer(object):
	def __init__(self,filename):
		self.file_ = filename;
		self.file_list = os.listdir(filename);
	
	def Print_file(self):
		print(self.file_list);
		
	def Draw(self):
		plt.figure(figsize = (10,10));
		for name in self.file_list:
			t = name;
			name= self.file + "/" + name;
			data = np.loadtxt(name,skiprows = 1);
			plt.plot(data[:,1],data[:,2],label = t);
		plt.legend();
		plt.show();
	
	def Draw_Intense(self,Re,hour,title,left=0,right=3000,Y_lim=False):
		num = [];
		Max = [];
		print(self.file_list);
		for name in self.file_list:
			t = re.findall(Re,name);
			try:
				num.append(int(t[0]));
			except:
				continue;
		num.sort();
		print(num);
		plt.figure(figsize = (10,10));
		for name in num:
			t = hour+str(name)+"min";
			name = self.file_ + "/"+ t + ".txt";
			data = np.loadtxt(name,skiprows = 1);
			M = np.max(data[:,2],axis = 0);
			Max.append(M);
		print(Max);
		plt.scatter(num,Max,s = 180);
		plt.title(title,fontproperties = "SimHei",fontsize = 20);
		if Y_lim == True:
			plt.ylim([left,right]);
		plt.show();
		
		
		return num,Max;