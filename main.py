# python3
#Vladislavs Sidorkins 221RDB070

def parallel_processing(n, m, data):
    flow=[0]*n
    output = []
    
    for i, dat in enumerate(data):
        mainiga= min(range(n), key=flow.__getitem__)
        output.append((mainiga,flow[mainiga]))
        flow[mainiga] +=dat

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = map(int,input().split())
    
    data =list(map(int,input().split()))
    result = parallel_processing(n,m,data)




    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    

    for flow,mainiga_time in result:
        print(flow,mainiga_time)
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
