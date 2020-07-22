#This python algorithm counts the inversions in a series of numbers, as well as the inversions in two differently ordered
#music playlists. This project was completed for my Sophomore Data Structures course.


# CS 2123, The University of Tulsa

#Justin Klopfer and Alex Poe

from collections import deque
import itertools

def mergeandcount(lft,rgt):
    lftCurrentPointer = 0
    rghtCurrentPointer = 0
    inversionCount = 0
    output = []
    while(lftCurrentPointer < len(lft) and rghtCurrentPointer < len(rgt)):
        if (lft[lftCurrentPointer] > rgt[rghtCurrentPointer]):
            output.append(rgt[rghtCurrentPointer])
            inversionCount += len(lft) - lftCurrentPointer
            rghtCurrentPointer += 1
        else:
            output.append(lft[lftCurrentPointer])
            lftCurrentPointer += 1
        
    if (lftCurrentPointer == len(lft)):
        while (rghtCurrentPointer < len(rgt)):
            output.append(rgt[rghtCurrentPointer])
            rghtCurrentPointer += 1
    if (rghtCurrentPointer == len(rgt)):
        while (lftCurrentPointer < len(lft)):
            output.append(lft[lftCurrentPointer])
            lftCurrentPointer += 1    
    return (inversionCount, output)
    """
    Glue procedure to count inversions between lft and rgt.
    Input: two ordered sequences lft and rgt
    Output: tuple (number inversions, sorted combined sequence)
    """


def sortandcount(seq):
    if (len(seq) <= 1):
        return (0, seq)
    else:
        n = len(seq)
        A = seq[0:int(len(seq) / 2)]
        B = seq[int((len(seq) / 2)):int(len(seq))]
        (countA, A) = sortandcount(A)
        (countB, B) = sortandcount(B)
        (finalInversions, sortedList) = mergeandcount(A, B)
        totalInversions = finalInversions + countA + countB
        return (totalInversions, sortedList)
    """
    Divide-conquer-glue method for counting inversions.
    Function should invoke mergeandcount() to complete glue step.
    Input: ordered sequence seq
    Output: tuple (number inversions, sequence)
    """
    

if __name__ =="__main__":
    seq1 = [7, 10, 18, 3, 14, 17, 23, 2, 11, 16]
    seq2 = [2, 1, 3, 6, 7, 8, 5, 4, 9, 10]
    seq3 = [1, 3, 2, 6, 4, 5, 7, 10, 8, 9]
    songs1 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (5,"Cake: I Will Survive"),
             (6,"Aretha Franklin: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs2 = [(3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (8,"Coldplay: Clocks"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (9,"Nickelback: Gotta be Somebody"),
             (10,"Garth Brooks: Friends in Low Places")]
    songs3 = [(1,"Stevie Ray Vaughan: Couldn't Stand the Weather"),
             (2,"Jimi Hendrix: Voodoo Chile"),
             (3,"The Lumineers: Ho Hey"),
             (4,"Adele: Chasing Pavements"),
             (6,"Aretha Franklin: I Will Survive"),
             (5,"Cake: I Will Survive"),
             (7,"Beyonce: All the Single Ladies"),
             (8,"Coldplay: Clocks"),
             (10,"Garth Brooks: Friends in Low Places"),
             (9,"Nickelback: Gotta be Somebody")]
  
  
    print(seq1)
    print("# Inversions: %s\n" %sortandcount(seq1)[0])
    print(seq2)
    print("# Inversions: %i\n" %sortandcount(seq2)[0])
    print(seq3)
    print("# Inversions: %i\n" %sortandcount(seq3)[0])
    print(songs1)
    print("# Inversions: %i\n" %sortandcount(songs1)[0])
    print(songs2)
    print("# Inversions: %i\n" %sortandcount(songs2)[0])
    print(songs3)
    print("# Inversions: %i\n" %sortandcount(songs3)[0])
