import os
import pickle
help_text="Welcome C++ compiler as like an interpreter\ng++ on linux2\n\nCommands\n   help - For more information\n   about - About infomration\n   cls - clear screen\nHeader Files\n   for include header file just simple type\n   #include<headername>\nFunction\n   for crating function just type\n   typename functionname(args*){\n   and then [ENTER]\n   at end of function just type}\n"
about_text="Welcome C++ cmopiler as like interpreter\ng++ on linux2\n\n   Lokesh Bhoyar\n   for bugs inform at \n    lokesh.prenoramance2@gmail.com\n\n          Thank You!"
print('Welcome C++ compiler as like an interpreter\nG++ on linux2\nType "help","about" for more information.')
os.system('echo "#include<iostream>\nusing namespace std;" >header;echo >function;echo >body;echo "%s\n%s\nint main(){\n	%s\n	return 1;\n}">main')
func=''
s=0
def Hcompile(text):
	temp=open('temp.cpp','w')
	temp.write(text+'\nint main(){return 1;}')
	temp.close()
	if os.system('g++ temp.cpp'):
		return False
	else:
		return True
def Acompile(text='\n'):
	temp=open('temp.cpp','w')
	temp.write( open('main').read()%(open('header').read(),open('function').read()+text,open('body').read()) )
	temp.close()
	if os.system('g++ temp.cpp -o runthis'):
		return False
	else:
		return True
while(True):
	try:
		if not s:
			cmd=input('h4k3r >>> ')
		else:
			cmd=input('... ')
	except:
		break
	if cmd[-1]=='{':
		func+=cmd+'\n'
		s+=1
		continue
	elif cmd[-1]=='}' or cmd[-2]=='}':
		s-=1
		func+=cmd+'\n'
		if not s:
			if Acompile(func):
				function=open('function','a')
				function.write(func)
				function.close()
				func=''	
		continue
	elif s:
		func+=cmd+'\n'
		continue
	if cmd[0]=='#':
		if Hcompile(cmd):
			header=open('header','a')
			header.write(cmd+'\n')
			header.close()
	elif cmd=='exit':
		break
	elif cmd=='help':
		print(help_text)
	elif cmd=='about':
		print(about_text)
	elif cmd=='cls':
		os.system('clear')
	else:
		body=open('body','w')
		body.write(cmd+';')
		body.close()
		if Acompile():
			os.system('chmod 755 runthis')
			os.system('./runthis')
			print('')
		os.system('echo >body')
	
print('\nExit')

