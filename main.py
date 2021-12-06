# Day one part one
def sonarSweepOne():
    with open('dayOneInput.txt', 'r') as file:
        counter = 0
        sonar = file.read().splitlines()
        prevNumber = -1

        for x in sonar:
            if prevNumber != -1:
                if int(x) > int(prevNumber):
                    counter += 1
            prevNumber = x

    return counter


# Day one part two
def sonarSweepTwo():
    with open('dayOneInput.txt', 'r') as file:
        counter = 0
        sonar = file.read().splitlines()
        prevSum = -1

        for i, x in enumerate(sonar):
            if i + 1 < len(sonar) and i + 2 < len(sonar):
                curSum = int(x) + int(sonar[i + 1]) + int(sonar[i + 2])
            if prevSum != -1:
                if curSum > prevSum:
                    counter += 1
            prevSum = curSum

    return counter


# Day two part one
def diveOne():
    with open("dayTwoInput.txt", "r") as file:
        dive = file.read().splitlines()
        depth = 0
        horPos = 0

        for i, x in enumerate(dive):
            if x[0] == 'd':
                depth += int(x[len(x) - 1])
            elif x[0] == 'u':
                depth -= int(x[len(x) - 1])
            elif x[0] == 'f':
                horPos += int(x[len(x) - 1])

    return depth * horPos


# Day two part two
def diveTwo():
    with open("dayTwoInput.txt", "r") as file:
        dive = file.read().splitlines()
        depth = 0
        horPos = 0
        aim = 0

        for i, x in enumerate(dive):
            if x[0] == 'd':
                aim += int(x[len(x) - 1])
            elif x[0] == 'u':
                aim -= int(x[len(x) - 1])
            elif x[0] == 'f':
                horPos += int(x[len(x) - 1])
                depth += aim * int(x[len(x) - 1])

    return depth * horPos


if __name__ == '__main__':
    # print(sonarSweepOne())
    # print(sonarSweepTwo())
    # print(diveOne())
    print(diveTwo())
