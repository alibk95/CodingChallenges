class Bpp:
    # Bin Pack Problem (BPP)
    def __init__(self):
        pass

    def solve(self, input_list, bin_volume):
        result = 0
        remaining = bin_volume
        for i in range(len(input_list)):
            if remaining >= input_list[i]:
                remaining = remaining - input_list[i]
            else:
                result += 1
                remaining = bin_volume - input_list[i]
        return result


bpp = Bpp()
# Code driver
driver_list = [4, 8, 9, 1, 3, 6, 7, 2, 1, 6, 5]
bin_capacity = 11
print("minimum number of bins required to handle the bin pack problem is: ", bpp.solve(driver_list, bin_capacity))
