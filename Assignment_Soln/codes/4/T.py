with open("uni1.dat","r") as f1:
    with open ("uni2.dat","r")as f2:
        with open ("T.dat","w") as f3:
            a=[]
            for i in f1:
                a.append(i)
            b=[]
            for i in f2:
                b.append(i)
            c=[]
            for i in range(0,1000000):
                c.append(float(a[i])+float(b[i]))    
            for i in range(0,1000000):
                f3.write(f"{c[i]}\n")