# Write your movie_review function here:
def movie_review(rating):
  if rating >= 9:
    return "Outstanding!"
  elif rating > 5:
    return "This one was fun."
  else:
    return "Avoid at all costs!"
# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."