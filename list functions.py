N = int(input())

commands = list()
l = list()

for i in range(N):
    string = str(input())
    commands.append(string.split())
    if commands[0][0] == "insert":
        l.insert(int(commands[0][1]),int(commands[0][2]))
    elif commands[0][0] == "print":
        print(l)
    elif commands[0][0] == "remove":
        l.remove(int(commands[0][1]))
    elif commands[0][0] == "append":
        l.append(int(commands[0][1]))
    elif commands[0][0] == "sort":
        l.sort()
    elif commands[0][0] == "reverse":
        l.reverse()
    del[commands[0]]