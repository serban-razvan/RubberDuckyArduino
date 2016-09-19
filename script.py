import os

def trans(string):
    if string in ["DELETE","HOME","END","INSERT","END","TAB","ESC"]:
        return "KEY_"+string
    elif string.startswith("F") and len(string)>=2: ##f1-f12
        return "KEY_"+string
    elif string == "PAGEUP":
        return "KEY_PAGE_UP"
    elif string == "PAGEDOWN":
        return "KEY_PAGE_DOWN"
    elif string in ["GUI", "WINDOWS"]:
        return "KEY_PAGE_DOWN"
    elif string in ["UP","DOWN","LEFT","RIGHT"]:
        return "KEY_"+string+"_ARROW"
    elif string == "UPARROW":
        return "KEY_UP_ARROW"
    elif string == "DOWNARROW":
        return "KEY_DOWN_ARROW"
    elif string == "LEFTARROW":
        return "KEY_LEFT_ARROW"
    elif string == "RIGHTARROW":
        return "KEY_RIGHT_ARROW"
    elif string == "ESCAPE":
        return "KEY_ESC"
    elif string == "SPACE":
        return "' '"
    elif string == "CAPSLOCK":
        return "KEY_CAPS_LOCK"
    


    elif len(string)==1:
        return "'"+string+"'"
    else:
        return None

def slash(string):
    return string.replace("\\","\\\\")

print "What's the Rubber Ducky Script called?"
while 1:
    nume = raw_input()
    if nume in os.listdir("."):
        break
    else:
        print nume+" cannot be found. Try again."

with open(nume) as f:
    lines = [line.rstrip(' \n\t\r') for line in f]

final = open(nume+".ard","w");

DEF=0


for i in range(len(lines)):
    x=lines[i]
    res = x.partition(" ")
    if res[0] in ["REM",""]:
        pass
    elif res[0] in [ "DEFAULT_DELAY", "DEFAULTDELAY"]:
        DEF = int(res[2])
    elif res[0] == "DELAY":
        final.write("delay("+str(int(res[2]))+");")
    elif res[0] == "ENTER":
        final.write("Keyboard.write(KEY_RETURN);")
    elif res[0] == "STRING":
        final.write("Keyboard.print(\""+slash(res[2])+"\");")
    elif res[0] in ["GUI", "WINDOWS"]:
        final.write("Keyboard.press(KEY_LEFT_GUI);")
        final.write("Keyboard.write("+trans(res[2])+");")
        final.write("Keyboard.release(KEY_LEFT_GUI);")
    elif res[0] in ["MENU", "APP"]:
        final.write("Keyboard.press(KEY_LEFT_SHIFT);")
        final.write("Keyboard.write(KEY_F10);")
        final.write("Keyboard.release(KEY_LEFT_SHIFT);")
    elif res[0] == "SHIFT":
        final.write("Keyboard.press(KEY_LEFT_SHIFT);")
        final.write("Keyboard.write("+trans(res[2])+");")
        final.write("Keyboard.release(KEY_LEFT_SHIFT);")
    elif res[0] == "ALT":
        final.write("Keyboard.press(KEY_LEFT_ALT);")
        final.write("Keyboard.write("+trans(res[2])+");")
        final.write("Keyboard.release(KEY_LEFT_ALT);")
    elif res[0] in ["CTRL", "CONTROL"]:
        final.write("Keyboard.press(KEY_LEFT_CTRL);")
        final.write("Keyboard.write("+trans(res[2])+");")
        final.write("Keyboard.release(KEY_LEFT_CTRL);")

    elif trans(res[0])!=None: #simple command
        final.write("Keyboard.write("+trans(res[0])+");")

        
    else:
        print "Wrong at the loop"
        print "String is "+ x
        print "Its id is "+ str(i)
        



    if DEF!=0:
        final.write("delay("+str(DEF)+");")

    final.write("\n")

final.close()


######### FUNCTION MAKER

with open(nume+".ard","r") as final:
    content = final.read()
    
ext = open("extern.h","w")

ext.write ("void FUNCTIE(){\n\n")
ext.write (content)
ext.write ("\n}")
ext.close()
