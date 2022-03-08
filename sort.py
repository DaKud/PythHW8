import viev
import write_read_file
def sort(n,f):
    for i in f:
        if n in i:
            print(i.strip())

# sort(viev.get_class(),write_read_file.read_file())



def sort_data(d,f):
    
    if d=='1':
        for i in f:
            h=i.split() 
            print(h[0])
    if d=='2':
        for i in f:
            h=i.split()
            print(h[1])    
    if d=='3':
        for i in f:
            h=i.split()
            print(h[2])
    if d=='4':
        sort(viev.get_class(),write_read_file.read_file())
    if d=='5':
        print(*f,sep='')
    if d=='6':
        sort(viev.get_sort_data(),write_read_file.read_file())    
    if d=='7':
        print('До встречи!')        
          
        

sort_data(viev.get_number_operasion(),write_read_file.read_file())