# python3
#Vladislavs Sidorkins 221RDB070

def parallel_processing(n, m, data):
    flow=[0]*n
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    for i in range(m):
        j=0
        while j<n and flow[j]>0:
            j+=1
        
        if j==n:
            wait=min(flow)
            flow=[change - wait for change in flow]
            j=flow.index(0)
        flow[j]=data[i]
        output.append([j,sum(flow[:j+1])])

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int,input().split())
    
    data =list(map(int,input().split()))




    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)

    for i,j in result:
        print(i,j)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
