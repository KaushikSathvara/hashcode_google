summation = 0
max_summation = 0


def read_file():
    with open("Docs/b_small.in", "r") as inp:
        n = inp.readlines()
    n1 = n[0][:-1]
    p1 = n[1][:-1]

    n1 = n1.split(" ")
    n1[0] = int(n1[0])
    n1[1] = int(n1[1])

    p1 = list(map(int, p1.split(" ")))
    return n1[0], n1[1], p1


max_slices, type_pizza, pizza = read_file()
slices = int(max_slices)
total_types = int(type_pizza)
pizza_types = [int(i) for i in pizza]


def check_index(i, j):
    j = (total_types - 1) - j  # -1 because we are doing with indexes
    if i != j:
        return True
    return False


def create_output_file(required_list, no_of_pizzas):
    with open("file.txt", "w") as f:
        f.write(str(no_of_pizzas) + "\n")

        f.write(" ".join([str(i) for i in required_list]))


for idx, item_i in enumerate(pizza_types):
    summation = item_i
    required_list = [idx]

    for jdx, item_j in enumerate(reversed(pizza_types)):
        temp = summation + item_j
        if temp <= slices and check_index(idx, jdx):
            summation = temp
            print("Appending", required_list)
            required_list.append((total_types - 1) - jdx)

    if summation >= max_summation:
        max_summation = summation
    print("local max", summation, "list", required_list)
    if summation == slices:
        break

# print(sorted(required_list))
create_output_file(sorted(required_list), len(required_list))

