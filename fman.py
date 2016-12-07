f = open('pass.txt', 'w')
f.write("TEXT TO BE WRITTEN")
a="superb"
f.write("\n"+a)
f = open('pass.txt', 'a')
f.write("asdfa")
f.close()

