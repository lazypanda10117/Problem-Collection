class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Troll solution
        # We define a hash function that uniquely maps string upto permutation isomorphism to the same value
        # We are leveraging the python built-in bignum implementation
        # We also make use of the english letter frequency in common english words
        PRIME_LETTER_MAP = dict(
            e=2,
            t=3,
            a=5,
            o=7,
            i=11,
            n=13,
            s=17,
            h=19,
            r=23,
            d=29,
            l=31,
            c=37,
            u=41,
            m=43,
            w=47,
            f=53,
            g=59,
            y=61,
            p=67,
            b=71,
            v=73,
            k=79,
            j=83,
            x=89,
            q=97,
            z=101
        )
        
        def uniquePermHash(s):
            result = 1
            for c in s:
                result *= PRIME_LETTER_MAP.get(c)
            return result
        
        result_dict = dict()
        
        for s in strs:
            hash_val = uniquePermHash(s)
            if hash_val in result_dict:
                result_dict[hash_val].append(s)
            else:
                result_dict[hash_val] = [s]
        
        return [r for r in result_dict.values()]
