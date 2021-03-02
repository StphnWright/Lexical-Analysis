**ENGI E1006 - Intro to Computing for Engineers & Applied Scientists**

**Group Exercise Set 2**

Due: Thursday February 18 11:59pm, New York time (ET / GMT-5)

Please ask the instructor and CAs/TAs for help if you get stuck.

Do not use Python modules other than those explicitly mentioned.

Unlike the take-home projects, the group exercises are intended to be worked on your assigned groups 
on repl.it. You can work with your group during Thursday class and you are welcome to continue in your
own time. If you do not complete these problems during class, you must complete them at another time.

Groups should upload a single version of their solutions.

Comments in Python start with with a "# ..." 

Upload the following four files to Courseworks:

problem1.py
problem2.py
problem3.py
 
**Problem 1 (30 pts) - Pig Latin **

Pig Latin is a language game in which words are altered according to certain rules.  To make the pig latin form of an English word, the initial consonant sound is transposed to the end of the word, and an "ay" is affixed. Specifically, there are two rules: 
	•	If a word begins with a vowel, append "yay" to the end of the word. 
	•	If a word begins with a consonant, remove all the consonants from the beginning up to the first vowel and append them to the end of the word. Finally, append "ay" to the end of the word. The letter "y" counts as a consonant. If there are no vowels, simply append "ay" to the end of the word. 

For example: 
	•	dog => ogday
	•	python => onpythay
	•	scratch => atchscray
	•	is => isyay
	•	apple => appleyay
(a) In the file problem1.py, write a function

def piggify(word):
    ...

That takes an input String word as its parameter and returns a string containing the pig latin translation of
the word. You can assume that the input is always a lower-case string (no input verification is necessary). 

Hints: Use indexing and slicing. You might also want to use a string of vowels and then use the in operator to
check if a letter is a vowel.

vowels = 'aeiou'

(b) In the same file, write a program that repeatedly prompts the user to input a new word and then prints the
pig latin translation of the word (by calling the piggify function). When the user types a single period, the
program should quit. 

**Problem 2 (30 points) - Fancy Print**

Write a function

def print_box(s):
   ...

That prints  out the string s centered, in a box. For example, print_box("Python rocks!") should print.

*****************
* Python rocks! *
*****************

Make sure this also works for multi-line strings. The multi-line string "Python\nRocks\n!" should be printed like this:

**********
* Python *
* Rocks  *
*   !    *
**********

Write a main program that prompts the user to input a string, and then calls the print_box function to print it.

Save your program, including the function, in a file problem2.py.

**Problem 3 (40 pts) - Finding Subsequences in DNA Strings**

DNA molecules consist of a sequence of the four nucleotide bases: adenine, thymine, cytosine, and guanine. The
nucleotide bases are often abbreviated by their first letter, ATCG) so that DNA is represented as a string of
these four letters. A DNA string can be millions of bases long.

One important problem on DNA strings is substring matching, which is the task of checking whether a shorter
substring is contained within a longer string. Obviously, finding a substring in a long string has many
interesting applications, but here we will focus on DNA sequences.

Python strings already provide an s.find(substring) method that returns the index in s at which substring
first appears. If the substring does not appear, the method returns -1. For example: "ATCGCGTACT".find("CGCG")
returns 2, but "ATCGCGTACT".find("CGAT") returns -1. 

(a) Without using the existing find method of Python strings, write a function find(s, substring).

that does the same thing as the find method. If the substring appears in s, the method should return its index,
otherwise it should return -1. Write the function in the file problem3.py. 

(b) Without using the existing find method, write a function find_multi(s, substring), that returns a list of the
indices of all occurrences of the substring. If the substring is not found, the function can return an empty list.
Make sure your function can handle overlapping substrings. 

For example: 

find_multi("ATGCGCGAT", "GCG") should return [2,4].
