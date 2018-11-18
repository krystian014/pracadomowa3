print ("Zacznij zgadywac...")
slowo = "testowanie"
proby = ''
rundy = 10
while rundy > 0:         
    failed = 0             
    for char in slowo:      
        if char in proby:    
            print (char),    
        else:          
            print ("_")                    
            failed += 1        
    if failed == 0:        
        print ("Wygrana!")     
        break              
    print    
    proba = input("Zgadnij literke:") 
    proby += proba                    
    if proba not in slowo:   
        rundy -= 1         
        print ("Zle")     
        print ("Zostalo " + str(turns) + " prob" )  
        if rundy == 0:               
            print ("Przegrana")
