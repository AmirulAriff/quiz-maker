print("enter your question. press enter if you are done.")
contents = []
lmao = ""
while True:
    if lmao == "lol":
        break
    try:
        line = input()
    except EOFError:
        break
    if line == '':
        hello = input("type quit to finish: ")
        if hello == "quit":
                print("yeay")
                break
        else:
         while hello != "quit":
            hello = input("type quit to finish: ")
            if hello == "quit":
                lmao = "lol"
                print("yeay")

    contents.append(line)



print(contents)
#print(str(contents)[1:-1])
lembu = (' \n '.join(map(str, contents)))
print(str(lembu))




