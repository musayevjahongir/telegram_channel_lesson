from read_data import fromJson


def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    d={}
    for i in data["messages"]:
        d[int(i["date"][5:7])]=0
    for i in data["messages"]:
        d[int(i["date"][5:7])]+=1
    return d
data=fromJson("data/result.json")
print(get_post_per_month(data))