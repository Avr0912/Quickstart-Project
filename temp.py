import os

#queue and priority queue functions
def enqueue(arr, val):
    arr.append(val)

def pq_enqueue(arr, val):
    if isEmpty(arr):
        arr.append(val)
        return
    for x in range(len(arr)):
        if(cmpPriority(arr[x], val)):
            arr.insert(x, val)
            return
    arr.append(val)     

def dequeue(arr):
    if isEmpty(arr):
        print("Error: attempting to dequeue empty queue")
        return None
    toRet = arr.pop(0)
    return toRet

def peek(arr):
    if isEmpty(arr):
        print("Error: peeking empty queue")
        return None
    return arr[0]

def isEmpty(arr):
    if len(arr) == 0:
        return True
    return False

#stack functions
def pop(arr):
    if isEmpty(arr):
        print("Error: attempting to pop empty stack")
        return None
    return arr.pop()

def push(arr, val):
    arr.insert(0, val)



#string functions   
def getPriority(str):
    if str == "":
        print("Error: empty string")
        return str
    index = str.rindex(",")+2
    return str[index:]

def cmpPriority(str1, str2):
    p1 = getPriority(str1)
    p2 = getPriority(str2)
    return p1>p2


#build methods
def build_queue(arr, filename):
    with open(filename, 'r') as file:
        for line in file:
            l = line.strip()
            enqueue(arr, l)

def build_pq(arr, filename):
    with open(filename, 'r') as file:
        for line in file:
            l = line.strip()
            pq_enqueue(arr, line)

def build_stack(arr, filename):
    with open(filename, 'r') as file:
        for line in file:
            l = line.strip()
            push(arr, l)

#process methods
def process_queue(arr):
    while not isEmpty(arr):
        task = dequeue(arr)
        taskName = task[:task.find(",")]
        print("Running $" + taskName)

def process_stack(arr):
    while not isEmpty(arr):
        task = pop(arr)
        taskName = task[:task.find(",")]
        print("Running $" + taskName)



l = []
inputs = {"0", "1", "2"}
ds = input("Choose your data structure\n0:Stack\n1:Queue\n2:Priority Queue\n")
if ds not in inputs:
    print("Error: Invalid input")
    exit()

filename = input("Input filename\n")
if(not os.path.exists(filename)):
    print("Error: File does not exist")
    exit()

if ds == "0":
    build_queue(l, filename)
    l.reverse()
    process_stack(l)

if ds == "1":
    build_queue(l, filename)
    process_queue(l)

if ds == "2":
    build_queue(l, filename)
    l.sort(reverse=False, key=getPriority)
    process_queue(l)