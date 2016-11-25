import DatabaseConfig
import User
import Interest
import Engine
import Util


def buildUser(firstName, fullName, password):
    return User.User(name=firstName, fullname=fullName, password=password)

def printDb(session):
    for user in session.query(User.User).all():
        print(user)


def populateDatabase(session):
    users = []

    num = len(session.query(User.User).all())
    todo = 0 if (num > 500) else (500 - num)

    for i in range(todo):
        user = User.createUser()
        users.append(user)

    session.add_all(users)
    session.commit()


def driver():
    session = DatabaseConfig.setupDb()
    populateDatabase(session)
    sample_user = User.createUser()

    print "Matching the following user: \n" + sample_user.prettyPrint()

    matched_user, score, time = Engine.findMatch(sample_user, session)

    print "Best match: \n" + matched_user.prettyPrint()
    Util.export(sample_user, matched_user, score, time)



driver()






