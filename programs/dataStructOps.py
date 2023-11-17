l = [1,2,3,4]
t = (2,3,4,5)

# ---------------------------------------
# del l
# print(l) - err after deleting l (del l)

# del l[3]
# print(l)

# del l[5] #IndexError: list assignment index out of range

# l = []
# del l # no err
# ---------------------------------------

# l.pop() #pops last item; l = [1,2,3]
# print(l.pop()) #l = [1,2,3, 4] =>#4
# l.pop()
# print(l)

# print(l.pop(2)) #3
# print(l) #[1,2,4]
# ---------------------------------------
# l.remove(3)
# print(l) #[1, 2, 4]

# print(l.remove(3)) #None

# l.remove() #typeerror - needs argument
# l.remove(5) #ValueError: list.remove(x): x not in list
# ---------------------------------------
# print(l.clear()) #None

# l.clear()
# print(l) #[]
# ---------------------------------------

s = {3,4,5,6,7}

# del s
# print(s) #NameError: name 's' is not defined

# del s[1] #TypeError: 'set' object doesn't support item deletion
# ---------------------------------------
# s.pop()
# print(s) #removes random values
# s.pop()
# print(s) #removes random values
# ---------------------------------------
# s.remove(4)
# print(s) #{3, 5, 6, 7}

# s.remove(10) #KeyError: 10
# ---------------------------------------
# print(s.discard(4)) #None 
# print(s) #{3, 5, 6, 7}

# s.discard(10) # doesn't return error
# print(s) #{3, 4, 5, 6, 7}
# ---------------------------------------
# s.clear()
# print(s) #set()
# ---------------------------------------


d = {1:2, 3:4, 5:6, 7:8}
# ---------------------------------------
# del d
# print(d)

# del d[2] #KeyError: 2

# del d[3]
# print(d) #{1: 2, 5: 6, 7: 8}
# ---------------------------------------
# d.pop() #TypeError: pop expected at least 1 argument, got 0

# print(d.pop(3)) #4
# print(d) #{1: 2, 5: 6, 7: 8}

# d.pop(4) #KeyError: 4,  if key is not found & default val isnt given=>err

# print(d.pop(4, -1)) #-1; if key is not found & default val is given, then that val displayed
# print(d) #{1: 2, 3: 4, 5: 6, 7: 8}
# ---------------------------------------
# d.clear()
# print(d) #{}
# ---------------------------------------
# d.popitem()
# print(d) #{1: 2, 3: 4, 5: 6}

# d.popitem(1) # takes no argument

# d = {}
# d.popitem() #KeyError: 'popitem(): dictionary is empty'
# ---------------------------------------

