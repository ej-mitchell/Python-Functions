def reverse(text):
   i=len(text)
   backward=""
   while i>0:
       i-=1
       backward+=text[i]
       if i==0:
           return backward
           break