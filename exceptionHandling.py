#TranTung

try:
    f = open("demoFile.txt")
    try:
        f.write("Hello world!")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when openfile")