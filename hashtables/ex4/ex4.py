def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # absolute the entirety of a
    # put them all in a dictionary... yay
    # the key will be the number
    # the value will be how many times it has been encountered
    new = {}
    more = []
    for i in a:
        x = abs(i)
        new[x] = 1+new.get(x, 0)
    keys = list(new.keys())
    print(new)
    for l in new:
        print(new[l])
        if new[l] >= 2:
            more.append(keys[l])
    return more


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4, 7]))
