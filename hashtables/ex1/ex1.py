def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create a dict
    # put each of the weights in the dict
    # run a for loop and check if
    # temp[i]-limit = anything in the dict
    dic = {}
    for i in range(length):
        dic[weights[i]] = weights[i]
    print(dic)
    for l in dic:
        x = limit-l
        if (x in dic.keys()) == True:
            y = (list(dic.keys()).index(x))
            z = (list(dic.keys()).index(l))
            if z == y:
                return (z+1, y)
            if z > y:
                return (z, y)
            if z < y:
                return (y, z)

    return None


if __name__ == "__main__":
    print(get_indices_of_item_weights([1, 2, 3, 4, 5], 5, 9))
    print(get_indices_of_item_weights([4, 3, 7, 18, 46], 5, 10))
    weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
    print(get_indices_of_item_weights(weights_4, 9, 7))
    weights_2 = [4, 4]
    print(get_indices_of_item_weights(weights_2, 2, 8))
