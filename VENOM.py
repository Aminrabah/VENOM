import os,platform
os.system('git pull')
#exit('\n Update Soon...!')
VENOM=platform.architecture()[0]
if VENOM=="32bit":exit(' \n 32bit soon')#__import__("BSDK32")
elif VENOM=="64bit":__import__("BSDK")
