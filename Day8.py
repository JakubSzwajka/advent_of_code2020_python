file = open("sample_data.txt", "r")

instructions = []

for row in file:
    instruction = {}
    parts = row.strip().split(' ')
    instruction['inst'] = parts[0]
    instruction['step'] = int(parts[1])
    instruction['times'] = 0
    instructions.append(instruction)

instr_quant = len(instructions)
# print(instructions)

accumulator = 0
iterator = 0
while instructions[iterator]['times'] == 0: 
    # print(instructions[iterator])

    if instructions[iterator]['inst'] == 'nop':
        instructions[iterator]['times'] += 1
        iterator += 1
        continue
    elif instructions[iterator]['inst'] == 'acc':
        instructions[iterator]['times'] += 1
        accumulator += instructions[iterator]['step']
        iterator += 1
        continue

    elif instructions[iterator]['inst'] == 'jmp':
        instructions[iterator]['times'] += 1
        iterator += instructions[iterator]['step']
        continue

print(accumulator)