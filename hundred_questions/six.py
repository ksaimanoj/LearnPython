import math

def formula(d, c = 50, h = 30):
    return math.sqrt((2 * c * d) / h )

def main():
    input_text = input()
    output = []
    l = input_text.split(",")
    for item in l:
        output.append(math.floor(formula(int(item))))
    print(output)

main()