import pyttsx3 as pt
import os

pt.speak("  Welcome!")
pt.speak("Type what can i open for you from the below list")
print("\n  Welcome!")
print("\n->Chrome\n->Microsift-edge\n->Notepad\n->VSCode\n->Media_player\n->Music_player\n->Power Point\n->MS Word\n->MS Excel\n->Paint\n->Calculator\n->Camera\n->Calender\n->Alarm-Clock\n->Maps\n->News\n->Game-Candy Crush\n->Screensnip\n->File Explorer\n->System Settings\n")



while True:
	print("Chat what you want to open: "  , end='')
	a = input()

	if("dont" in a) or ("no" in a) or ("don't" in a):
		pt.speak("Enter the next command!")
		print("Enter the next command!")

	else: 
		if ("chrome" in a):
			os.system("start chrome")

		elif(("microsoft" in a) and ("edge" in a)):
			os.system("start microsoft-edge:")

		elif(("notepad" in a) or ("editor" in a) ) :
			os.system("start notepad")

		elif(("player" in a) and ("media" in a)):
			os.system("start vlc")

		elif(("player" in a) and ("music" in a)):
			os.system("start mswindowsmusic:")

		elif("camera" in a) or ("web cam" in a):
			os.system("start microsoft.windows.camera:")

		elif("calculator" in a):
			os.system("start calc")	

		elif(("ms word" in a) or ("word" in a)):
			os.system("start winword")
	
		elif(("ms excel" in a) or ("excel" in a)):
			os.system("start excel")

		elif(("ms powerpoint" in a) or ("power point" in a) or("ppt" in a)):
			os.system("start powerpnt")

		elif("paint" in a):
			os.system("start mspaint")

		elif("alarm" in a) or ("clock" in a):
			os.system("start ms-clock:")

		elif("calender" in a):
			os.system("start outlookcal:")

		elif("maps" in a) or ("map" in a):
			os.system("start ms-drive-to:")

		elif("news" in a):
			os.system("start bingnews:")

		elif("candy crush" in a) or ("game" in a):
			os.system("start candycrushsodasaga:")

		elif(("vscode" in a) or ("code" in a)):
			os.system("start code")

		elif("snip" in a):
			os.system("start snippingtool")

		elif("file explorer" in a):
			os.system("start explorer")

		elif(("system settings" in a) or ("settings" in a) or ("setting" in a)):
			os.system("start ms-settings:")

		elif("exit" in a)  or ("quit" in a) or ("stop" in a):
			pt.speak("Signing off, Bye!")
			print("\n  Signing off, Bye!")
			break
		else:
			pt.speak("Didn't undertand, please try again")
			print("Didn't undertand try again")


