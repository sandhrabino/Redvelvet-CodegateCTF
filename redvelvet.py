from z3 import *
a=[]

s = Solver()
a= [BitVec("flag[%d]"%i,16) for  i in range (26)]

for i in range(26):
	s.add(a[i]>=32)
	s.add(a[i]<127)


s.add(a[0]*(((a[1]^a[0])+(a[0]^a[1]))*a[0])-a[1]==10858)  #w,h
s.add(a[0]>85)                                            
s.add(a[0]<=96)
s.add(a[1]>0x60)
s.add(a[1]<=0x6f)
s.add(a[1]%a[2] == 7)     #h,a
s.add(a[2]>0x5a)
s.add((a[2]/a[3])+(a[2]^a[3]) == 0x15)        #a,t
s.add(a[2]<0x59)
s.add(a[3]<0x77)
s.add(((a[4]^(a[3]^a[4]))%a[4])+a[3]==0x89)      #t,_
s.add(a[4]==0x5f)
s.add(a[3]>0x73)
s.add(((a[4]^a[5])^a[4])^(a[4]+a[5])==0xe1)       #_,Y
s.add(a[5]<0x59)                     
s.add(a[5]>0x55)
s.add(a[5]<a[6])
s.add(a[6]>0x6e)
s.add(a[7]>0x73)
s.add(a[6]<a[7])
s.add((a[6]+a[7])^(a[5]+a[6])==0x2c)         #Y,o,u
s.add(((a[6]+a[7])%a[5])+a[6]==0xa1)
s.add(a[7]<0x77)
s.add(a[7]>a[8])
s.add(a[8]>a[9])
s.add(a[8]>0x5a)
s.add(a[9]<0x59)
s.add(a[9]<=a[10])
s.add((a[7]+a[9])^(a[8]+a[9])==0x7a)         #u,_,W    
s.add(((a[7]+a[9])%a[8])+a[9]==0x65)

s.add(((a[9]+a[10])/a[11])*a[10]==0x61)       #W,a,n
s.add(((a[9]-a[10])^a[11])*a[10]==0xfffd898)
s.add(a[11]<0x72)
s.add(a[10]<a[11])
s.add(a[11]==a[12])
s.add(a[12]>a[13])
s.add(((a[13]-a[12])*a[11])+a[13]-a[11]==0xffffa5d)    #a,n,n
s.add(a[14]>0x5a)
s.add(a[14]<0x5f)
s.add(a[13]>a[14])
s.add(a[13]<0x5f)
s.add(((1+a[13]+a[15])*a[14])-a[15]==0x3c9a)         #a,_,B
s.add(a[14]>=a[15])
s.add((a[16]-a[17])^a[16]-a[17]==0x46)
s.add(((a[16]+a[17])/a[15])+a[15]==0x44)      #B,e,?
s.add(a[16]>a[15])
s.add(a[15]>a[17])
s.add(a[16]>0x64)
s.add(a[16]<0x68)
#17,18,19 th charecters are being checked by function 12 
s.add(((a[19]+a[18])^a[18])+a[17]-a[19]==0x6f)      #),_,l
s.add(((a[18]-a[19])^a[18])+a[18]==0x65)
s.add(a[19]<=0x2c)
s.add(a[17]>a[18])
s.add(a[18]>a[19])
s.add(a[18]<0x3b)
s.add(a[19]<a[20])
s.add(a[20]<a[21])
s.add(a[19]>0x28)
s.add(a[20]>0x5a)
s.add(a[21]<0x6d)
s.add(((a[19]+a[21])^a[20])-a[19]==0x10d)
s.add(((a[20]-a[19])^a[21])+a[20]==0xb9)
s.add((a[21]+a[22])^a[22]+a[21]-a[23]==0xb9)
s.add(a[21]>a[23])
s.add(a[23]>0x5a)
s.add(a[22]<0x63)
s.add(a[22]>a[23])
s.add(a[24]>=a[23])
s.add(a[24]<0x6d)
s.add(a[24]>a[25])
s.add(a[25]>0x5f)
s.add((((a[24]-a[23])*a[24])^a[25])-a[23]==0x4be)
s.add(((a[25]-a[24])*a[25]^a[23])+a[24]==0xfffffbf6)

print s.check()
print s.model()
flag = ''.join([chr(int(str(arr(a[i])))) for i in range(0,26)])
print flag
