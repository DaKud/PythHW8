from sort import sort,get_da
from viev import get_number_operasion,get_data
from write_read_file import read_file,write_file

def sort_data():
    while True: 
        d=get_number_operasion()
        if d=='1':
            print(*get_da(0,read_file()),sep='\n')    
        elif d=='2':
            print(*get_da(1,read_file()),sep='\n')        
        elif d=='3':
            print(*get_da(2,read_file()),sep='\n')    
        elif d=='4':
            print(*sort(input('Введите № класса: '),read_file()),sep='')   
        elif d=='5':
            print(*read_file(),sep='')
        elif d=='6':
            print(*sort(input('Введите фамилию ученика:'),read_file()),sep='')    
        elif d=='7':
            write_file(get_data())
        elif d=='8':
            print('До встречи!')        
            break  

# def button():
#     return sort_data()    

        
