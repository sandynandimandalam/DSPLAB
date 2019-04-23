year=input('enter year=')
if(year%400==0):
 print year,'is a leap year'
elif(year%4==0):
      if(year%100!=0):
           print year,'is a leap year'
      else:
           print 'not a leap year'
else:
      print 'not a leap year'