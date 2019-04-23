import math
print("\t------------calculator--------------")
def sum(a,b):
	a+=b
	return a
def sub(a,b):
	if a>b:
		a-=b
		return a
	else:
		b-=a
		return b
def mul(a,b):
	a*=b
	return a
def div(a,b):
	q=a/b
	r=a%b
	print("\n the quotient is:%s"%q)
	print("\n the remainder is:%s"%r)
def sqr(a):
	x=math.sqrt(a)
	return x
while True:
 print("\n\n choose the operation you want to perform:")
 print("\n\t1.addition")
 print("\n\t2.subtraction")
 print("\n\t.multiplication")
 print("\n\t4.division")
 print("\n\t5.square root")
 print("\n\t6.exit")
 choice=int(input('>'))

 if choice==1:
	print("\n\n enter the two numbers:")
	num1=int(input('>'))
	num2=int(input('>'))
	s=sum(num1,num2)
	print("the sum is:%s"%s)
	
 elif choice==2:
	print("\n\n enter the two numbers:")
	num1=int(input('>'))
	num2=int(input('>'))
	d=sub(num1,num2)
	print("the diference is :",d)
 elif choice==3:
	print("\n\n enter the two numbers:")
	num1=int(input('>'))
	num2=int(input('>'))
	p=mul(num1,num2)
	print("the product is :",p)
 elif choice==4:
	print("\n\n enter the two numbers:")
	num1=int(input('>'))
	num2=int(input('>'))
	div(num1,num2)
 elif choice==5:
	print("\n\n enter the two numbers:")
	num1=int(input('>'))
	q=sqr(num1,num2)
	print("the square root is :",d)
 else:
	print("\n\nyou choose to exit.bye......")
	break
           
	