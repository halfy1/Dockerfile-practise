import sys

def print_help():
    print("Usage:")
    print("  sum x y z  -> returns x+y+z")
    print("  product x y z -> returns x*y*z")
    print("Example:")
    print("  docker run --rm  sum 1 2 3")
    sys.exit(0)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or "--help" in args:
        print_help()

    mode = args[0]
    numbers = args[1:]

    # Проверяем, что есть хотя бы один аргумент-число
    if not numbers:
        print_help()

    nums = list(map(float, numbers))

    if mode == "sum":
        print(sum(nums))
    elif mode == "product":
        product = 1
        for n in nums:
            product *= n
        print(product)
    else:
        print(f"Unknown mode '{mode}'. Available modes: sum, product")
        print_help()