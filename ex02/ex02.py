def multiply_all(*args: int) -> int:
    mult = 1
    for arg in args:
        mult *= arg
    return mult

def main():
    inpstr = input("Introduce numbers: ")
    nrstr = inpstr.split(" ")
    nrs = []
    if inpstr:
        for x in nrstr:
            nrs.append(int(x))
    res = multiply_all(*nrs)
    print(res)

main()