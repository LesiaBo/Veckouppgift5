#omvandlar grader Celsius till grader Fahrenheit:
def c_to_f(degree):
    if degree < -273.15:
        return None
    print(f"{degree * 9 / 5 + 32}")
    return degree * 9 / 5 + 32