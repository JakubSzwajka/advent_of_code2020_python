file = open("sample_data.txt", "r")

rules = []
result = 0

def does_contain( bag_1 , bag_2 ):
    for rule in rules: 
        if rule['color'] == bag_1:
            for bag_in_bag1 in rule['contains']:
                if bag_in_bag1['color'] == bag_2:
                    return True
                else:
                    x = does_contain(bag_in_bag1['color'], bag_2)
                    if x == True:
                        return True
    return False

def rule_contains( bags ):
    string = ' '.join(bags)
    bags_contained = string.split(',')
    result_list = []

    for bag_contained in bags_contained: 
        bag = {}

        bag_list = bag_contained.split(' ')
        if bag_list[0] == '':
            bag_list.remove('')
        bag['color'] = bag_list[1] + ' ' + bag_list[2]

        result_list.append(bag)

    return result_list

for row in file: 
    words = row.strip().split(' ')

    rule = {}
    rule['color'] = words[0] + ' ' + words[1]
    rule['contains'] = rule_contains(words[4:])
    rules.append(rule)     

# print(rules)
for rule in rules:
    if does_contain( rule['color'], 'shiny gold'):
        result += 1

print(result)