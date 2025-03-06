
#获取页数信息

def getRecords(lst,start,pageSize=3):
    count=len(lst)#求出总数
    if(count%pageSize==0):
        pageNum=(int)(count/pageSize)
    else:
        pageNum=(int)(count/pageSize+1)
    if(start>count):
        start=count

    records=(lst[(start-1)*pageSize:(start-1)*pageSize+pageSize])
    return {"pageNum":pageNum,"records":records,"pageSize":pageSize,"count":count}
