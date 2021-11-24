 
class ClosedHash():
    def __init__(self, size):
        self.size = size
        self.empty = []
        self.deleted = ["*","*"]
        self.dictionary = [0 for _ in range(size-1)]
        self.map = {}
        for _ in range(size):
            self.map[_] = []

    def insert(self, x):
        key, value = x
        if (self.map[self.find(key, value)] == x):
            return 
        bucket = self.locate(key, value)   
        if(self.map[bucket] == self.empty or self.map[bucket == self.deleted]):
            self.map[bucket] = [key, value]
        else:
            raise ValueError("Table is full")
        
    def locate(self, key, value):
        initial = self.h(key)
        i = 0

        while (i < self.size and (self.map[(initial+i) % self.size] != [key, value]) and (self.map[(initial+i) %self.size] != self.empty) ):
            if(self.map[(initial+i) %self.size] == self.deleted):
                return ((initial + i) % self.size)
            i = i+ 1
        return ((initial + i) % self.size)

    def h(self, x):
        sum = 0
        for i in range(len(x)):  
            sum = sum + ord(x[i])
        h = sum % self.size
        return h

    def find(self, key, value):
        initial = self.h(key) 
        i = 0  
        while (i < self.size and (self.map[(initial+i) % self.size] != [key, value]) and (self.map[(initial+i) %self.size] != self.empty) ):
            i = i+ 1
        return ((initial + i) % self.size)

    def get_key(self, key):
        initial = self.h(key) 
        i = 0   
        while (i < self.size):
            if(len(self.map[(initial+i) % self.size]) > 0):
                if((self.map[(initial+i) % self.size][0] == key)):
                     return ((initial + i) % self.size) 
            i = i+ 1
        return ((initial + i) % self.size)
    
    def __getitem__(self, key):
        initial = self.h(key) 
        i = 0   
        while (i < self.size):
            if(len(self.map[(initial+i) % self.size]) > 0):
                if((self.map[(initial+i) % self.size][0] == key)):
                     return self.map[((initial + i) % self.size) ][1]
            i = i+ 1
        return self.map[ ((initial + i) % self.size)][1]

    def delete(self, key, value):
        bucket = self.find(key, value)
        if self.map[bucket] == [key, value]:
            self.map[bucket] = self.deleted
        

    

