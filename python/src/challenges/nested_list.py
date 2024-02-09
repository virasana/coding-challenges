def get_second_lowest_people(data):
    second_lowest_score = sorted(set([score for _, score in data]))[1]
    result = sorted([name for name, score in data if score == second_lowest_score]) 
    return result

    # # data = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    # sorted_data = sorted(data, key = lambda x: (x[1], x[0]))
    # second_lowest_grade = sorted(set(score for _, score in data))[1]
    # people_with_second_lowest_grade = [person for person, score in sorted_data if score == second_lowest_grade]

    # result = [person for person in people_with_second_lowest_grade]
    # return result

if __name__ == '__main__':
    multiline_string = """\
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39\
"""

    # Split the multiline string into lines
    lines = multiline_string.strip().split('\n')
    lines = lines[1:]
    data = [[lines[i], float(lines[i+1])] for i in range(0, len(lines), 2)]   
    second_lowest_people = get_second_lowest_people(data)
    print(*second_lowest_people, sep="\n")
    
    # for person in people_with_second_lowest_grade:
    #     print(person)

    


