# Jennifer Ly, grudat20 uppg 6.2

scarves = {}                                    # key=length n, value=number of scarves with length n

def p_memo(n):
    # Creates the given h-vector 
    h1 = [0, 2, 5, 6, 9]
    h2 = (n-4)*[0]
    h = h1 + h2 

    # Calculates the maximume revenue  
    if n==0:
        return 0
    else:
        revenue = []
        for i in range(1, n+1):    
            numb = h[i]+p_memo(n-i)
            revenue.append(numb)
            if i not in scarves.keys():         # if a scarf of length i has NOT been created before 
                scarves[i] = 1                  
            else:                               # if already a scarf of length i has been created before
                scarves[i] += 1                 
    return max(revenue)

def p(n):
    # Creates the given h-vector 
    h1 = [0, 2, 5, 6, 9]
    h2 = (n-4)*[0]
    h = h1 + h2 
    
    r = list(range(0,n+1)) # Array for revenue
    s = list(range(0,n+1)) # Array for cuts
    r[0] = 0
    revenue = []


    for j in range(1,n+1):
        x = 0
        for i in range(1,j+1):
            if x < (h[i] + r[j-i]):
                x = (h[i] + r[j-i])
                s[j] = i
        r[j] = x
    i = n
    revenue.append(r[n]) # Maxmimal revenue
    while i > 0:
        revenue.append(s[i]) 
        i -= s[i]
    return revenue 

def message(n,a,b):
    """Output message"""
    return (" " + str(n) + a + str(p(n)[0]) + b + str(p(n)[1:]))

def output(n):
    if n < 4:
        print(message(n,"        ", "      "))
    elif 4 <= n <= 9:
        print(message(n,"        ", "     "))
    elif n > 9:
        print(message(n,"       ", "     "))
        
def main():
    print("Length  Profit  Cuts - [1, 2, 3..., n]")
    for n in range(21):
        output(n)

if __name__ == "__main__":
    main()     

# def info(scarves, revenue):
#     print("For the maximume revenue", revenue)
#     for key in scarves.keys():
#         print(scarves[key],"scarves of length", key, "m were produced")


# >>> info(scarves, p_memo(5))
#For the maximume revenue 12
#16 scarves of length 1 m were produced
#8 scarves of length 2 m were produced
#4 scarves of length 3 m were produced
#2 scarves of length 4 m were produced
#1 scarves of length 5 m were produced
