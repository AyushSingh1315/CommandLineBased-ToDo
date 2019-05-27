''' This is a simple CommandLine based TODO List'''

from os.path import exists
from getpass import getuser
from os import mkdir,chdir



tasks = []

def main():
    username = getuser()
    path = 'C://Users//'+str(username)+'//Documents//TODOListData'

    if exists(path=path):
        display(path)
        inp = input('Enter your command :>> ')
        if inp[0:8] == 'todo.add':
            task = inp[10:-2]
            add2list(task, path)

            main()



        elif inp[0:14] == 'todo.removeAll':
                print("Are you sure you wanna remove all the tasks??? \n Y/N>>",end=' ')
                s = input("")
                if s=='Y' or s=='y':
                    file = open(path + "//data.des", 'w')
                    file.write('``')
                    file.close()

                elif s=='N' or s=='n':
                    main()

                else:
                    print('Wrong input :(')

                main()
        elif inp[0:11] == 'todo.remove':
            num = int(inp[12])
            removeFromList(num,path)
            main()

        elif inp[0:9]=='todo.help':
            print("Command Line TODO List ver 1.0 \n \t ~Created by Ayush Singh\n\n1. Use todo.add('Your Task') to add a new task\n2. Use todo.remove(task_number) to remove a Task \n3. Use todo.removeAll() to remove all the tasks at once\n4. Use todo.exit() to exit"
                  "\n\n NOTE: If you want to add multiple tasks at once input them as task1``task2``task3``task4 \n where `` are two grave accents(The key above Tab Key)")
            main()

        elif inp[0:9]=='todo.exit':
            exit()

        elif inp[0:14] == 'todo.removeAll':
                print("Are you sure you wanna remove all the tasks??? \n Y/N>>",end=' ')
                s = input("")
                if s=='Y' or s=='y':
                    file = open(path + "//data.des", 'w')
                    file.write('``')
                    file.close()

                elif s=='N' or s=='n':
                    main()

                else:
                    print('Wrong input :(')

                main()



        else:
            print('\n\nPlease check your input\n\n type todo.help() for more information')
            main()


    else:
        chdir("C://Users//"+str(username)+'//Documents//')
        mkdir("TODOListData")
        chdir("TODOListData")
        file = open('data.des','w')
        file.write('``')
        file.close()
        file = open('helper.dll','w')
        file.write("JUST KIDDING.......Ignore this dll file :)")
        file.close()










def display(path):
    file = open(path+"//data.des",'r')
    data = file.read()
    tasks = data.split('``')
    print('Current Tasks : ')
    for i in range(1, len(tasks)-1):
        print(str(i)+' '+tasks[i])
    file.close()




def add2list(task, path):
    file2 = open(path + "//data.des", 'a')
    file2.write(task+'``')
    file2.close()




def removeFromList(num,path):
    file = open(path + "//data.des", 'r')
    data = file.read()
    tasks = data.split('``')
    tasks.pop(num)
    file.close()
    file = open(path + "//data.des", 'w')
    for task in tasks:
        file.write(task+'``')

    file.close()
    file = open(path + "//data.des", 'r')
    data_trimmed = file.read()[0:-2]
    file.close()

    file = open(path + "//data.des", 'w')
    file.write(data_trimmed)
    file.close()








if __name__ == '__main__':
    print('Type todo.help() to view the commands')
    main()


