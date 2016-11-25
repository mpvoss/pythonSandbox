import random
import Interest

alcohol_brands = []
sports_teams = []
sports = []
states = []


def populateList(file_name, list):
    with open(file_name) as f:
        for line in f:
            #print line.strip()
            list.append(line.strip())

def populateLists():
    populateList('../data/states.txt', states)
    populateList('../data/alcohol_brands.txt', alcohol_brands)
    populateList('../data/sports.txt', sports)
    populateList('../data/nba_teams.txt', sports_teams)
    populateList('../data/nfl_teams.txt', sports_teams)

def randomBoolean():
    return bool(random.getrandbits(1))


def configureInterests(user):

    for i in range(5):
        if randomBoolean():
            user.interests.append(Interest.Interest(name="state", value=random.choice(states), parent=user.id))
        if randomBoolean():
            user.interests.append(Interest.Interest(name="sports", value=random.choice(sports), parent=user.id))
        if randomBoolean():
            user.interests.append(Interest.Interest(name="alcohol_brands", value=random.choice(alcohol_brands), parent=user.id))
        if randomBoolean():
            user.interests.append(Interest.Interest(name="sports_teams", value=random.choice(sports_teams), parent=user.id))

def compareInterests(list1, list2):
    common = []
    unique1 = []
    unique2 = []

    for interest in list1:
        found = False
        for interest2 in list2:
            if interest.value == interest2.value:
                common.append(interest)
                found = True
        if not found:
            unique1.append(interest)

    for interest in list2:
        found = False
        for interest2 in list1:
            if interest.value == interest2.value:
                found = True
        if not found:
            unique2.append(interest)

    return common, unique1, unique2


populateLists()