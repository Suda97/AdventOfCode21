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


if __name__ == '__main__':
    # print(sonarSweepOne())
    print(sonarSweepTwo())
