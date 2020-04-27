# Take input from matrix and calculate the Individual repeated Number of Column as well As Row also calculate Trace of The Matrix(Diagonal addition).

def count(x):
    print('************************')
    print(x)
    _size = len(x)
    repeated=[]
    for i in range(_size):
        l=i+1
        for j in range(l, _size):
            if(x[i] == x[j] and x[i] not in repeated):
                repeated.append(x[i])
    
    print("The Total  Repeated no.are:",len(repeated))
    

def check(data):
    r=[]
    for i in data:
        print(i)
        r.append(i)
    count(data)
    r.clear()    
    data.clear()

    

    

def calculate(matrix):
    print('***************************************')
    data=[]
    for i in matrix:
        print(i)
    
    n=0
    for i in range(0,len(matrix),1):
        for i in matrix:
            #print(i[n])
            data.append(i[n])
        n+=1
        userip=input('Want to Count no. of repeated no in row/columns(Type Y):')
        if(userip=='y'or userip=='Y'):
            check(data)
        else:
            exit                


r=0
def proceed(matrix):
    counter=0
    for i in matrix:
        for j in matrix:
            val=int(input('Enter the element(row-wise input):'))
            i.append(val)
            counter+=1
            if(counter==4):
                print('**************enter the elements for another row****************')
                counter=0
    for i in range(0,2,1):
        ip=int(input("want check for Column or column(row=1/column and Trace of matrix=2):"))
        if(ip==1):
            print("Matrix is:")
            for i in matrix:
                print(i)
            for i in matrix:
                count(i)

        elif(ip==2):
            i=0
            k=0
            for m in matrix:
                k+=m[i]
                i+=1
    
            
            print('*****************************')
            calculate(matrix);
            
            print('The Trace of Matrix is:',k)
        else:
            print('******error********')


def compute(testcase,N_size):
    matrix=[]
    print("The Test Case No. is:",testcase)
    for i in range(0,N_size,1):
        a=[]
        matrix.append(a)
    ip=input('Want to Proceed for Taking Input(y=yes):')
    if(ip=='y' or ip=='Y'):
        proceed(matrix);
    else:
        exit
        

ip=int(input('On how many Matrices Do you Want to Perform Operation:'))
for i in range(0,ip,1):
    testcase=int(input('Enter the No of Test Case:'))
    N_size=int(input('The Size of the Matrix is(nxn):'))
    compute(testcase,N_size)
