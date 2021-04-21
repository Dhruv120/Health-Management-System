l= (input("Enter  Retrive(1) or lock(2) : "))
a = (input("Enter client no. : "))
b = (input("Enter type no. : "))

def getdate():
    import datetime
    return datetime.datetime.now()
p = getdate()

if l == "1":
    if a == "1"  and b == "1" :
        d= open("he.txt" )
        con1 = d.read()
        print( f"[{p}] + {con1}")

    elif a == "1" and b == "2":   
        g= open("hd.txt" )
        con2 = g.read()
        print(f"[{p}] + {con2}")
    
    elif a == "2" and b == "1":   
        h= open("me.txt"  )
        con3 = h.read()
        print(f"[{p}]+ {con3}")

    elif a == "2" and b == "2":   
        i= open("md.txt" )
        con4 = i.read()
        print(f"[{p}] + {con4}")    

    elif a == "3" and b == "1":   
        j= open("de.txt" )
        con5 = j.read()
        print(f"[{p}] + {con5}")

    elif a == "3" and b == "2":   
        k= open("dd.txt" )
        con6 = k.read()
        print(f"[{p}] + {con6}")

elif l=="2":
    if a == "1"  and b == "1" :
        d = open("he.txt" , "w")
        m = input("type here :  ")
        con1 = d.write(m)
        print("Successfully printed")

    elif a == "1" and b == "2":   
        g= open("hd.txt" , "w")
        m = input("type here :  ")
        con2 = g.write(m)
        print("Successfully printed")    

    elif a == "2" and b == "1":   
        g= open("me.txt" , "w")
        m = input("type here :  ")
        con3 = g.write(m)
        print("Successfully printed")

    elif a == "2" and b == "2":   
        g= open("md.txt" , "w")
        m = input("type here :  ")
        con4 = g.write(m)
        print("Successfully printed")

    elif a == "3" and b == "1":   
        g= open("de.txt" , "w")
        m = input("type here :  ")
        con5 = g.write(m)
        print("Successfully printed")    

    elif a == "3" and b == "2":   
        g= open("dd.txt" , "w" )
        m = input("type here :  ")
        con6 = g.write(m)
        print("Successfully printed")                            
            