def myfunc(string):
    x = []
    for i in range(len(string)):
        if i % 2 == 0:
            x.append(string[i].upper())
        elif i % 2 == 1:
            x.append(string[i].lower())
    return ''.join(x)
print(myfunc('Anthropomorphism'))




def paper_doll(text):
    result=''
    for char in text:
        result += char*3
    return result
print(paper_doll('Tarun'))


def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([2,4,6,8,9,8]))


def spy_game(nums):
    code = [0, 0, 7, 'x']

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))

def spy_newgame(nums):

    lis = []

    for item in nums:

        if item == 0 or item == 7:

            lis.append(item)

        else:

            continue

    if lis[:3] == [0,0,7]:

        return True

    else:

        return False

print(spy_newgame([1,2,0,1,0,7,0]))


def spygames(nums):
    for i in range(len(nums)):

        if nums[i] == 0:

            for y in range(i + 1, len(nums)):

                if nums[y] == 0:

                    for z in range(y + 1, len(nums)):

                        if nums[z] == 7:
                            return True

    else:

        return False

print(spygames([1, 2, 0, 1, 0, 7, 0]))


def newpr(num):
    out = [2]
    if num < 2:
        return 0
    else:
        for i in range(3,num):
            for item in out:
                if i % item == 0:
                    break
            else:
                    out.append(i)
    print(out)
    print(len(out))

newpr(16)
