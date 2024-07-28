import typing

def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age
    return name_with_age



if __name__ == "__main__":
    get_name_with_age("name", 1)