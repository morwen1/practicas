import time
file = open("archivo.txt" ,'r') 
    
print(file.read())
x = time.process_time()
print(x)
file.close()
