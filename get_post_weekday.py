from read_data import fromJson
import datetime
def get_post_weekday(data:dict)->dict:
    """
    Return the number of posts for each weekday
    args:
        data: a dictionary of posts
    returns: a dictionary with the number of posts for each weekday
    """
    d={}
    for i in data["messages"]:
        s=datetime.datetime.fromisoformat(i["date"])
        d[s.isoweekday()]=0
    for i in data["messages"]:
        s=datetime.datetime.fromisoformat(i["date"])
        d[s.isoweekday()]+=1
    return d
data=fromJson("data/result.json")
print(get_post_weekday(data, ))