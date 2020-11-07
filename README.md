# Task - DNA String Parsing

### Summary
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains. An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

### Task 
Given a DNA string s of length at most 1000 nt, return four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

**Sample Dataset:**

AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

**Sample Output:**

20 12 17 21

### Acceptance Criteria
* New Project and Repository
* At least 5 commits 
* Uses OOP - must be in class and method format
* Has documentation
* Follows best practices
NOTE -> Must be in class and method format

# Process 
#### 1. Create a Parent class
* A Parent class is created called DNA_Parse.
* The class is initialised to take a user input and convert to upper case.
```python
class DNA_Parse:
    def __init__(self):
        self.s=input("Please enter your string: \n").upper()
```

* Within the class, a letters function is defined which iterates through the string and counts the times the letters A, C, G, and T appears. This is returned in a formatted string. 
```python
    def letters(self):
        for let in self.s:
            return "{} {} {} {} ".format(self.s.count("A"),self.s.count("C"),self.s.count("G"),self.s.count("T"))
```
#### 2. Class Instantiation
* A run file is created to instantiate the DNA_Parse class. 
* The DNA_Parse class is imported.
```python
from string import DNA_Parse
```
* An instance is created called dna_test and the letters function is executed. 
```python
dna_test=DNA_Parse()
print(dna_test.letters())
```
