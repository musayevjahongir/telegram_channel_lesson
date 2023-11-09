from read_data import fromJson

def get_post_per_week(data:dict,month:int)->dict:
    """
    Return the number of posts for each week of a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        dict: a dictionary with the number of posts for each week.
    """
    d={1:0, 2:0, 3:0, 4:0, 5:0}
    for i in data["messages"]:
        if int(i["date"][5:7])==month:
            if int (i["date"][8:10])<=7: d[1]+=1
            elif int (i["date"][8:10])<=14: d[2]+=1
            elif int (i["date"][8:10])<=21: d[3]+=1
            elif int (i["date"][8:10])<=28: d[4]+=1
            elif int (i["date"][8:10])>28: d[5]+=1
    return d
data=fromJson("data/result.json")
print(get_post_per_week(data, 11))
