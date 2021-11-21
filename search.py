#Powered By StarWorld
def search(lists=[""],texts=""):
    __search__ = []
    for __count__ in range(0,len(list(lists))):
        if texts in list(lists)[__count__]:
            __search__.append(list(lists)[__count__])
    return __search__

