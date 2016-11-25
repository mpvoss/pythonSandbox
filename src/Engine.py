import DatabaseConfig
import User
import itertools
import Interest
import datetime
import warnings

def findMatch(user, session):
    start_time = datetime.datetime.now()
    goal_interests = set(user.interests)

    map = {}
    for interest in goal_interests:
        if interest.name in map:
            map[interest.name].append(interest.value)
        else:
            map[interest.name] = [interest.value]

    best_match = None
    max = 0
    for person in session.query(User.User).all():
        count = 0
        for interest in person.interests:
            if interest.name in map:
                for z in map[interest.name]:
                    #print(z + " " + interest.name)

                    if z == interest.value:
                            count = count + 1

        if max < count:
            best_match = person
            max = count

    print("Best match score: " + str(max))

    end_time = datetime.datetime.now()

    return best_match, max, end_time - start_time

def test():
    session = DatabaseConfig.setupDb()
    user1 = User.User(name="1")
    user1.interests.append(Interest.Interest(name="food", value="mexican"))

    result = findMatch(user1, session)
    print(result)

test()