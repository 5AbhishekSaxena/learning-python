cmdString = [12, "insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort",
             "print", "pop", "reverse", "print"]

N = cmdString[0]  # int(input())

newList = list()

for i in range(1,N+1):
    cmd = cmdString[i]
    if "insert" in cmd:
        cmdType = cmd.split()
        pos = int(cmdType[1])
        value = int(cmdType[2])
        newList.insert(pos, value)
    elif "print" in cmd:
        print(newList)
    elif "remove" in cmd:
        cmdType = cmd.split()
        pos = int(cmdType[1])
        newList.remove(pos)
    elif "append" in cmd:
        cmdType = cmd.split()
        value = int(cmdType[1])
        newList.append(value)
    elif "sort" in cmd:
        newList.sort()
    elif "pop" in cmd:
        newList.pop()
    elif "reverse" in cmd:
        newList.reverse()
