class Solution:    
    def num_layer(self, s):
        return len(s.split('\t'))-1
    
    def clean_name(self, s):
        return s.strip('\t')
    
    def is_file(self, s):
        return len(s.split('.')) >= 2
    
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split('\n')
        files = ['']
        stack = []
        
        for line in lines:
            cur_level = self.num_layer(line)
            while cur_level < len(stack):
                stack.pop()
            clean_name = self.clean_name(line)
            if self.is_file(clean_name):
                path = '/'.join(stack)
                path_name = f"{path}/{clean_name}" if path else clean_name
                files.append(path_name)
            else:
                # it is a directory
                stack.append(clean_name)
        
        return len(max(files, key=lambda s: len(s)))