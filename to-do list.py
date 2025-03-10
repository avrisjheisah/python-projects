user_input = 'random'
data = []

def menu():
    print('menu :')
    print('1. add task')
    print('2. complete task')
    print ('3. view all tasks')
    print('4. exit')

while user_input != '4':
    menu()
    user_input = input("enter the number that corresponds to what you would like to do : ")

    if user_input == '1':
        task = input('new task : ')
        data.append(task)
        print(' added task : ', task)
    elif user_input == '2':
        task = input('what did you complete : ')
        if task in data:
            data.remove(task)
        print('completed : ', task)
    elif user_input == '3':
        print('To-do list : ')
        for task in data:
            print(task)
    elif user_input == '4':
        print('bye bye')
    else:
        print('invalid number. enter numbers between 1 to 4.')
