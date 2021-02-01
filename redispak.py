import redis

r = redis.StrictRedis(host='127.0.0.1', port=6379, db=3, charset="utf-8", decode_responses=True)

HASH = "zhash"+":"
index = 1


#       QUERY

def showset(group):
    # print("------- REDIS SHOWSET A")
    titles = r.smembers(group)
    return titles


def gethash(title, HASH):
    # print("------- REDIS GETHASH A")
    # simple hash field retrieval:
    content = r.hget(HASH + title, 'content')

    return content

'''

#      NEW



def addtohash(item, HASH):
    # print("------- REDIS ADDTOHASH N")

    hashcontent = item['content']
    hashgroup = item['group']
    hashstamp = item['timestamp']


    #print(item['title'])
    hashtitle = item['title']

    r.hmset(HASH + hashtitle, { 'title': hashtitle, 'content': hashcontent, 'group': hashgroup, 'timestamp': hashstamp })

    return "OK"


def getallkeys():
    print("--------- REDIS GETALLKEYS N D")
    keys = r.keys('*')
    vals = ''
    allvals = []
    for key in keys:
        allvals.append(key)
    return allvals


def setadd(item, set):
    # set name is from 'all' 'poetry' 'software' ....
    print("------- REDIS SETADD N")

    print(set)
    r.sadd(set, item)
    return set


#             DELETE

# it is 'correct' to  assume that THIS deletion is 'global' on the item:
# the hash id is NOT needed:
def setrem(title, group):
    print("------- REDIS SETREM D")
    print("what is the group ?" + group)

    r.srem(group, title)
    r.hdel(HASH + title, 'title','content','group','timestamp')

    return title


def getgroup(title, HASH):
    print("------- REDIS GETGROUP")
    # simple hash field retrival:
    group = r.hget(HASH + title, 'group')

    return group




def delset(setname):
    print("------- REDIS DELSET"+ setname)
    r.delete(setname)
    return setname



def remfromset(title, set):
    # this only deals with set="all"
    # how to handle set="software" etc:
    # set name is now 'software'
    print("------- REDIS REMFROMSET")
    r.srem(set, title)
    return title



def getindex(title, HASH):
    print("------- REDIS GETINDEX")
    # simple hash field retrival:
    index = r.hget(HASH + title, 'index')

    return index





def scan(index):
    print("------- REDIS SCAN")
    # set name is from 'all' 'poetry' 'software' ....
    print("SCAN")
    d = r.scan(index)

    return d

def gethashall(title):
    print("------- REDIS GETHASHALL")
    # simple hash field retrieval:

    # title is in format 'zhash:The Desolate Field' - no quotes!
    print(title)
    # returns a dictionary of all fields as key value pairs
    d = r.hgetall(title)

    return(d)

def getzhashgroup(title):
    print("------- REDIS GETZHASHGROUP")
    # simple hash field retrival:
    group = r.hget(title, 'group')

    return group

def getredishashvals():
    print("------- REDIS GETREDISHASHVALS")
    keys = r.keys('*')
    vals = ''
    allvals = []
    for key in keys:

        if key.startswith('zhash'):
            group = getzhashgroup(key)

            allvals.append(group)
    return allvals


def getredishashtitles():
    print("-------- REDIS GETREDISHASTITLES")

    keys = r.keys('*')
    ztitle = []
    value = ""
    titles = []
    groups = []
    for key in keys:
        if key.startswith('zhash'):
            ztitle = key.split(':')
            value = ztitle[1]
            titles.append(value)
        else:
            groups.append(key)

        # Creating an empty dictionary
    dbdict = {}

    # Adding list as value
    dbdict["group"] = groups
    dbdict["title"] = titles

    return dbdict

def getgrouptitlehash():
    print("--------- REDIS GETGROUPTITLES")
    keys = r.keys('*')
    vals = ''
    allvals = []
    for key in keys:
        allvals.append(key)
    return allvals

'''
