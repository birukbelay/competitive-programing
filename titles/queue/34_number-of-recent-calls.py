# https://leetcode.com/problems/number-of-recent-calls/


class RecentCounter:
    counter=0
    pings=[]
    sums=0
    def __init__(self):
        self.counter=0
        self.pings=[]        
        self.sums=0   

    def ping(self, t: int) -> int:
        self.pings.append(t)
        print("t===>",t)
        print("values==> sums-",self.sums,"counter-",self.counter, "pings=", self.pings)
        for i in reversed(self.pings):
            print("      *** in loop - i=",i, "ctr=", self.counter, "sums-",self.sums)
            if self.sums>=3000:
                val=self.counter
                self.sums=0
                self.counter=0
                return  val
                
                
            self.sums+=i
            print("sums=",self.sums)         
            
            self.counter+=1
            print("counter=",self.counter)
        val=self.counter
        self.sums=0