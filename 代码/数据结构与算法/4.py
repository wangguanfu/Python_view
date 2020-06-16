dirs = {"C": "NULL",
        "D": {"D1": "NULL",
              "D2": {"D2_1": "NULL"}}, "E": {"E1": {"E1_1": {"E1_1_1": "NULL"},
                                                    "E1_2": "NULL"},
                                             "E2": "NULL"}}


def dirnames(dic):
    for key in dic.keys():
        print(key)
        if type(dic[key]) == type({}):
            dirnames(dic[key])
        else:
            pass
            # print(dic[key])


dirnames(dirs)
