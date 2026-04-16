def e(t,k):
    if len(t)%2:t+='X'
    r=''
    for i in range(0,len(t),2):
        a,b=ord(t[i])-65,ord(t[i+1])-65
        r+=chr((k[0][0]*a+k[0][1]*b)%26+65)
        r+=chr((k[1][0]*a+k[1][1]*b)%26+65)
    return r

def d(t,k):
    det=(k[0][0]*k[1][1]-k[0][1]*k[1][0])%26
    di=pow(det,-1,26)
    k=[[k[1][1]*di%26,-k[0][1]*di%26],
       [-k[1][0]*di%26,k[0][0]*di%26]]
    return e(t,k)

k=[[3,3],[2,5]]
c=e("HELP",k)
print(c,d(c,k))