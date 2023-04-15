# An analog clock has standard 12-hour format and three hands to tell hours, minutes and seconds. 
# All hands are moving smoothly with constant speeds. 
# Given the time that the clock is showing, determine the integer part of the angle degree between hours and seconds hands. 
# The position of the hour hand is updated every 6 minutes.
# Example : timeDegrees("11:19:41") = 93
def timeDegrees(s):
    input=s.split(":")
    for i in range(len(input)):
        input[i] = (int)(input[i])
    
    if input[0] > 6 :
        degreeHour = 30 * abs(12-input[0])  
    else:
        degreeHour = 30 * (input[0])
    degreeHour = degreeHour - ((input[1] // 6) *3)
    if input[2] > 30:
        degreeSecond = 6 * (60-input[2])
    else:
        degreeSecond = 6 * (input[2])
    if (input[2] > 30 and input[0] > 6) or (input[2] < 30 and input[0] < 6):
        return max(degreeSecond,degreeHour) - min(degreeHour,degreeSecond)
    else:
        return degreeSecond + degreeHour

print(timeDegrees("10:59:59"))