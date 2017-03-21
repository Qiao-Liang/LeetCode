def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    # str_num = str(num)
    # if len(str_num) == 1:
    #     return num
    # else:
    #     temp = 0
    #     for digit in str_num:
    #         temp += int(digit)
        
    #     return addDigits(temp)

    if num > 9:
        temp = 0
        while num != 0:
            temp += num % 10
            num = num // 10
            
        return addDigits(temp)
    else:
        return num