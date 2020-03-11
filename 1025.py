def binary_search_iter(arr,n):
    start = 0
    end = len(arr)-1

    while(start<=end or end>=start):
        mid = (start+end)//2
        if(arr[mid] == n):
            while(mid > 0 and arr[mid-1] == n):
                mid = mid - 1
            return ('{} found at {}'.format(n,mid+1))
        elif(arr[mid]<n):
            start = mid+1
        else:
            end = mid-1
    return ('{} not found'.format(n))

times = 1
while True:
    marbles, num_ques = map(int,input().split())
    if(marbles == 0 and num_ques == 0):
        break
    print('CASE# {}:'.format(times))

    marbles_arr = []
    for i in range(marbles):
        marbles_arr.append(int(input()))
    marbles_arr.sort()

    for i in range(num_ques):
        num = int(input())
        print(binary_search_iter(marbles_arr,num))
    times+=1