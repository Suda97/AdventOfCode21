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


# Day four part one
def bingoOne():
    with open("dayFourInput.txt", "r") as file:
        bingo = file.read().splitlines()
        randomNumbers = [int(i) for i in bingo[0].split(',')]
        blocks = 0
        block = []
        data = []

        for x in bingo[2:]:
            if x != "":
                block.append([int(i) for i in x.strip().split(" ") if i != ""])
            else:
                data.append(block)
                block = []
                blocks += 1

        winningBlock = checkBingoOne(data, randomNumbers)

        summ = 0
        for row in winningBlock[0]:
            summ += sum(row)

        return summ * winningBlock[1]


def checkBingoOne(data, randomNumbers):
    # O(n)^ TO THE MOON!!!!! (I know It's bad)
    for number in randomNumbers:
        for block in data:
            for row in block:
                for i, num in enumerate(row):
                    if num == number:
                        row[i] = False
                    else:
                        continue

                if row == [False, False, False, False, False]:
                    return block, number

            for i in range(0, 5):
                count = 0

                for row in block:
                    if row[i] == False:
                        count += 1

                if count == 5:
                    return block, number


# Day four part two
def bingoTwo():
    with open("dayFourInput.txt", "r") as file:
        bingo = file.read().splitlines()
        randomNumbers = [int(i) for i in bingo[0].split(',')]
        blocks = 0
        block = []
        data = []

        for x in bingo[2:]:
            if x != "":
                block.append([int(i) for i in x.strip().split(" ") if i != ""])
            else:
                data.append(block)
                block = []
                blocks += 1

        while len(data) != 1:
            winningBlock = checkBingoTwo(data, randomNumbers)
            data = winningBlock[0]
            randomNumbers = winningBlock[1]

        winningBlock = check(winningBlock[0], winningBlock[1])
        summ = 0
        for row in winningBlock[0]:
            summ += sum(row)

        return summ * winningBlock[1]


def checkBingoTwo(data, randomNumbers):
    # O(n)^4 TO THE MOON!!!!! (I know It's bad)
    for number in randomNumbers:
        for b, block in enumerate(data):
            for row in block:
                for i, num in enumerate(row):
                    if num == number:
                        row[i] = False
                    else:
                        continue

                if row == [False, False, False, False, False]:
                    data.pop(b)
                    return data, randomNumbers, number

            for i in range(0, 5):
                count = 0

                for row in block:
                    if row[i] == False:
                        count += 1

                if count == 5:
                    data.pop(b)
                    return data, randomNumbers, number


def check(data, randomNumbers):
    for number in randomNumbers:
        for b, block in enumerate(data):
            for row in block:
                for i, num in enumerate(row):
                    if num == number:
                        row[i] = False
                    else:
                        continue

                if row == [False, False, False, False, False]:
                    return block, number

            for i in range(0, 5):
                count = 0

                for row in block:
                    if row[i] == False:
                        count += 1

                if count == 5:
                    return block, number


# Day five part one
def hydroVenture():
    with open("dayFiveInput.txt", "r") as file:
        data = file.read().splitlines()
        numbers = []
        res = ([[0 for col in range(1000)] for row in range(1000)], [0])
        count = 0

        for i, points in enumerate(data):
            num = points.replace(' -> ', ',')
            num = (num.strip().split(","))
            numbers.append([int(j) for j in num])

            if numbers[i][0] == numbers[i][2]:
                res = vertical(res, numbers[i])
            elif numbers[i][1] == numbers[i][3]:
                res = horizontal(res, numbers[i])
            else:
                res = diagonal(res, numbers[i])

        return res[1][0]


def horizontal(res, crds):
    start = min(crds[0], crds[2])
    end = max(crds[0], crds[2]) + 1

    for i in range(start, end):
        res[0][i][crds[1]] += 1
        if res[0][i][crds[1]] == 2:
            res[1][0] += 1
    return res


def vertical(res, crds):
    start = min(crds[1], crds[3])
    end = max(crds[1], crds[3]) + 1

    for i in range(start, end):
        res[0][crds[0]][i] += 1
        if res[0][crds[0]][i] == 2:
            res[1][0] += 1
    return res


class point:
    def __init__(self, xvalue=None, yvalue=None):
        self.xvalue = xvalue
        self.yvalue = yvalue


def diagonal(res, crds):
    pointOne = point(crds[0], crds[1])
    pointTwo = point(crds[2], crds[3])

    if pointOne.xvalue > pointTwo.xvalue and pointOne.yvalue < pointTwo.yvalue:
        counter = pointOne.xvalue - pointTwo.xvalue + 1
        i = pointTwo.xvalue
        j = pointTwo.yvalue

        while counter > 0:
            res[0][i][j] += 1
            if res[0][i][j] == 2:
                res[1][0] += 1
            i += 1
            j -= 1
            counter -= 1

    elif pointTwo.xvalue > pointOne.xvalue and pointTwo.yvalue < pointOne.yvalue:
        counter = pointTwo.xvalue - pointOne.xvalue + 1
        i = pointOne.xvalue
        j = pointOne.yvalue

        while counter > 0:
            res[0][i][j] += 1
            if res[0][i][j] == 2:
                res[1][0] += 1
            i += 1
            j -= 1
            counter -= 1

    elif pointOne.xvalue > pointTwo.xvalue and pointOne.yvalue > pointTwo.yvalue:
        counter = pointOne.xvalue - pointTwo.xvalue + 1
        i = pointTwo.xvalue
        j = pointTwo.yvalue

        while counter > 0:
            res[0][i][j] += 1
            if res[0][i][j] == 2:
                res[1][0] += 1
            i += 1
            j += 1
            counter -= 1

    elif pointTwo.xvalue > pointOne.xvalue and pointTwo.yvalue > pointOne.yvalue:
        counter = pointTwo.xvalue - pointOne.xvalue + 1
        i = pointOne.xvalue
        j = pointOne.yvalue

        while counter > 0:
            res[0][i][j] += 1
            if res[0][i][j] == 2:
                res[1][0] += 1
            i += 1
            j += 1
            counter -= 1

    return res


# Day six part one
def lanterfishOne():
    with open("daySixInput.txt", "r") as file:
        data = [int(i) for i in file.read().split(",")]
        currData = data

        for i in range(80):
            temp_data = []
            new_fish = []

            for fish in currData:
                if fish == 0:
                    new_fish.append(8)
                    fish = 6
                else:
                    fish -= 1
                temp_data.append(fish)

            temp_data.extend(new_fish)
            currData = temp_data

        return len(currData)


# Day six part two
from collections import Counter


def lanterfishTwo():
    with open("daySixInput.txt", "r") as file:
        data = [int(i) for i in file.read().split(",")]
        # We have to use dict for this amount of days (256), This solution also works with part one
        livesInDays = dict(Counter(data))

        for i in range(256):
            livesInDays = {d: (0 if livesInDays.get(d + 1) is None else livesInDays.get(d + 1)) for d in range(-1, 8)}
            livesInDays[8] = livesInDays[-1]
            livesInDays[6] += livesInDays[-1]
            livesInDays[-1] = 0

        return sum(livesInDays.values())


# Day seven part one
def whaleOne():
    with open("daySevenInput.txt", "r") as file:
        data = [int(i) for i in file.read().split(",")]
        fuel = []

        for i in range(len(data)):
            fuel.append((sum(abs(val - i) for val in data)))

        return min(fuel)


# Day seven part Two
def whaleTwo():
    with open("daySevenInput.txt", "r") as file:
        data = [int(i) for i in file.read().split(",")]
        fuel = []

        for i in range(len(data)):
            diff = [abs(val-i) for val in data]
            sumDiff = sum([sum(list(range(d+1))) for d in diff])
            fuel.append(sumDiff)

        return min(fuel)


# Day eight part one
def sevenSegmentSearchOne():
    with open("dayEightInput.txt", "r") as file:
        data = [line for line in file.read().replace(" | ", ",").replace("\n", ",").split(",")]
        outputData = []
        j = 1

        for i, val in enumerate(data):
            if i == j:
                outputData.append(val.split(" "))
                j += 2

        count = 0
        for val in outputData:
            for seg in val:
                if 2 <= len(seg) <= 4 or len(seg) == 7:
                    count += 1

        return count


def sevenSegmentSearchTwo():
    print("I need a break")


if __name__ == '__main__':
    # print(sonarSweepOne())
    # print(sonarSweepTwo())
    # print(diveOne())
    # print(diveTwo())
    # print(binaryDiagnosticOne())
    # print(binaryDiagnosticTwo())
    # print(bingoOne())
    # print(bingoTwo())
    # print(hydroVenture())
    # print(lanterfishOne())
    # print(lanterfishTwo())
    # print(whaleOne())
    # print(whaleTwo())
    # print(sevenSegmentSearchOne())
    print(sevenSegmentSearchTwo())
