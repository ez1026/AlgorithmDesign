import random

class TopN:
    # 父节点下标
    def parent(self, n):
        return int((n - 1) / 2)
 
    # 左节点下标
    def left(self, n):
        return 2 * n + 1
 
    # 右节点下标
    def right(self, n):
        return 2 * n + 2
 
    # 构建小顶堆，保证父节点小于左右子节点
    def buildHeap(self, n, data):
        for i in range(1, n):
            t = i
            # 调整堆，如果节点比父亲节点小，则交换
            while t != 0 and data[t] < data[self.parent(t)]:
                temp = data[t]
                data[t] = data[self.parent(t)]
                data[self.parent(t)] = temp
                t = self.parent(t)
        # print(data)
 
    # 调整data[i]
    def adjust(self, i, n, data):
        # 小于堆的根节点，不调整
        if data[i] <= data[0]:
            return
        
        # 置换堆顶
        temp = data[i]
        data[i] = data[0]
        data[0] = temp
        # 调整堆顶
        t = 0
        while (self.left(t) < n and data[self.left(t)] < data[t]) or (self.right(t) < n and data[self.right(t)] < data[t]):
            if self.right(t) < n and data[self.right(t)] < data[self.left(t)]:
                # 右孩子更小，置换右孩子
                temp = data[t]
                data[t] = data[self.right(t)]
                data[self.right(t)] = temp
                t = self.right(t)
            else:
                # 否则置换左孩子
                temp = data[t]
                data[t] = data[self.left(t)]
                data[self.left(t)] = temp
                t = self.left(t)
        # print(data)
 
    # 寻找topN，调整data，将topN排到最前面
    def findTopN(self, n, data):
        # 先构建n个数的小顶堆
        self.buildHeap(n, data);
        # n往后的数进行调整
        for i in range(n, len(data)):
            self.adjust(i, n, data)
        # print(data)
        return data[:n]
 
if __name__ == "__main__":
    # 第一组测试 12个
    arr1 = [58, 26, 45, 18, 22, 39, 96, 75, 80, 65, 63, 28]
    print("原数组：" + str(arr1))
    topn = TopN()
    result = topn.findTopN(5, arr1)
    print("数组进行Top-N调整：" + str(result))
 
    # 第二组测试 随机100000000个

    tempList = []
    for i in range(10000000):
        temp = random.randint(0, 100000000)
        tempList.append(temp)
    # print("原数组：" + str(tempList))
    topn = TopN()
    result = topn.findTopN(10, tempList)
    print("数组进行Top-N调整：" + str(result))


