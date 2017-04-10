def manipulate_dic(n):
    completed = []
    incomplete = []
    for k, v in n.items():

        if v == 'YES':
            completed.append(k)
        elif v == 'NO':
            incomplete.append(k)
        else:
            return 'You have not chosen any skill'

    print("\n\nComplete skills")
    for item in completed:
        print(item)

    print("\n\nIncomplete skills")

    for item in incomplete:
        print (item)


