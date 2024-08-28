# ---------------------------
# -- Continue, Break, Pass --
# ---------------------------

myNumbers = [1, 2, 3, 5, 7, 10, 13, 14, 15, 19]

# Continue ==> Skip The ( Specific Element ) And Continue 

for numbers in myNumbers :

  if numbers == 13 :

      continue

  print( numbers )

print( "_" * 100 ) # -- Separator --

# Pass ==> Skip Any Program If I Completed Or Not

for numbers in myNumbers :
  pass

print( "Here We Have 'pass'." )

print( "_" * 100 ) # -- Separator --

# Break ==> Stop The Function

for numbers in myNumbers:

  if numbers == 13:

    break

  print( numbers )