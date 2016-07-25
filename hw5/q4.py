# a
def next_row(lst):
    temp_lst = [0] +lst +[0]
    next_row = []
    for i in range(len(lst) + 1):
        next_row += [temp_lst[i] + temp_lst[i+1]]
    return next_row

# b   
def generate_pascal():
    row_i = [1]
    while True:
        yield row_i
        row_i = next_row(row_i)
        
# c
def generate_bernoulli():
    row_i = [1]
    while True:
        yield [sum(row_i[:k+1]) for k in range(len(row_i))]
        row_i = next_row(row_i)
        
