class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_set = set()
        self.num_list = list()
        self.remove_count = 0
    
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.num_set:
            return False
        self.num_set.add(val)
        self.num_list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.num_set:
            return False
        self.num_set.remove(val)
        self.remove_count += 1    
        if self.remove_count > len(self.num_list) // 2:
            self.rebuild_list()
        return True
        
    def rebuild_list(self) -> None:
        self.remove_count = 0
        self.num_list = list(self.num_set)
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        while True:
            choice_idx = random.randrange(0, len(self.num_list), 1)
            choice = self.num_list[choice_idx]
            if choice in self.num_set:
                return choice