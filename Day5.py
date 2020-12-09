file = open("sample_data.txt", "r")

list_of_seats_ID = []

def get_seat_ID(boarding_pass , range_list):
    for letter in range(len(boarding_pass)):
        
        y = {
            'F': lambda x: ( x[1] - x[0] ) / 2 + x[0],
            'B': lambda x: ( x[1] - x[0] ) / 2 + x[0] + 1,
            'L': lambda x: ( x[3] - x[2] ) / 2 + x[2],
            'R': lambda x: ( x[3] - x[2] ) / 2 + x[2] + 1 
        }[boarding_pass[letter]](range_list)

        position = {
            'F': lambda x: 1,
            'B': lambda x: 0,
            'L': lambda x: 3,
            'R': lambda x: 2
        }[boarding_pass[letter]]('')

        range_list[position] = int(y)
    return range_list[0] * 8 + range_list[2]

for boarding_pass in file:
    range_list = [0,127,0,7]
    list_of_seats_ID.append(get_seat_ID(boarding_pass.strip(), range_list))

list_of_seats_ID.sort()

for seat in range(len(list_of_seats_ID)):
    
    if seat + 1 < len(list_of_seats_ID):
        if list_of_seats_ID[seat] + 1 != list_of_seats_ID[seat + 1]:
            print(list_of_seats_ID[seat] + 1)
