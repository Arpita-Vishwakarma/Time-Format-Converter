def timeConversion(s):
    # Extracting hours, minutes, and seconds
    hh, mm, ss = map(int, s[:-2].split(':'))
    meridiem = s[-2:]

    # Converting to 24-hour format
    if meridiem == 'PM' and hh != 12:
        hh += 12
    elif meridiem == 'AM' and hh == 12:
        hh = 0

    # Formatting the result
    return '{:02d}:{:02d}:{:02d}'.format(hh, mm, ss)

if __name__ == '__main__':
    s = input("Enter the time in 12-hour clock format: ")
    result = timeConversion(s)
    print("Equivalent time in 24-hour clock format:", result)