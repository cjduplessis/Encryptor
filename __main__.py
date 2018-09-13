import random
import math
import functools

def modular_sum(n, b):

    int_val = int(n)
    transform = []    
    while int_val > 0:
        transform.insert(0, int_val % b)
        int_val = int_val // b
    return transform

def modular_sum_inv(m, b):

    value = 0   
    for idx in range(0,len(m)):
        value += int(m[idx])*(b**idx)      
    return value

def to_ordinal_string(string):
    if string:
        result = ''
        for character in string:
            ascii_value = ord(character)
            padded_int = str(ascii_value).zfill(3)
            result += padded_int
        return result
    return

def add_hash(text):

    text_len = len(text)
    hash_len = text_len * 256
    
    hash_digits = []
    for i in range(0, hash_len):
        hash_digits.append(str(random.randint(0,9)))

    start_idx = random.randint(0, hash_len - 1)
    for i in range(0, len(text)):
        idx = (start_idx + i) % hash_len
        hash_digits[idx] = text[i]
    
    return functools.reduce(lambda x,y: x + y, hash_digits), start_idx

def main():
    while True:
        text = input('Input some text to encrypt: ')
        ord_string = to_ordinal_string(text)

        pre_key_list = []
        for i in range(0, 2):
            base = random.randint(11, math.ceil(math.sqrt(int(ord_string))))
            pre_key_list.append(base)
            m = modular_sum(ord_string, base)
            grp = random.randint(0, len(m) - 1)
            pre_key_list.append(grp)
            del m[grp]
            ord_string = str(modular_sum_inv(m, base))

        print(add_hash(ord_string))
    
      
if __name__ == "__main__":
    main()
