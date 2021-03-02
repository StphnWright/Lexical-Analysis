"""
A program to identify shorter DNA substrings 
contained within a longer string.  

"""

#multidimensional list of strings
inputs = [["ATGCGCGAT", ["GCG"]], ["ATCGCGTAC", ["CGCG", "CGAT"]]]

def find(s, substring):
  index = 0
  for letter in s:
    sub = s[index: index + len(substring)] #create string with slicing
    if substring == sub:
      return index
    index += 1
  return -1 #substring not in list

def find_multi(s, substring):
  index = 0
  indices = []
  for letter in s:
    sub = s[index: index + len(substring)]
    if substring == sub:
      indices.append(index) #append string to list
    index += 1
  return indices

#output function to minimize print statements
def output(dna, substring):
  print("DNA Sequence: ", dna)
  print("Substring: ", substring)
  print("Find: ", find(dna, substring))
  print("Find Multi: %s\n" % find_multi(dna, substring))

#call output function
for input in inputs:
  dna = input[0]
  for substring in input[1]:
    output(dna, substring)
