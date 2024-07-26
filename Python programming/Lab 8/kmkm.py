def rep(filepath,searchstr,replacestr):
    str =""
    with open(filepath, 'r') as file:
        content = file.read()
        # str = content.replace(searchstr,replacestr)

        print("Before replace \n", content)

        words = content.split()
        print(words)
        count = 1
        for word in words:
            print(word)
            if word == searchstr:
                str += searchstr+"\t"
            else:
                str += word+"\t"
            if count % 4 == 0: