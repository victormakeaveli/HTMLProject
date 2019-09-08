def rac1():
    positive_results = []
    negative_results = []
    happy = []
    sad = []
    global inp_num
    global its

    for inp_num in range(0, 3001):

        if inp_num in range(0, 10):
            ed = [int(i) for i in str(inp_num)]
        else:
            ed = [int(i) for i in str(inp_num**2)]

        check = 0
        counter = 0

        while check != 1:

            counter += 1

            if len(ed) == 1:
                check = (ed[0] ** 2)
                print(f'[1] Checking {inp_num} > {ed[0]}² = {check}')

            elif len(ed) == 2:
                check = (ed[0] ** 2) + (ed[1] ** 2)
                print(f'[2] Checking {inp_num} > {ed[0]}² + {ed[1]}² = {check}')

            elif len(ed) == 3:
                check = (ed[0] ** 2) + (ed[1] ** 2) + (ed[2] ** 2)
                print(f'[3] Checking {inp_num} > {ed[0]}² + {ed[1]}² + {ed[2]}² = {check}')

            elif len(ed) == 4:
                check = (ed[0] ** 2) + (ed[1] ** 2) + (ed[2] ** 2) + (ed[3] ** 2)
                print(f'[4] Checking {inp_num} > {ed[0]}² + {ed[1]}² + {ed[2]}² + {ed[3]} = {check}')

            elif len(ed) == 5:
                check = (ed[0] ** 2) + (ed[1] ** 2) + (ed[2] ** 2) + (ed[3] ** 2) + (ed[4] ** 2)
                print(f'[5] Checking {inp_num} > {ed[0]}² + {ed[1]}² + {ed[2]}² + {ed[3]}² + {ed[4]}² = {check}')

            elif len(ed) == 6:
                check = (ed[0] ** 2) + (ed[1] ** 2) + (ed[2] ** 2) + (ed[3] ** 2) + (ed[4] ** 2) + (ed[5] ** 2)
                print(f'[6] Checking {inp_num} > {ed[0]}² + {ed[1]}² + {ed[2]}² + {ed[3]}² + {ed[4]}² + {ed[5]}² = {check}')

            elif len(ed) == 7:
                check = (ed[0] ** 2) + (ed[1] ** 2) + (ed[2] ** 2) + (ed[3] ** 2) + (ed[4] ** 2) + (ed[5] ** 2) + (ed[6] ** 2)
                print(f'[7] Checking {inp_num} > {ed[0]}² + {ed[1]}² + {ed[2]}² + {ed[3]}² + {ed[4]}² + {ed[5]}² + {ed[6]}² = {check}')

            else:
                print('error')

            ed = [int(i) for i in str(check)]

            if check in positive_results:
                its = True
                break

            if check not in negative_results:
                if check == 1:
                    pass
                else:
                    negative_results.append(check)
                    continue

            else:
                its = False
                sad.append(inp_num)
                break
            its = True

        if its:
            happy.append(inp_num)
            print(f'{inp_num} is happy')
            print()

            while counter != 1:
                counter -= 1

                if any(i in negative_results for i in positive_results):
                    pass
                else:
                    positive_results.append(negative_results[-1])
                negative_results.pop()
            continue

        else:
            print(f'{inp_num} is sad')
            print()

    print(f'Happy {len(happy)} => {happy}')
    print(f'Sad {len(sad)} => {sad}')
    print('-'*250)
    print(f'Positive Results {len(positive_results)} => {sorted(positive_results)}')
    print(f'Negative Results {len(negative_results)} => {sorted(negative_results)}')


rac1()
