from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    s=0
    for i in data["messages"]:
        if int(i["date"][5:7])==month:
            s+=1
    return s
data=fromJson("data/result.json")
print(get_post_month(data,11))