def num_text():
    try:
        number = list(str(input("Enter a number: ")))
        const_num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        the_num = []
        for num in number:
            the_num.append(const_num[int(num)])
    except ValueError:
        print("Sorry numeric values only. '{}' isn't a numeric value.".format(''.join(number)))
    else:
        print("Here is your number: {} ".format("".join(number)))
        print("In word form: {} ".format(the_num))

num_text()