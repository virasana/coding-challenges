def count_substring(string, sub_string):
    substring_length = len(sub_string)
    return (
        sum(1 for i in range(len(string) - substring_length + 1) 
            if string[i:i + substring_length] == sub_string)
    )

string = 'ABCDCDC'
sub_string = 'CDC'
if __name__ == '__main__':
    count = count_substring(string, sub_string)
    print(count) 


# This uses while and string.find to do the same    
# def count_substring(string, sub_string):
#     count = 0
#     start = 0
#     while True:
#         start = string.find(sub_string, start)  # Find the next occurrence of the substring
#         if start == -1:
#             break  # No more occurrences found
#         count += 1
#         start += 1  # Move to the next character in the string
#     return count

