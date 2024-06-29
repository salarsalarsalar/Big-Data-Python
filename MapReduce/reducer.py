#!/usr/bin/python

import sys
import operator

#user_id , latitude , longitude , city, category
list1=[]
list2=[]
lista=[]
listb=[]
current_user=None
current_city=None
latitude=0
longitude=0
category=0


similarity=0
count=0
def get_jaccard_sim(str1, str2): 
    a = set(str1.split()) 
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
'''
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float(intersection) / union
''' 
for line in sys.stdin:
	#print(line)
	
		
	thisUser,thislatitude,thislongitude,thiscity,thiscategory=line
	'''
	try:
       	 lattitude= int(lattitude)
       	 longitude= int(longitude)
       	 lattitude=round(lattitude,2)
       	 longitude=round(longitude,2)
    	except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
        '''
	if  thisUser != current_user and thisUser != None:
		#list1.append(thisUser,thislatitude,thislongitude,thiscity,thiscategory)
		#list2.append(current_user,latitude,longitude,current_city,category)
		if lattitude==thislattitude and longitude==thislongitude:	
				#similarity=
				
				
			
			#print ("{0}\t{1}\t{2}\t{3}\t{4}".format(current_user,current_city,latitude,longitude,category))
				count+=1
			
  	a = set(thisUser,thislatitude,thislongitude,thiscity,thiscategory) 
   	b = set(latitude,longitude,current_city,category)
        c = a.intersection(b)
        d=float(len(c)) / (len(a) + len(b) - len(c))
	print(d)

	current_user=thisUser
	current_city=city
	lattitude=thislattitude
	longitude=thislongitude
	category=thiscategory
	
#for line in sys.stdin:

	
		
		
	
		
		
		
