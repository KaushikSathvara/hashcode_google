slices = 100
total_types = 10
pizza_types = [4, 14, 15, 18, 29, 32, 36, 82, 95, 95]

# =============================================================================

summation = 0


def read_file():
    with open("Docs/a_example.in", "r") as inp:
        n = inp.readline()
        p = inp.readline()
    n1 = n[:-1]
    p1 = p[:-1]

    lis1 = n1.split(" ")
    lis2 = p1.split(" ")
    max_slices = lis1[0]
    type_pizza = lis1[1]
    pizza = []

    for i in lis2:
        pizza.append(i)

    return max_slices, type_pizza, pizza


max_slices, type_pizza, pizza = read_file()
slices = max_slices
total_types = type_pizza
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


max_summation = 0

for idx, item_i in enumerate(pizza_types):
    summation = item_i
    required_list = [item_i]

    for jdx, item_j in enumerate(reversed(pizza_types)):
        temp = summation + item_j
        if temp <= slices and check_index(idx, jdx):
            summation = temp
            print("Appending", required_list)
            required_list.append(item_j)

    if summation >= max_summation:
        max_summation = summation
    print("local max", summation, "list", required_list)
    if summation == slices:
        break

create_output_file(sorted(required_list), len(required_list))

