import random
import math
import matplotlib.pyplot as plt

def monte_carlo(n):
    a = []
    nc = 0
    for i in range(n):
        row = []
        row.append(random.uniform(-1,1))
        row.append(random.uniform(-1,1))
        a.append(row)

    for i in range(n):
        k = math.sqrt(a[i][0]*a[i][0] + a[i][1]*a[i][1])
        if k<1:
            nc+=1

    pi = (4*nc)/n
    pii = math.pi
    print('pi for {} points : {}'.format(n,pi))
    print('pi using built-in function : {}'.format(pii))

    plt.scatter([i[0]  for i in a if math.sqrt(i[0]*i[0] + i[1]*i[1]) > 1],[i[1] for i in a if math.sqrt(i[0]*i[0] + i[1]*i[1]) > 1],color = "red")
    plt.scatter([i[0]  for i in a if math.sqrt(i[0]*i[0] + i[1]*i[1]) < 1],[i[1] for i in a if math.sqrt(i[0]*i[0] + i[1]*i[1]) < 1],color = "blue")
    plt.title('n='+str(n)+'  pi='+str(pi))
    #plt.savefig(str(n)+'.png')
def main():
    a = [1000,10000,100000]
    for n in a:
        monte_carlo(n)

if __name__ == "__main__":
    main()


for i in range(n):
        k=0
        for j in range(d):
            k += a[i][j]*a[i][j]
        if k<1:
            nc += 1