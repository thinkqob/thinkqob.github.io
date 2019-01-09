# A very simple music recommender system.

PREF_FILE = "musicrec-store.txt"


def loadusers(filename):
    """ Reads in a file of stored user's preference
        stored in the file 'filename'.
        Return a dictionary containing a mapping
        of users names to a list preferred artists
    """
    file = open(filename, 'r')
    userdict = {}
    for line in file:
        # Read and parse a single line
        [username, bands] = line.strip().split(":")
        bandlist = bands.split(",")
        bandlist.sort()
        userdict[username] = bandlist
    file.close()
    return userdict


def getpreferences(username, usermap):
    """ Return a list if the user's preferred artists.

        If system already knows about the user,
        it gets the preferences out of the usermap
        dictionary and then asks the user if she has
        additional preferences. If the user is new,
        it simply asks the user for her preferences.
    """
    newpref = ""
    if username in usermap:
        prefs = usermap[username]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("PLease enter another artist or band that you")
        print("like, or just press enter")
        newpref = raw_input("to see your recommendations:")
    else:
        prefs = []
        print("I see that your are a new user")
        print("Please enter the name of an artist or band")
        newpref = raw_input("that you like: ")

    while newpref != "":
        prefs.append(newpref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newpref = raw_input("to see your recommendations: ")

    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs


def getrecommendations(curruser, prefs, usermap):
    """ Gets recommendations for a user (curruser) based
        on the users in usermap (a dictionary)
        and the user's preferences in pref (a list).
        Returns a list of recommended artists.
    """
    bestuser = findbestuser(curruser, prefs, usermap)
    recommendations = drop(prefs, usermap[bestuser])
    return recommendations


def findbestuser(curruser, prefs, usermap):
    """ Find the user whose tastes are closets to the current
        user. Return the best user's name (a string)
    """
    users = usermap.keys()
    bestuser = None
    bestscore = -1
    for user in users:
        score = nummatches(prefs, usermap[user])
        if score > bestscore and curruser != user:
            bestscore = score
            bestuser = user
    return bestuser


def drop(list1, list2):
    """ Return a new list that contains only the elements in
        list2 that were NOT in list1
    """
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[i])
            j += 1

    return list3


def nummatches(list1, list2):
    """ Return the number of elements that match between
        two sorted list
    """
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches


def saveuserpreferences(username, prefs, usermap, filename):
    """ Writes all of the user preferences to the file.
        Return nothing.
    """
    usermap[username] = prefs
    file = open(filename, 'w')
    for user in usermap:
        tosave = str(user) + ":" + ",".join(usermap[user]) + "\n"
        file.write(tosave)
    file.close()


def main():
    """ The main recommendation function """
    usermap = loadusers(PREF_FILE)
    print("Welcom to the music recommender system!")

    username = raw_input("Please enter your name: ")
    print("Welcome,", username)

    prefs = getpreferences(username, usermap)
    recs = getrecommendations(username, prefs, usermap)

    # Print the user's recommendations
    if len(recs) == 0:
        print("I'm sorry but I have no recommendations")
        print("for you right now.")
    else:
        print(username, "based on the users I currently")
        print("know about, I believe you might like:")
        for artist in recs:
            print(artist)

        print("I hope you enjoy them! I will save youd")
        print("preferred artist and have new")
        print(" recommendations for you in the future")

    saveuserpreferences(username, prefs, usermap, PREF_FILE)

if __name__ == "__main__":
    main()

