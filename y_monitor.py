#import requests_html  - no work with list of liked videos but right work with others lists
from selenium import webdriver
import time
from bs4 import BeautifulSoup 

"""
chrome_opt = webdriver.ChromeOptions()
#chrome_opt.add_experimental_option('useAutomationExtension', False)
#chrome_opt.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_opt.add_argument('--disable-gpu')
dv_path = 'D:\\geckodriver.exe'
dv= webdriver.Chrome(executable_path=dv_path, chrome_options=chrome_opt)
dv.get('https://www.youtube.com/')
"""

def position():
	pass
	
def log():
	pass

def scrolling():
	pass

def getData():
	with open('test.txt', 'r', encoding='utf-16') as t:
		r_text = t.read()
		return r_text

def analise_data(html):
	soup = BeautifulSoup(html, 'html.parser')
	tags=soup('a')
	c=0
	d={}

	def filter(): # filter for atributtes and values that indicate that is correct tag 'span' 
		score=0 
		title=0 
		id_=0

		if j.get('title') and j.get('title') is not None:
			title=1
		if j.get('id') and j.get('id') == "video-title":
			id_=1
		score = title + id_  # computing score

		if score == 2: return True  # if score is 2, this mean that the tag aproves all filters required for be valid

	for i in tags: # find all tags "a' that have inside the tags 'span' and save every container 'a' in the var "i"  
		for j in i.find_all('span'): # find all tags 'span' in every container "i"
			if filter() == True: # condition that verify result that retutn the filter function
				d[c]=j.get_text().strip() # add in the dictionary
				c+=1

	return d			

def save(dic_f='', opt=False, dic_m=''):
	if opt == False:
		cf=open('new_list.txt', 'w', encoding='utf-16')
		print('Write dictionary:\n')
		for i in dic_f:
			content=dic_f[i]+'\n'
			cf.write(content)
		cf.close()
		print('end..\n')

	if opt == True:	
		cf2=open('miss_list.txt', 'w', encoding='utf-16')
		print('write miss:\n')
		for i in dic_m:
			content2=i+'\n'
			cf2.write(content2)
		cf2.close()
		print('end..\n')	

def comparison(dic):
	miss=[]
	flag=False
	cf=open('new_list.txt', 'r', encoding='utf-16')
	file_r=cf.readlines()
	for i in file_r:
		for j in dic:
			if dic[j].strip() == i.strip():
				flag=True  # if match in any of the iteration of "j" on "i", mean that "i" element (of old list) exist in "dic"(new list)
		if flag == True: 
			flag=False # if "flag" was true and exist, si ignored, so is required change again to false an continue
		else:    # if "flag" variable was keep in false, means that "i" element of old list is missing in the new dict(new list)           
			miss.append(i) # so the element is add in the missing elements list	
		
	return miss



gHtml=getData()
dictionary=analise_data(gHtml)

while 1:

	inp=input('Comparison [1] -- Save New File [2] -- Save Miss File [3]: ')

	if inp=='1':
		print('lista:',comparison(dictionary))
	elif inp == '2':
		save(dic_f=dictionary)
	elif inp == '3':
		save(opt=True,dic_m=comparison(dictionary))
	else:
		exit='exit? [y] '
		if exit=='y' or exit=='Y':  
			break






