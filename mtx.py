class mtx() :

    s = '+'
    # initializes matrices
    def __init__(self, mtrs = [[]], m = 1, n = 1) :
        
        # checks if argument is a valid order
        if m <= 0 or n <= 0 :
            print("INVALID")
            return
        
        # creats empty matrices if no matrices argument is given
        elif mtrs == [[]] :
            ml = []
            for i in range(m) :
                for j in range(n) :
                    ml.append(' ')
                mtrs.append(ml)
                ml = []
        
        # checks if argument/created is a valid matrices
        for i in mtrs :
            if len(i) != len(mtrs[0]) :
                print("INVALID")
                mtrs = [[]]
                break
        self.mtrs = mtrs
    
    # checks if matrices is valid
    def isvalid(self) :
        for i in self.mtrs :
            if len(i) != len(self.mtrs[0]) :
                return(False)
        return(True)

    # return order of the matrices
    def order(self, o = 'mn') :
        m = len(self.mtrs)
        n = len(self.mtrs[0])
        if o == 'mn' :
            return(f"{m},{n}")
        elif o == 'm' :
            return(int(m))
        elif o == 'n' :
            return(int(n))
        else :
            return

    # prints matrices in proper format
    def display(self) :
        mstr = '| '
        for i in self.mtrs :
            for j in i :
                mstr += ' ' + str(j)
            print(mstr + ' |')
            mstr = '| '

    # returns transpose of the matrices
    def trans(self, o = 'dc') :
        trans_mtrs = []
        lm = []
        for i in range(self.order('n')) :
            for j in self.mtrs :
                lm.append(j[i])
            trans_mtrs.append(lm)
            lm = []
        if o == 'dc' :
            return(trans_mtrs)
        elif o == 'c' :
            self.mtrs = trans_mtrs
            return(self.mtrs)
        else :
            return
    
    # checks if matrices is a square matrices
    def issquare(self) :
        if self.order('m') == self.order('n') :
            return(True)
        else :
            return(False)

    # checks if matrices is a 2x2 matrices
    def istwo(self) :
        if (self.order('m') == 2) and (self.order('n') == 2) :
            return(True)
        else :
            return(False)

    # returns the determinant value of the matrices
    def det(self) :
        det_mtrs = 0
        n = 0
        m = []
        val = []
        if self.issquare() :
            if self.istwo() :
                det_mtrs = (self.mtrs[0][0] * self.mtrs[1][1]) - (self.mtrs[0][1] * self.mtrs[1][0])
                return(det_mtrs)
            else :
                for i in self.mtrs[0] :
                    if n == 0 :
                        for j in self.mtrs[1:] :
                            m.append(j[1:])
                    elif n == len(self.mtrs[0])-1 :
                        for j in self.mtrs[1:] :
                            m.append(j[:-1])
                    else :
                        for j in self.mtrs[1:] :
                            m.append(j[:n] + j[n+1:])
                    val.append(i * mtx(m).det())
                    m = []
                    n += 1
                for idx, i in enumerate(val) :
                    if idx%2 == 0 :
                        det_mtrs += i
                    else :
                        det_mtrs -= i
                return(det_mtrs)
        else:
            return('Invalid')

    # defines matrices addition
    def __add__(self, other) :
        sum_mtrs = []
        lm = []
        if self.order() == other.order() :
            for i in range(self.order('m')) :
                for j in range(self.order('n')) :
                    lm.append(self.mtrs[i][j] + other.mtrs[i][j])
                sum_mtrs.append(lm)
                lm = []
        else :
            sum_mtrs = [[]]
        return(sum_mtrs)

    # defines matrices subtraction
    def __sub__(self, other) :
        sub_mtrs = []
        lm = []
        if self.order() == other.order() :
            for i in range(self.order('m')) :
                for j in range(self.order('n')) :
                    lm.append(self.mtrs[i][j] - other.mtrs[i][j])
                sub_mtrs.append(lm)
                lm = []
        else :
            sub_mtrs = [[]]
        return(sub_mtrs)
    
    # defines matrices multiplication
    def __mul__(self, other) :
        mul_mtrs = []
        lm = []
        n = 0
        other_trans = other.trans()
        if self.order('n') == other.order('m') :
            for i in self.mtrs :
                for j in other_trans :
                    for k in range(self.order('n')) :
                        n += i[k] * j[k]
                    lm.append(n)
                    n = 0
                mul_mtrs.append(lm)
                lm = []
        else :
            mul_mtrs = [[]]
        return(mul_mtrs)

# DEBUGGING
#mtrs1 = mtx([[1, 2, 3], 
#            [4, 5, 6],
#            [7, 8, 9]])
#mtrs2 = mtx([[6, 1, 1], 
#            [4, -2, 5],
#            [2, 8, 7]])
#mtrs3 = mtx([[1, 2], 
#           [3, 4]])
# mtrs1.display()
# print(mtrs1.order())
# print(mtrs1.ifvalid())
# mtx(mtrs1 + mtrs2).display()
# mtx(mtrs1 - mtrs2).display()
# print(mtrs1.trans('c'))
# mtrs1.display()
# print(mtrs1.order())
# mtx(mtrs1 * mtrs3).display()
#print(mtrs1.det())
#print(mtrs2.det())
#print(mtrs3.det())
