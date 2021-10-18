queue = []
def enqueue_queue():
    element=input("Enter the element : ")
    queue.append(element)
    print(element,"is added in queue ")
def dequeue():
    if not queue:
        print("Queue is empty..")
    else:
        remove=queue.pop(0)
        print(remove,"is removed in queue")
def display():
    print(queue)
while True:
    print("Select the Operation \n1->Insert:\n 2-> Delete:\n 3->Display:\n 4->Exit:")
    num=int(input("Enter your choice: "))
    if  num==1:
        enqueue_queue()
    elif num==2:
        dequeue()
    elif num==3:
        display()
    elif num==4:
        break
    else:
        print("Select the correct operation ..")