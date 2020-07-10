han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    # print("Line:", line)
    wds = line.split()
    # print("Words:", wds)
    # Guardian in a compound statement
    # Guardian 구문을 앞에 놓아야 한다.
    # or은 앞의 것이 참인 경우 뒤의 것은 스킵한다.
    if len(wds) < 3 or wds[0] != 'From':
        # print("Ignore")
        continue
    print(wds[2])


# 문제가 발생한 구문만 찾아가서 분석하기 보다는
# 그 전에 print를 이용해서 어떻게 작동하는지 파악 후에
# 어떤 문제가 발생한 것인지 분석하는 것이 현명하다.
