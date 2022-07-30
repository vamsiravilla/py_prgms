##text=open('file.txt','r')
##d=dict()
##for line in text:
##    line=line.strip()
##    line=line.lower()
##    words=line.split()
##    for word in words:
##        if word in d:
##            d[word]=d[word]+1
##        else:
##            d[word]=1
##print(d)            
##for key in list(d.keys()):
##    print(key,':',d[key])

##file=open('file.txt')
##lines=file.readlines()
##last_lines=lines[-5:]
##print(last_lines)

##file = open("file.txt")
##lines=file.readlines()
##print(lines)


##import random
##lines=open('file.txt').read().splitlines()
##print(random.choice(lines))

##for i in range(65,65+26):
##    res=chr(i)+'.txt'
##    open(res,'w')
##    print(res)

##file=open('abc.txt','w')
##data="vamsi"
##file.write(data)

##with open("file.txt",'r') as f:
##    data=f.read()
##    data.replace(","," ")
##    print(len(data.split(" ")))

##test=[]
##alpha='a'
##for i in range(0,26):
##    test.append(alpha)
##    alpha=chr(ord(alpha)+1)
##print(test)    


##file_name = input("Enter The File's Name: ")
##try:
##	file_read = open(file_name, "r")
##	text = input("Enter the String: ")
##	lines = file_read.readlines()
##	new_list = []
##	idx = 0
##	for line in lines:
##		if text in line:
##			new_list.insert(idx, line)
##			idx += 1
##	file_read.close()
##	if len(new_list)==0:
##		print("\n\"" +text+ "\" is not found in \"" +file_name+ "\"!")
##	else:
##		lineLen = len(new_list)
##		print("\n**** Lines containing \"" +text+ "\" ****\n")
##		for i in range(lineLen):
##			print(end=new_list[i])
##		print()
##except :
##    print("\nThe file doesn't exist!")

##file_name=input("Enter the file name:")
##try:
##    file_read=open(file_name,"r")
##    text=input("Enter the string:")
##    lines=file_read.readlines()
##    new_list=[]
##    idx=0
##    for i in lines:
##        if text in i:
##            new_list.insert(idx,i)
##            idx+=1
##    file_read.close()
##    if len(new_list)==0:
##        print("************text not found***********")
##    else:
##        line_len=len(new_list)
##        print("********lines containing""+text+""*********")
##        for i in range(line_len):
##            print(end=new_list[i])
##        print()    
##except:
##    print("The file is not exists")

##file_name=input("Enter the file name:")
##try:
##    file_read=open(file_name,"r")
##    text=input("enter the string:")
##    lines=file_read.readlines()
##    new_list=[]
##    idx=0
##    for line in  lines:
##        if text in line:
##            new_list.insert(idx,line)
##            idx+=1
##    file_read.close()
##    if len(new_list)==0:
##        print(text, "is not found in", file_name)
##    else:
##        linelen=len(new_list)
##        print("*****************Lines Containing*******************")
##        for k in range(linelen):
##            print(end=new_list[k])
##        print()
##except:
##    print("The file is not exist")

##import requests
##from bs4 import BeautifulSoup as bs
##
##URL = 'https://www.geeksforgeeks.org/page/'
##
##for page in range(1, 10):
##
##	req = requests.get(URL + str(page) + '/')
##	soup = bs(req.text, 'html.parser')
##
##	titles = soup.find_all('div', attrs={'class', 'head'})
##
##	for i in range(4, 19):
##		if page > 1:
##			print(f"{(i-3)+page*15}" + titles[i].text)
##		else:
##			print(f"{i-3}" + titles[i].text)


##import hashlib
##print("**************PASSWORD CRACKER ******************")
##		
### To check if the password
### found or not.
##pass_found = 0									
##
##input_hash = input("Enter the hashed password:")
##
##pass_doc = input("\nEnter passwords filename including path(root / home/):")
##
##try:
##	# trying to open the password file.
##	pass_file = open(pass_doc, 'r')			
##except:
##	print("Error:")
##	print(pass_doc, "is not found.\nPlease give the path of file correctly.")
##	quit()
##
##
### comparing the input_hash with the hashes
### of the words in password file,
### and finding password.
##
##for word in pass_file:
##	# encoding the word into utf-8 format
##	enc_word = word.encode('utf-8')
##			
##	# Hashing a word into md5 hash
##	hash_word = hashlib.md5(enc_word.strip())
##
##	# digesting that hash into a hexa decimal value	
##	digest = hash_word.hexdigest()		
##	
##	if digest == input_hash:
##		# comparing hashes
##		print("Password found.\nThe password is:", word)
##		pass_found = 1
##		break
##
### if password is not found.
##if not pass_found:
##	print("Password is not found in the", pass_doc, "file")
##	print('\n')
##print("***************** Thank you **********************")

##class Student:  
##    # Constructor - non parameterized  
##    def __init__(self):  
##        print("This is non parametrized constructor")  
##    def show(self,name):  
##        print("Hello",name)  
##student = Student()  
##student.show("John") 


##class Student:
##    def __init__(self,name,id,age):
##        self.name=name
##        self.id=id
##        self.age=age
##s=Student("vamsi",20290,27)
##print(getattr(s,'name'))
##setattr(s,"name","vamsi-Ravilla")
##print(getattr(s,'name'))
##print(hasattr(s,'id'))
##delattr(s,'age')
##print(getattr(s,'age'))

##class Student:
##    def __init__(self,name,id,age):
##        self.name=name;
##        self.id=id;
##        self.age=age;
##    def display(self):
##        print("Name:%s,ID:%d"%(self.name,self.id))
##s=Student("vamsi",20290,27)
##print(s.__doc__)
##print(s.__dict__)
##print(s.__module__)

##class Animal:  
##    def speak(self):  
##        print("Animal Speaking")  
###child class Dog inherits the base class Animal  
##class Dog(Animal):  
##    def bark(self):  
##        print("dog barking")  
##d = Dog()  
##d.bark()  
##d.speak()  


##class Calculation1:
##    def summation(self,a,b):
##        return a+b
##class Calculation2:
##    def multiplication(self,a,b):
##        return a*b
##class Derived(Calculation1,Calculation2):
##    def Devide(self,a,b):
##        return a/b
##d=Derived()
##print(d.summation(10,20))
##print(d.multiplication(10,20))
##print(d.Devide(10,20))
##

##class Calculation1:  
##    def Summation(self,a,b):  
##        return a+b;  
##class Calculation2:  
##    def Multiplication(self,a,b):  
##        return a*b;  
##class Derived(Calculation1,Calculation2):  
##    def Divide(self,a,b):  
##        return a/b;  
##d = Derived()  
##print(isinstance(d,Derived))  

##import os
##print(os.getcwd())

##import os
##print(os.name)

##import os
##os.mkdir("d:\\newdir")

##import os
##os.chdir("d:\\")

##import os
##os.rmdir("d:\\newdir")
##os.chdir("..")
##os.rmdir("newdir ")

##import os
##try:
##    filename="Python.txt"
##    f=open(filename,'rU')
##    text=f.read()
##    f.close()
##except IOError:
##    print("Problem reading:"+filename)

##import os
##fd="python.txt"
##file=open(fd,'w')
##file.write("This is awesome")
##file.close()
##file=open(fd,'r')
##text=file.read()
##print(text)
##file=os.popen(fd,'w')
##file.write("This is awesome")


##import os
##fr="Python1.txt"
##file=open(fr,'r')
##text=file.read()
##print(text)
##os.close(file)

##import os
##fd="python.txt"
##os.rename(fd,'Python1.txt')
##os.rename(fd,'Python1.txt')


##import os
##import sys
##path1=os.access("Python.txt",os.F_OK)
##print("Exist path:",path1)
##
##path2=os.access("Python.txt",os.R_OK)
##print("It access to read the file:",path2)
##
##path3=os.access("Python.txt",os.W_OK)
##print("It access to write the file:",path3)
##
##path4=os.access("Python.txt",os.X_OK)
##print("Check if path can be executed:",path4)

##import sys
##sys.modules
##sys.argv
##sys.base_exec_prefix
##sys.base_prefix
##sys.byteorder
##sys.maxsize
##sys.path
##sys.stdin
##sys.getrefcount
##sys.exit
##sys.executable
##sys.platform

##import sys
##print(type(sys.argv))
##print("the command line arguments are:")
##for i in sys.argv:
##    print(i)

##import getopt
##import sys
##argv=sys.argv[1:]
##try:
##    opts,args=getopt.getopt(argv,'hm:d',['help','my_file='])
##    print(opts)
##    print(args)
##except getopt.GetoptError:
##    print("something went wrong!")
##    sys.exit(2)

##import random
##num=random.random()
##print(num)

##import random
##num=random.randint(1,500)
##print(num)

##import random
##num=random.randrange(1,10)
##print(num)
##num=random.randrange(1,10,2)
##print(num)
##num=random.randrange(0,101,10)
##print(num)

##import random
##random_s=random.choice("Random Module")
##print(random_s)
##random_l=random.choice([23,54,765,23,45,45])
##print(random_l)
##random_s=random.choice([12,64,23,54,34])
##print(random_s)

##import random
##a=[34,23,65,86,23,43]
##random.shuffle(a)
##print(a)
##random.shuffle(a)
##print(a)

import random
random.seed(2)
print("Generating 5 random numbers:")
print([random.randint(1,300) for r in range(6)])
random.seed(2)
print([random.randint(1,300) for i in range(6)])
