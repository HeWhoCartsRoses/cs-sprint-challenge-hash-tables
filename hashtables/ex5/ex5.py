# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    ends = []
    found = []
    for i in files:
        ends.append(i.split('/')[-1])
    return found


if __name__ == "__main__":
    files1 = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries1 = [
        "foo",
        "qux",
        "baz"
    ]
    # files = []

    # for i in range(500000):
    #     files.append(f"/dir{i}/file{i}")

    # for i in range(500000):
    #     files.append(f"/dir{i}/dirb{i}/file{i}")

    # queries = []

    # for i in range(1000000):
    #     queries.append(f"nofile{i}")

    # queries += [
    #     "file3490",
    #     "file256",
    #     "file999999",
    #     "file8192"
    # ]

    # print(finder(files, queries))
    print(finder(files1, queries1))
