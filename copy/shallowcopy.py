# https://realpython.com/copying-python-objects/

if __name__ == "__main__":
    xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ys = list(xs)  # Make a shallow copy

    print(xs)
    print(ys)

    xs.append(['new sublist'])
    print(xs)
    print(ys)

    xs[1][0] = 'X'
    print(xs)
    print(ys)