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

        winningBlock = check(winningBlock[0],winningBlock[1])
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
    return "Kappa"

if __name__ == '__main__':
    # print(sonarSweepOne())
    # print(sonarSweepTwo())
    # print(diveOne())
    # print(diveTwo())
    # print(binaryDiagnosticOne())
    # print(binaryDiagnosticTwo())
    # print(bingoOne())
    # print(bingoTwo())
    print(hydroVenture())
