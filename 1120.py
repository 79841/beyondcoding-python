# N = int(input())
# for _ in range(N):

#     s = 0
#     a = 0

#     for e in input():
#         if e == "O":
#             a += 1
#             s += a
#         else:
#             a = 0
    
#     print(s)
while True:
    n = int(input())
    
    f = []

    if n == -1:
        break
    
    for i in range(1, n):
        if n % i  == 0:
            f.append(i)
    
    if sum(f) == n:
        output = f"{n} = {f[0]}"
        for i in range(1, len(f)):
            output += f" + {f[i]}"
        print(output)
        
    else:
        print(f"{n} is NOT perfect.")

