# ********working day - Task 8*********** #
import sys
from time import perf_counter


# accumulator =0
# nop<val> -> move to next line
# acc<val> -> add <val> to accumulator and move to next line
# jmp<val> -> move to line >val>  positions away

def read_file(file):
    try:
        # The readlines() method returns a list containing each line in the file as a list item
        with open(file, 'r') as f:
            content = f.readlines()
            content = [line.strip() for line in content]
    except:
        print('Error to read file')
        sys.exit()
    # print(content)
    return content


if __name__ == "__main__":
    start_timer = perf_counter()

    input_data = read_file("data.txt")
    accu = 0
    line = 0
    instructions = []

    while line not in instructions:
        instructions.append(line)
        currentInstruction = input_data[line].split()
        #print(currentInstruction)
        #print(currentInstruction)
        cmd = currentInstruction[0]
        #print(cmd)
        num = int(currentInstruction[1])
        #print(num)
        if cmd == 'acc':
            accu += num
            line += 1
        elif cmd == 'jmp':
            line += num
        elif cmd == 'nop':
            line += 1

    print("Part 1: The value in the accumulator is : " + str(accu))
    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)
