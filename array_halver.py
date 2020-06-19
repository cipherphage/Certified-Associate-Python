from functools import reduce

# this one was not part of the course, just seemed fun
# given an array (list) of integers find the halfway
# point defined by the sum of the integers and return
# a tuple containing the halved arrays
# if the halfway point is not exact then return a tuple
# containing the halved arrays with the first half larger
# than the second half (in sum)

# example: [1,2,7,4,2,4] => ([1,2,7],[4,2,4])  
# total sum = 20, each half sum = 10

# example: [1,2,7,4,2,4,5] => ([1,2,7,4],[2,4,5]) 
# total sum = 25, first half sum = 14, second half sum = 11

def halfSumFunc(arr):
    total_sum = 0
    sum_list = []

    for i in range(len(arr)):
        total_sum += arr[i]
        sum_list.append(total_sum)

        if i == len(arr)-1:
            # coerce to int to round floats down
            half_sum = int(total_sum / 2)
            # assign si variable otherwise UnboundLocalError
            si = 0
            
            try:
                si = sum_list.index(half_sum)
            except(ValueError):
                # using reduce here is not great because it will traverse the entire array
                # let's use another for loop instead and break when we reach the condition
                # other_sum = reduce((lambda a,b: b if (a < half_sum and half_sum < b) else a), sum_list)
                for j in range(len(sum_list)):
                    if j < len(sum_list):
                        if sum_list[j] < half_sum and half_sum < sum_list[j+1]:
                            other_sum = sum_list[j+1]
                            si = sum_list.index(other_sum)
                            break

            sip = si+1
            return (arr[0:sip], arr[sip:])
        
    return ([],[])

ans1 = halfSumFunc([1,2,7,4,2,4])
ans2 = halfSumFunc([])
ans3 = halfSumFunc([3])
ans4 = halfSumFunc([1,2,7,4,2,4,5])
ans5 = halfSumFunc([1,1,1,1])
ans6 = halfSumFunc([7,2,4,7,2,45,78,1,34,89,83,5,7])

# this is an interesting case, how to handle it?
ans7 = halfSumFunc([0,0,0,0,0])

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
print(ans6)
print(ans7)