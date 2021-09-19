#!/usr/bin/env python3
import requests, tarfile

import sys, os, time, os.path, random
from tkinter import *
from tkinter import messagebox



#-------------------------------------------------------------------------------------------------------------------------------------------------
# Url - alternative version Firefox x64 > Ukraine lang.

urlFirefox = "https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=uk"
urlFirefoxBeta = "https://download.mozilla.org/?product=firefox-beta-latest-ssl&os=linux64&lang=uk"
urlFirefoxDeveloperEdition = "https://download.mozilla.org/?product=firefox-devedition-latest-ssl&os=linux64&lang=uk"
urlFirefoxNightly = "https://download.mozilla.org/?product=firefox-nightly-latest-l10n-ssl&os=linux64&lang=uk"
#urlFirefoxExtendedSupportRelease = 

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def firefox():
	
	mb = messagebox.askquestion ('Інформаційне вікно','Провести: завантаження та інтеграцію; Firefox Stable ?')
	if mb == 'yes':

		name = os.getenv('USER')

		nameOld = "/home/" + name + "/.local/share/applications/firefox.tar.bz2"
		nameOldEx = "/home/" + name + "/.local/share/applications"


# Завантаження файлу

		file=open(nameOld,"wb") 
		ufr = requests.get(urlFirefox) 
		file.write(ufr.content) 
		file.close()

# Розпакування файлу

		tar = tarfile.open(nameOld, "r:bz2")  
		tar.extractall(nameOldEx)
		tar.close()

# Видалення сміття

		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), nameOld)
		os.remove(path)

# Створення пускового файлу 

		fileDesktop = open('/home/'+name+'/.local/share/applications/firefoxStable.desktop', 'w')
		fileDesktop.write('[Desktop Entry]'+ '\n')
		fileDesktop.write('Type=Application'+ '\n')
		fileDesktop.write('Name=Firefox Stable'+ '\n')
		fileDesktop.write('Terminal=false'+ '\n')
		fileDesktop.write('Categories=WebBrowser;'+ '\n')
		fileDesktop.write('MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;x-scheme-handler/chrome;video/webm;application/x-xpinstall;'+ '\n')
		fileDesktop.write('StartupNotify=true'+ '\n')

		runFile = "/home/" + name + "/.local/share/applications/firefox/firefox"
		iconFile = "/home/" + name + "/.local/share/applications/firefox/browser/chrome/icons/default/default64.png"	
	
		fileDesktop.write('Exec ='+ runFile + '\n')
		fileDesktop.write('Icon =' + iconFile + '\n')
		fileDesktop.close()



		messagebox.showinfo("Інформаційне вікно", "Процес - інтеграції >> ЗАВЕРШИНИЙ ! :)")
	
	else:
		 print("pass")


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def firefoxBeta():
	
	mb = messagebox.askquestion ('Інформаційне вікно','Провести: завантаження та інтеграцію; Firefox Beta ?')
	if mb == 'yes':

		name = os.getenv('USER')

		nameOld = "/home/" + name + "/.local/share/applications/firefoxBeta.tar.bz2"
		nameOldEx = "/home/" + name + "/.local/share/applications/"
		
		if os.path.exists(nameOldEx + 'fBeta'):
			print("файл існує!")	
		else:
		
			fileFBeta = os.mkdir(nameOldEx + 'fBeta')
		
		nameOldfBeta = nameOldEx + 'fBeta'

# Завантаження файлу

		file=open(nameOld,"wb") 
		ufr = requests.get(urlFirefoxBeta) 
		file.write(ufr.content) 
		file.close()

# Розпакування файлу

		tar = tarfile.open(nameOld, "r:bz2")  
		tar.extractall(nameOldfBeta)
		tar.close()

# Видалення сміття

		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), nameOld)
		os.remove(path)

# Створення пускового файлу 

		fileDesktop = open('/home/'+name+'/.local/share/applications/firefoxBeta.desktop', 'w')
		fileDesktop.write('[Desktop Entry]'+ '\n')
		fileDesktop.write('Type=Application'+ '\n')
		fileDesktop.write('Name=Firefox Beta'+ '\n')
		fileDesktop.write('Terminal=false'+ '\n')
		fileDesktop.write('Categories=WebBrowser;'+ '\n')
		fileDesktop.write('MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;x-scheme-handler/chrome;video/webm;application/x-xpinstall;'+ '\n')
		fileDesktop.write('StartupNotify=true'+ '\n')

		runFile = "/home/" + name + "/.local/share/applications/fBeta/firefox/firefox"
		iconFile = "/home/" + name + "/.local/share/applications/fBeta/firefox/browser/chrome/icons/default/default64.png"	
	
		fileDesktop.write('Exec ='+ runFile + '\n')
		fileDesktop.write('Icon =' + iconFile + '\n')
		fileDesktop.close()



		messagebox.showinfo("Інформаційне вікно", "Процес - інтеграції >> ЗАВЕРШИНИЙ ! :)")
	
	else:
		 print("pass")
	

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def firefoxDev():
	
	mb = messagebox.askquestion ('Інформаційне вікно','Провести: завантаження та інтеграцію; Firefox Dev ?')
	if mb == 'yes':

		name = os.getenv('USER')

		nameOld = "/home/" + name + "/.local/share/applications/firefoxDev.tar.bz2"
		nameOldEx = "/home/" + name + "/.local/share/applications/"
		
		if os.path.exists(nameOldEx + 'fDev'):
			print("файл існує!")	
		else:
		
			fileFBeta = os.mkdir(nameOldEx + 'fDev')
		
		nameOldfDev = nameOldEx + 'fDev'

# Завантаження файлу

		file=open(nameOld,"wb") 
		ufr = requests.get(urlFirefoxDeveloperEdition) 
		file.write(ufr.content) 
		file.close()

# Розпакування файлу

		tar = tarfile.open(nameOld, "r:bz2")  
		tar.extractall(nameOldfDev)
		tar.close()

# Видалення сміття

		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), nameOld)
		os.remove(path)

# Створення пускового файлу 

		fileDesktop = open('/home/'+name+'/.local/share/applications/firefoxDev.desktop', 'w')
		fileDesktop.write('[Desktop Entry]'+ '\n')
		fileDesktop.write('Type=Application'+ '\n')
		fileDesktop.write('Name=Firefox Dev'+ '\n')
		fileDesktop.write('Terminal=false'+ '\n')
		fileDesktop.write('Categories=WebBrowser;'+ '\n')
		fileDesktop.write('MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;x-scheme-handler/chrome;video/webm;application/x-xpinstall;'+ '\n')
		fileDesktop.write('StartupNotify=true'+ '\n')

		runFile = "/home/" + name + "/.local/share/applications/fDev/firefox/firefox"
		iconFile = "/home/" + name + "/.local/share/applications/fDev/firefox/browser/chrome/icons/default/default64.png"	
	
		fileDesktop.write('Exec ='+ runFile + '\n')
		fileDesktop.write('Icon =' + iconFile + '\n')
		fileDesktop.close()



		messagebox.showinfo("Інформаційне вікно", "Процес - інтеграції >> ЗАВЕРШИНИЙ ! :)")
	
	else:
		 print("pass")
	


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def firefoxNightly():
	
	mb = messagebox.askquestion ('Інформаційне вікно','Провести: завантаження та інтеграцію; Firefox Nightly ?')
	if mb == 'yes':

		name = os.getenv('USER')

		nameOld = "/home/" + name + "/.local/share/applications/firefoxNightly.tar.bz2"
		nameOldEx = "/home/" + name + "/.local/share/applications/"
		
		if os.path.exists(nameOldEx + 'fNightly'):
			print("файл існує!")	
		else:
		
			fileFNightly = os.mkdir(nameOldEx + 'fNightly')
		
		nameOldfNightly = nameOldEx + 'fNightly'

# Завантаження файлу

		file=open(nameOld,"wb") 
		ufr = requests.get(urlFirefoxNightly) 
		file.write(ufr.content) 
		file.close()

# Розпакування файлу

		tar = tarfile.open(nameOld, "r:bz2")  
		tar.extractall(nameOldfNightly)
		tar.close()

# Видалення сміття

		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), nameOld)
		os.remove(path)

# Створення пускового файлу 

		fileDesktop = open('/home/'+name+'/.local/share/applications/firefoxNightly.desktop', 'w')
		fileDesktop.write('[Desktop Entry]'+ '\n')
		fileDesktop.write('Type=Application'+ '\n')
		fileDesktop.write('Name=Firefox Nightly'+ '\n')
		fileDesktop.write('Terminal=false'+ '\n')
		fileDesktop.write('Categories=WebBrowser;'+ '\n')
		fileDesktop.write('MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;x-scheme-handler/chrome;video/webm;application/x-xpinstall;'+ '\n')
		fileDesktop.write('StartupNotify=true'+ '\n')

		runFile = "/home/" + name + "/.local/share/applications/fNightly/firefox/firefox"
		iconFile = "/home/" + name + "/.local/share/applications/fNightly/firefox/browser/chrome/icons/default/default64.png"	
	
		fileDesktop.write('Exec ='+ runFile + '\n')
		fileDesktop.write('Icon =' + iconFile + '\n')
		fileDesktop.close()



		messagebox.showinfo("Інформаційне вікно", "Процес - інтеграції >> ЗАВЕРШИНИЙ ! :)")
	
	else:
		 print("pass")
	
	
	
#-------------------------------------------------------------------------------------------------------------------------------------------------
# Download alternative version Firefox 

#file=open(r"firefox.tar.bz2","wb") 
#ufr = requests.get("https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=uk") 
#file.write(ufr.content) 
#file.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#-------------------------------------------------------------------------------------------------------------------------------------------------
# Unpacking the archive 

#tar = tarfile.open("/home/userbuild/appPy/file.tar.bz2", "r:bz2")  
#tar.extractall()
#tar.close()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#-------------------------------------------------------------------------------------------------------------------------------------------------
# gui 

root = Tk()
root.title("FIA - manager")
root.geometry("526x268")
root.resizable(False, False)
root["bg"] = "#000000"

ourButtonFirefox = PhotoImage(file="firefox2.png")
ourButtonFirefoxB = PhotoImage(file="firefoxB2.png")
ourButtonFirefoxD = PhotoImage(file="firefoxD2.png")
ourButtonFirefoxN = PhotoImage(file="firefoxN2.png")

Button(root, image=ourButtonFirefox, bg="#000000", activebackground = "#000068", command= lambda: firefox()).grid(row=0,column=0)
Button(root, image=ourButtonFirefoxB, bg="#000000", activebackground = "#000068", command= lambda: firefoxBeta()).grid(row=0,column=1)
Button(root, image=ourButtonFirefoxD, bg="#000000", activebackground = "#d0b000", command= lambda: firefoxDev()).grid(row=1,column=0)
Button(root, image=ourButtonFirefoxN, bg="#000000", activebackground = "#d0b000", command= lambda: firefoxNightly()).grid(row=1,column=1)

#Button(root, image=our_button, bg="#000000", activebackground = "#000068", highlightthickness=0, bd=0).grid(row=0,column=0)
#Label(text="FirefoxStable",font='Times 20').grid(row=0,column=1)
#Button(text="Firefox", padx="40", pady="10", font="Times 24",width=2, height=2).grid(row=0,column=0)


root.mainloop()


