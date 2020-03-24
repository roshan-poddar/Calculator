def rp():
    print("WELCOME TO RP CALCULATOR")
    print("""Option provided:
         1.Sum        2.Subtract
         3.Multiply   4.Divide
         5.Sqrt       6.Log
         7.Sin        8.Cos
         9.Tan       10.Degrees
        11.Radians""")
    a = input("Choose your option:")
    if a=="1":
        b = int(input("Enter the number:"))
        c = int(input("Enter the number:"))
        d = b+c
        print("sum = ",d)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "2":
        f = int(input("Enter the number:"))
        g = int(input("Enter the number:"))
        h = f-g
        print("Subtract = ",h)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "3":
        i = int(input("Enter the number:"))
        j = int(input("Enter the number:"))
        k = i*j
        print("Multiply = ",k)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "4":
        l = int(input("Enter the number:"))
        m = int(input("Enter the number:"))
        n = l/m
        print("Divide = ",n)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "5":
        from math import sqrt
        o = int(input("Enter the number:"))
        p = sqrt(o)
        print("sqrt = ",p)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "6":
        from math import log
        q = int(input("Enter the number:"))
        r = log(q)
        print("log = ",r)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a =="7":
        from math import sin
        s = int(input("Enter the number:"))
        t = sin(s)
        print("sin = ",t)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "8":
        from math import cos
        u = int(input("Enter the number:"))
        v = cos(u)
        print("cos = ",v)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "9":
        from math import tan
        w =int(input("Enter the number:"))
        x = tan(w)
        print("tan = ",x)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "10":
        from math import degrees
        y = int(input("Enter the radian:"))
        z = degrees(y)
        print("degrees = ",z)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    elif a == "11":
        from math import radians
        aa = int(input("Enter the degrees:"))
        bb = radians(aa)
        print("radians = ",bb)
        e = input("You want to reuse:")
        if "yes" in e or "Y" in e or "YES" in e or "y" in e:
            print(rp())
        else:
            print("Thank you for using our program")
    else:
        print("You entered something wrong:")
        print("Please choose your option carefully")
        print(rp())
        
        




rp()