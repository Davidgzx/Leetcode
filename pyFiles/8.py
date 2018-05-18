def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    temp=str.strip().split(" ")
    # print(temp)
    for item in temp:

        if item.isdigit():
            print(item)
            return int(item)
myAtoi("   -42")