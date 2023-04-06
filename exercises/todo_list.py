header = 'TODOS'
print(header)

todos = []
completed = []

while True:
    print('***********************')
    print('Yapilacak isler:')
    for i in range(len(todos)):
        print(f'{i+1}. {todos[i]}')
    
    print('Lutfen yapilacak bir is girin. Yardim icin h harfine basin.')
    command = input('> ')
    if command == 'q':
        break  
    elif command == 'h':
        print('Yardim menusu')
        print('----------------------')
        print('q harfi ile cikabilirsiniz')
        print('Listeye eklemek istediginiz isi yazip entera basin')
        print('Ya da bitirdiginiz isin numarasini yazin')   
    elif command.isnumeric():
        index = int(command)-1
        if index >= len(todos):
            print('Bu numarali bir is yok')
        else:
            done = todos.pop(index)
            completed.append(done)
    # son secenek olarak todos liste komutu ekle
    else:
        todos.append(command)

# program kapaninca yapilmis olan islemleri yazdir
if completed:
    print('Yaptigin isler:')
    for todo in completed:
        print(f'* {todo}')


    