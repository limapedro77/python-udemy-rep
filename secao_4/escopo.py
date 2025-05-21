x = 1

def escopo ():
    global x
    x = 10

    def escopo2 ():
        x = 20
        print(x)
    
    escopo2()
    print(x) 

print(x)
escopo()
