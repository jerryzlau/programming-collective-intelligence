#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
# A dictionary of movie critics and their ratings of a small set of movies
critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}

# Returns a similarity score of person 1 and person 2

# This is the Euclidean Distance Score approach
# Calculates the distance between two plot point as similarity score
def sim_distance(prefs, p1, p2):

  # get shared items
  shared_items = {}
  for item in prefs[p1]:
    if item in prefs[p2]:
      shared_items[item]=1
  
  # return 0 if no items match
  if len(shared_items)==0:
    return 0
  
  # otherwise, find the distance between the two plot points
  sum_of_squares=sum([pow(prefs[p1][item]-prefs[p2][item],2) for item in shared_items])

  # my python beginner way to calculate sum of square
  total = 0
  for item in shared_items:
    total += pow(prefs[p1][item]-prefs[p2][item],2)

  return 1/(1+sqrt(sum_of_squares))

# Returns Pearson correlation coefficient for person1 and person2
def sim_pearson(prefs, p1, p2)
    # get shared items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    # Find number of elements
    n = len(si)

    # Return 0 if nothing in common
    if n == 0: return 0

    # Add up all the preferences
    sum1=sum([prefs[p1][item] for item in si])
    sum2=sum([prefs[p2][item] for item in si])

    # sum all the squares
    sum1Sq=sum([pow(prefs[p1][item],2) for item in si])
    sum2Sq=sum([pow(prefs[p2][item],2) for item in si])

    # sum the products
    pSum=sum([prefs[p1][item]*prefs[p2][item] for item in si])

    # Calculate pearson score
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return r



