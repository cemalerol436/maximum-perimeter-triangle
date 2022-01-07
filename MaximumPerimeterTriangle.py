
def maximumPerimeterTriangle(sticks):


    lists = sorted((sticks), reverse=True)
    lenght = len(lists)

    i= 0
    sum = 0
    total = []

    while i<lenght:

        a = lists[i]

        for b in lists[i+1:lenght] :

            for c in lists[i+2:lenght]:

                if a<b+c:
                    total =[a,b,c]
                    total_sum = a+b+c

                    if total_sum>sum:
                        sum = total_sum
                        return sorted(total)

        i += 1

    if len(total) == 0:
        return "-1"


sticks = list(map(int, input("sticks:").rstrip().split()))

result = maximumPerimeterTriangle(sticks)

print(result)
