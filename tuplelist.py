import sys
l1 =[1,2,3,4,5]
t1=(1,2,3,4,5)
print(sys.getsizeof(l1))
def append_into_list(value):
    print("address: ",id(l1))
    print("before size of list", sys.getsizeof(l1))
    l1.append(value)
    print("updated list: ",l1)
    print("address remains the same: ", id(l1))
    print("after size of list", sys.getsizeof(l1))

print(sys.getsizeof(t1))
def append_into_tuple(value):
    print("address: ",id(t1))
    print("before size of list", sys.getsizeof(t1))
    l1.append(value)
    print("updated list: ",t1)
    print("address remains the same: ", id(t1))
    print("after size of list", sys.getsizeof(t1))
append_into_list(6)
append_into_list(7)
append_into_list(8)
append_into_list(9)
append_into_list(10)
append_into_list(11)
append_into_list(12)
append_into_list(6)
append_into_list(7)
append_into_list(8)
append_into_list(9)
append_into_list(10)
append_into_list(11)
append_into_list(12)
print()
print()
print()
append_into_tuple(7)
append_into_tuple(6)
append_into_tuple(8)
append_into_tuple(9)
append_into_tuple(10)
append_into_tuple(11)
append_into_tuple(12)
append_into_tuple(6)
append_into_tuple(7)
append_into_tuple(8)
append_into_tuple(9)
append_into_tuple(10)
append_into_tuple(11)
append_into_tuple(12)
t2 = (1,)
print(t2)
x="I'm a string" 
print(x)