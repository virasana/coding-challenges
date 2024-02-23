string = 'ABCDCDC'
sub_string = 'CDC'

# find CDC within string: expect: 2
print(sum(1 for i in range(len(string)) if string[i: i + len(sub_string)] == sub_string ))
