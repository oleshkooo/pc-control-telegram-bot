users = ['oleshko_o', 'asdasd']

currentUser = 'oleshko_o'

def searchList(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

print(searchList(users, currentUser))