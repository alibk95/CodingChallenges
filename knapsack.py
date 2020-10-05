def backpack(max_weight,items):
    matrix = [[0 for col in range(max_weight+1)] for row in range(len(items[0]))]
    for row in range(len(items[0])):
        for col in range(max_weight+1):
            if items[0][row] > col:
                matrix[row][col] = matrix[row-1][col]
            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row-1][col-items[0][row]]+ items[1][row])
    for i in range(len(items[0])):
        print(matrix[i])
    packed = []
    col = max_weight

    for row in range(len(items[0])-1,-1,-1):
        if row == 0 and matrix[row][col] != 0:
            packed.insert(0,row)
        if matrix[row][col] != matrix[row-1][col]:
            packed.insert(0,row)
            col -= items[0][row]
    print(packed)
    print(matrix[len(items[0])-1][max_weight])


item_weight = [3,1,2,4]
item_values = [7,2,4,5]
items = [item_weight,item_values]
backpack(6,items)