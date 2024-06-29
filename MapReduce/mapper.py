#!/usr/bin/python                                          
import sys                                                                                                
import csv
import regex
reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
prev_lat=0
prev_lon=0
prev_userid=None
prev_city=None
for line in reader: 
    userid, placeid, datetime, lat, lon, city, category=line
    '''#cur_userid, cur_placeid, cur_datetime, cur_lat, cur_lon, cur_city, cur_category=line
    print ("\nNew entry -------------------------------------------------\n\n")
    print ("userid\t{0}".format(userid))
    print ("placeid\t{0}".format(placeid))
    print ("datetime\t{0}".format(datetime))
    print ("lat\t{0}".format(lat))
    print ("lon\t{0}".format(lon))
    print ("city\t{0}".format(city))
    print ("category\t{0}".format(category))
    '''
    # match these categories with category variable
    #Arts,College,Food,Outdoors,Home,Nightlife,Shops,Travel(maybe not!)
  	
    '''
    #if		
	    if min_lat > lat:
	    	min_lat=lat
	    if max_lat < lat:
	    	max_lat=lat
    ''' 
    '''
    if cur_lat!=lat: 
    		cur_lat=lat
    if cur_lon!=lon: #and cur_userid!=userid:
    		cur_lon=lon#;cur_userid=userid
    '''
    #if cur_userid!=prev_userid:
    		#prev_userid=cur_userid;prev_lat=cur_lat;prev_lon=cur_lon;prev_city=cur_city		
    #elif cur_userid==prev_userid:
    print ("{0}\t{1}\t{2}\t{3}".format(userid,lat, lon, city, category))
    #print ("{0}\t{1}\t{2}\t{3}".format(prev_userid,prev_lat, prev_lon, prev_city))
    #prev_userid=cur_userid;prev_lat=cur_lat;prev_lon=cur_lon;prev_city=cur_city
    
   
    		
