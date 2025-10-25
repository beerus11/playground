class NestedLstItr:
    def __init__(self,lst):
        self.lst = lst
        self.st = [(self.lst,0)]
        self.__process_list()

    def __process_list(self):
        while self.st:
            lst,top_idx = self.st[-1]
            if len(lst) <= top_idx:
                self.st.pop()
                continue
            curr = lst[top_idx]
            if isinstance(curr,int):
                return True
            else:
                self.st[-1] = (lst, top_idx + 1)
                self.st.append((curr,0))
        return False


    def has_next(self):
        self.__process_list()
        return bool(self.st)

    def next(self):
        if not self.has_next():
            raise Exception("No element found")
        lst, idx = self.st[-1]
        self.st[-1] = (lst, idx + 1)
        return lst[idx]

t1 = [[1,2,3],[4,5,6,[7,8,9,[10,11,12]]]]
itr = NestedLstItr(t1)

while itr.has_next():
    print(itr.next())