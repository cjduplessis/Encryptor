class Base_X_Number:

    def __init__(self, int_value, base = 10):
        self.base = base
        self.int_value = int_value 

        if base < 2 or base > 64:
            raise Exception('Invalid base specified. '
                            'Base cannot be less than 2 or greater than 64')
        
        #if not(valid(int_value, base)):
        #    raise Exception('Invalid characters in number ' +
        #                    str(int_value) +
        #                    'for a base ' + str(base) + ' number')

    def __get_symbol(self, int_value):

        if int_value < 0:
            int_value = -int_value

        if int_value < 10:
            return str(int_value)

        if 10 <= int_value <= 35:  
            return chr(int_value + 55)

        if 36 <= int_value <= 61:
            return chr(int_value + 61)

        if int_value == 62:
            return chr(35) # '#'

        if int_value == 63:
            return chr(64) # '@'

    @staticmethod
    def to_base_x():
        res = ''
        N = self.int_value
        while N >= self.base:
            res = self.__get_symbol(N % self.base) + res
            N = N // self.base
        res = self.__get_symbol(N) + res
        return res
    
    def __repr__(self):
        return self.__to_base_x()

    def __str__(self):
        return self.__to_base_x()
    
def main():
    n = Base_X_Number(int(177166336026747270040),8)
    print(n, len(str(n)))
    
if __name__=="__main__":
    main()
