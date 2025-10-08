"""(i) Create a list spanning 1 to 50 using list comprehension method. Call this list a.
(ii) Slicing with positive step:
(a) a[1:5]
(b) a[3:20:2]
(c) a[::2]
(d) a[::]
(e) a[10::2]
(f) a[1:1:1]
(g) a[:0:]
(h) a[-7::1]. Is the output a non-empty list? Why did this work?
(i) a[-6:]
(j) a[-10:-4]
(iii) Slicing with negative step:
(a) a[::-1]
(b) a[::-3]
(c) a[:1:-2]
(d) a[-1:-1:-1]
(e) a[:-5:-1]
(f) a[:0:-1]
(g) a[:-1:-1]
(h) a[0:-5:-1]
(i) a[-1:5:-1]
(j) a[2:2:-1]
(k) a[2:1:-1]
(l) a[0:-5]
(iv) Modification of lists using list slicing:
(a) Create a list of even numbers from a using list slicing technique.
(b) Create a new list from a by choosing the first 10 numbers, then the even
numbers from 35-50."""
#(i)
a=[ i for i in range(1,51)]
print(a)

#(ii)
#(a)
print(a[1:5],f"Start={a[1]} , Stop={a[5-1]} , Step=0")

#(b)
print(a[3:20:2],f"Start={a[3]} , Stop={a[20-1]} , Step=2")

#(c)
print(a[::2],f"Start=No value given that's why it will start from the beginning => {a[0]} , Stop=No value given that's why by default it will go till the end=> {a[48]}, Step=2")

#(d)
print(a[::],f"Start={a[0]} , Stop={len(a)} , Step=0")

#(e)
print(a[10::2],f"Start={a[10]} , Stop={len(a)},here it will go till the end as no value is given , Step=2")

#(f)
print(a[1:1:1],f"Start={a[1]} , Stop={a[1]} , Step=1, It gave no result and an empty list because the value of start and stop is the same")

#(g)a[:0:]
print(a[:0:],f"Over here we again got an empty list because the stop index is set to 0")

#(h)
print(a[-7::1],f"Start={a[-7]},Stop index is taken as default as no value is specified= {len(a)}, Step =2")

#(i)
print(a[-6:],f"Start={a[-6]}, Stop={len(a)}")

#(j)
print( a[-10:-4],f"Start={a[-10]},Stop={a[-4-1]}")

#(iii)
#(a) a[::-1]
print(a[::-1],f"In here since no values are given by default the whole list will be considered from the beginning to the end but as the Step=-1 it will get reversed")

#(b)a[::-3]
print(a[::-3],f"Start={a[-1]}, Stop={a[-50]}, Step=-3")

#(c) a[:1:-2]
print(a[:1:-2],f"Start={a[-1]}, Stop={a[1]},Step=-2")

#(d) a[-1:-1:-1]
print(a[-1:-1:-1],f"Start={a[-1]}, Stop={a[-1]},Step=-1. Since the start and stop index are the same we got an empty list.")

#(e)a[:-5:-1]
print(a[:-5:-1],f"Start={a[-1]}, Stop={a[-5]} , Step=-1")

#(f) a[:0:-1]
print(a[:0:-1],f"Start={a[-1]}, Stop={a[0]} , Step=-1")

#(g) a[:-1:-1]
print(a[:-1:-1],f"Start={a[-1]}, Stop={a[-1]},Step=-1")

#(h) a[0:-5:-1]
print(a[0:-5:-1],f"Start={a[0]} , Stop={a[-5]} , Step=-1")

#(i) a[-1:5:-1]
print( a[-1:5:-1],f"Start={a[-1]},Stop={a[5]} , Step=-1")

#(j) a[2:2:-1]
print( a[2:2:-1],f"Start={a[2]} , Stop={a[2]} , Step=-1")

#(k) a[2:1:-1]
print( a[2:1:-1],f"Start={a[2]} , Stop={a[1]}, Step=-1")

#(l) a[0:-5]
print(a[0:-5] ,f"Start={a[0]} , Stop={a[-5]}")

"""(iv) Modification of lists using list slicing:
(a) Create a list of even numbers from a using list slicing technique.
(b) Create a new list from a by choosing the first 10 numbers, then the even
numbers from 35-50."""

#(a)
a2=[i for i in a[1::2]]
print(a2)
print(f'The list of even numbers:{a2}')

#(b)
b=[]
a=[b.append(j) for j in a[0:10]] + [b.append(i) for i in a[35:51] if i%2==0 ]
print(b)
