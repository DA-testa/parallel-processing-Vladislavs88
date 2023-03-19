# python3
#Vladislavs Sidorkins 221RDB070

def parallel_processing(n, m, data):
    flow=[0]*n
    output = []
    int1 =0
    int2 =0
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
        while int<m:
            for i in range(n):
                if flow[i]==0 and int1 <m:
                    flow[i] = data[int1]
                    output.append([i,int2])
                    int1 +=1
            int2 +=1
            flow=[mainiga-1 if mainiga >0 else = for mainiga in flow]
#             j+=1
        
#         if j==n:
#             wait=min(flow)
#             flow=[change - wait for change in flow]
#             j=flow.index(0)
#         flow[j]=data[i]
#         output.append([j,sum(flow[:j+1])])

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

    for rez in result:
        print(rez[0],rez[1])
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
