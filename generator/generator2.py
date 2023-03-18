# https://realpython.com/introduction-to-python-generators/
# Although both approach works, the 2nd approach using generators will save on memory.

def csv_reader(file_name):
    file = open(file_name)
    result = file.read().split("\n")
    return result


def csv_reader2(file_name):
    for row in open(file_name, "r"):
        yield row

if __name__ == "__main__":
    csv_gen = csv_reader2("sample.csv")
    row_count = 0

    for row in csv_gen:
        row_count += 1

    print(f"Row count is {row_count}")