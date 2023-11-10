from read_data import fromJson
import datetime
def get_posts_peer_day(data, day:str)->int:
    """
    Return the number of posts for given day

    Args:
        data (dict): a dictionary of posts

    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    b=datetime.datetime.fromisoformat(day).day
    s=0
    for i in data["messages"]:
        a=datetime.datetime.fromisoformat(i["date"])
        if a.day==b:
            s+=1
    return s
data=fromJson("data/result.json")
print(get_posts_peer_day(data,"2022-11-09"))