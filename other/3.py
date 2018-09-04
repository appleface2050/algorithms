def cmp_to_symbol(val, other_val):
    '''returns the symbol representing the relationship between two values'''
    return (val > other_val) - (val < other_val)

if __name__ == '__main__':
    print cmp_to_symbol(2,2)
