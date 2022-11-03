def foo(my_str1: str, my_str2: str) -> str:
    return my_str1.capitalize() + my_str2[::-1]


def bar(_list: list) -> str:
    s = ""
    for i in _list:
        s += i
    return s


if __name__ == "__main__":
    import time

    while True:
        var1 = "he"
        var2 = "oll"
        var3 = ["W", "o", "r", "l", "d"]
        spam = foo(var1, var2)
        eggs = bar(var3)
        time.sleep(0)
        print(f"{spam} {eggs}!")
        break
