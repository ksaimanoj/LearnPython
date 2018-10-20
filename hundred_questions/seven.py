def generate2DArray(x = 1, y = 1):
    response = []
    for i in range(x):
        row = []
        for j in range(y):
            row.append(i * j)
        response.append(row)
    return response

def main():
    print(generate2DArray(3,5))

main()