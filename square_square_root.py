import numpy as np

#This function will compute the formula in the assignment up to a maximum N
def compute_first_N(N):
    res=1
    for i in range(N):
        #We work from the inside outwards
        n=N-i
        #The smallest possible n is for sqrt(1+2), which is n=2
        if n==1:
            break
        res = np.sqrt(1+n*res)
    return res

if __name__=="__main__":
    print '\nWe will numerically evaluate the expression:\n\t sqrt( 1 + 2 sqrt( 1 + 3 sqrt( 1 + 4 sqrt(...) ) ) )\n'
    oldres = 0
    #If no convergence after 300 terms, probably it's divergent
    for i in range(300):
        #We were shown 4 terms in the assignment, so we'll start with that
        if i<4:
            continue
        res = compute_first_N(i)
        #We will stop when we get a convergence within 0.1%
        if abs(res-oldres)/(0.5*(res+oldres))<0.001:
            print 'The estimated result is',res,'obtained after',i,'terms'
            break
        oldres = res
    print '\nSurprised by the result? :)\n'
