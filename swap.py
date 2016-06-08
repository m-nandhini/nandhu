def oddswap(st):
    s = list(st)
    for c in range(0,len(s),2):
        t=s[c]
        s[c]=s[c+1]
        s[c+1]=t

    return "".join(s)
def evenswap(str):
  	m=list(str)
	  for n in range(0,len(m),2):
		    te=m[n]
		    m[n]=m[n+1]
	     	m[n+1]=te
	   return "".join(m)	
