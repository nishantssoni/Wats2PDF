import os
def cut_msg(string, cut):
    message = []
    length = 0
    temp = ""
    
    for i in string.split():
        
        if length < cut:
            temp = temp + i + ' '
            length = len(temp)
        else:
            message.append(temp.strip())
            length = 0
            temp = i + ' '

    message.append(temp.strip())
    return message

def getFileName():
    files = []
    count = 1;
    for x in os.listdir("./your_exported_txt"):
        if x.endswith(".txt"):
            print(f"{count}. {x}")
            count += 1
            files.append(x)
    
    if len(files) == 0:
        print("place some file in your exported chat and then try again")
        return "end"
    
    
    ch = int( input(f"\nenter your choice {1} - {count -1} :: ") )
    if(ch > len(files) or ch < 1):
        print("enter a valid choice")
        exit()
    return "./your_exported_txt/" + files[(ch-1)]
