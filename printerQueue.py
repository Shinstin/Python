import queue as Q

class ITEM :
    def __init__(self, priority, target):
        self.priority = priority
        self.target = target

def getTime() :
    args = input().split()
    pos = int(args[1])
    pque = Q.PriorityQueue()
    que = Q.Queue()

    priorlist = input().split()
    order = 0
    for prior in priorlist :
        que.put(ITEM(int(prior), pos == order))
        pque.put(-int(prior))
        order = order + 1

    time = 0
    while pque.empty != False :
        target = pque.get()
        while que.empty != False :
            item = que.get()
            if -target == item.priority :
                time = time + 1
                if item.target == True :
                    return time
                else :
                    break
            else :
                que.put(item)

if __name__ == "__main__" :
    tcnum = int(input())
    for i in range(tcnum) :
        print(getTime())