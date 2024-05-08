array = b'PYnative'     
array_view = memoryview(array)  
container = list(array_view)   
for char in container:
    print(char, end=" ")

#ant type use answer is same