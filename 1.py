def OddSum(a, n):
    odd = 0
    for i in range(n):
 
        # Loop to find even, odd Sum
        if i % 2 != 0:
            odd += a[i]

    print ("Odd index positions sum ", odd)
 
# Driver Function
 
arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
 
OddSum(arr, n)
