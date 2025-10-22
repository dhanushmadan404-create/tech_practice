fruits = ("apple", "banana", "cherry", "mango", "banana")
def act1(f):
    b=[]
    # act1=1
    print(len(f))
    print("")
    # act1=2
    for i in f[1]:
        print(i)
        print("")
    # act1=3
    # f[3]="grape"#output:error
    # act1=4
    b=list(f)
    print(b)


act1(fruits)