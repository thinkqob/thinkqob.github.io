def selectionsort(listtosort):
    """sorts alist iteratively and in-place"""
    for starting_index in range(len(listtosort)):
        min_elem_index = index_of_min(listtosort, starting_index)
        swap(listtosort, starting_index, min_elem_index)
    return listtosort


# And here is index_of_min!:
def index_of_min(alist, start_index):
    """returns the index if the min element at or after start_index"""
    min_elem_index = start_index
    for i in range(start_index, len(alist)):
        if alist[i] < alist[min_elem_index]:
            min_elem_index = i
    return min_elem_index


# And swap:
def swap(alist, i, j):
    """swap the values of a alist[i] and alist[j]"""
    temp = alist[i]         # store the value of alist[i] for a moment
    alist[i] = alist[j]     # make alist[i] refer to the value of alist[j]
    alist[j] = temp         # make alist[j] refer to the value of stored value

listtosort = [2, 5, 4]
artist =['Maroon 5', 'Adele', 'Lady Gaga']

print(listtosort)
print(artist)
selectionsort(listtosort)
selectionsort(artist)
print(listtosort)
print(artist)


def standardizeall(storeedprefs):
    """Return a new list of a lists of stored user preferences,
        With each artist string in Title Case,
        With leading and trailling whitespace removed.
    """
    standardstoredprefs = []
    for storeduser in storeedprefs:
        standardstoreduser = []
        for artist in storeduser:
            standardstoreduser.append(artist.strip().title())
        standardstoredprefs.append(standardstoreduser)
    return standardstoredprefs

print (standardizeall([['adele', 'laDy GAGA'], ['maROON 5']]))
