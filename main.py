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


# Day three part one
def binaryDiagnosticOne():
    with open("dayThreeInput.txt", "r") as file:
        binaryArr = file.read().splitlines()
        gammaRate = ""
        epsilonRate = ""

        j = 0
        while j < len(binaryArr[0]):
            i = 0
            ones = 0
            zeroes = 0

            while i < len(binaryArr):
                if binaryArr[i][j] == '1':
                    ones += 1
                else:
                    zeroes += 1
                i += 1

            if ones > zeroes:
                gammaRate += "1"
                epsilonRate += "0"
            else:
                gammaRate += "0"
                epsilonRate += "1"
            j += 1

    return int(gammaRate, 2) * int(epsilonRate, 2)


# Day three part two
def binaryDiagnosticTwo():
    with open("dayThreeInput.txt", "r") as file:
        binaryArr = file.read().splitlines()
        count = 0
        ones = 0
        zeroes = 0

        for x in binaryArr:
            if x[count] == '1':
                ones += 1
            else:
                zeroes += 1

        oxyArr = []
        if ones >= zeroes:
            for x in binaryArr:
                if x[count] == "1":
                    oxyArr.append(x)
        else:
            for x in binaryArr:
                if x[count] == "0":
                    oxyArr.append(x)

        count = 1
        oxygen = oxygenNumber(count, oxyArr)

        carArr = []
        count = 0
        if zeroes < ones or zeroes == ones:
            for x in binaryArr:
                if x[count] == "0":
                    carArr.append(x)
        else:
            for x in binaryArr:
                if x[count] == "1":
                    carArr.append(x)

        count = 1
        carbon = carbonNumber(count, carArr)

        return int(oxygen, 2) * int(carbon, 2)


def oxygenNumber(count, arr):
    ones = 0
    zeroes = 0

    for x in arr:
        if x[count] == '1':
            ones += 1
        else:
            zeroes += 1

    oxyArr = []
    if ones > zeroes or ones == zeroes:
        for x in arr:
            if x[count] == "1":
                oxyArr.append(x)
    else:
        for x in arr:
            if x[count] == "0":
                oxyArr.append(x)

    count += 1
    if len(oxyArr) == 1:
        return arr[0]
    else:
        return oxygenNumber(count, oxyArr)


def carbonNumber(count, arr):
    ones = 0
    zeroes = 0

    for x in arr:
        if x[count] == '1':
            ones += 1
        else:
            zeroes += 1

    carArr = []
    if zeroes < ones or ones == zeroes:
        for x in arr:
            if x[count] == "0":
                carArr.append(x)
    else:
        for x in arr:
            if x[count] == "1":
                carArr.append(x)

    count += 1
    if len(carArr) == 1:
        return carArr[0]
    else:
        return carbonNumber(count, carArr)


if __name__ == '__main__':
    # print(sonarSweepOne())
    # print(sonarSweepTwo())
    # print(diveOne())
    # print(diveTwo())
    # print(binaryDiagnosticOne())
    print(binaryDiagnosticTwo())
