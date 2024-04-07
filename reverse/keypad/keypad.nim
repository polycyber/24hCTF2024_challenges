import strutils, sequtils

echo "Enter the correct PIN to unlock the door"
var input: string = readLine(stdin)

if input.len != 8 or not all(input, isDigit):
    quit("Invalid input", 1)

let input_numbers: seq[int] = map(input, proc(x: char): int = parseInt($x))

let secret_code: array[8, int] = [2, 9, 3, 8, 5, 9, 1, 4]

for idx, current_number in input_numbers:
    if current_number != secret_code[idx]:
        quit("Invalid PIN", 1)

echo "Access granted!"
