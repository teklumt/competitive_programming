class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions.sort()
        res = []

        group = defaultdict(list)

        for tran in transactions:
            name, time , amount, city = tran.split(',')
            group[name].append([time, amount, city])

        for name in group:
            for i in range(len(group[name])):
                if int(group[name][i][1]) > 1000:
                    res.append(",".join([name, *group[name][i]]))
                else:
                    for j in range(len(group[name])):
                        if i != j:
                            if ((abs(int(group[name][i][0]) - int(group[name][j][0])) <= 60) and (group[name][i][2] != group[name][j][2])):
                                res.append(",".join([name, *group[name][i]]))
                                break
        return res