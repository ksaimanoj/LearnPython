def main():
    input_text = input()
    l = input_text.split(",")
    l.sort()
    print(",".join(l))

main()
