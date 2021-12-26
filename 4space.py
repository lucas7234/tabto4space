#4space.py
import webbrowser
fdir = input("Directory of original Python file: ")
sdir = input("Directory of ouput Python file: ")

#read original file and replace tab
f = open(fdir, 'r')
body = f.read().replace('\t', ' ' * 4)
f.close()

#write in output file
f = open(sdir, 'w')
f.write(body)
f.close()

#open new file in webbrowser
webbrowser.open_new("file:///"+sdir)
