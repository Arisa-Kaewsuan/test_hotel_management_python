def readFile():
    # STEP 1 : read file
    file = open("input.txt", "r")
    # TEST  STEP 1
    # print(file.read())
    # print(file.readline())
    
    
    # STEP 2 : store data read from file in "List"
    for line in file:
        file_list = line.split()
        # TEST  STEP 2
        # print(type(file_list))
        # print(file_list)
    
    
        
readFile()
