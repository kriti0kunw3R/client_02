st = {1,12,24,20,19}
st2 = {23,11,10,19}
print(type(st))
print(type(st2))
U = st.union(st2)
print(U)
T = st.intersection(st2)
print(T)

if T=={19}:
    print("U are Right!!!")
else:print("Nope")