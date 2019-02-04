#Learning to Speak Object-Oriented

import random

from urllib.request import urlopen

import sys
4
5 WORD_URL = "http://learncodethehardway.org/words.txt"
6 WORDS = []
7
8 PHRASES = {
9 "class %%%(%%%):":
10 "Make a class named %%% that is-a %%%.",
11 "class %%%(object):\n\tdef __init__(self, ***)" :
12 "class %%% has-a __init__ that takes self and *** params.",
13 "class %%%(object):\n\tdef ***(self, @@@)":
14 "class %%% has-a function *** that takes self and @@@ params.",
15 "*** = %%%()":
16 "Set *** to an instance of class %%%.",
17 "***.***(@@@)":
18 "From *** get the *** function, call it with params self, @@@.",
19 "***.*** = '***'":
20 "From *** get the *** attribute and set it to '***'."
21 }
22
23 # do they want to drill phrases first
24 if len(sys.argv) == 2 and sys.argv[1] == "english":
25 PHRASE_FIRST = True
26 else:
27 PHRASE_FIRST = False

# load up the words from the website
30 for word in urlopen(WORD_URL).readlines():
31 WORDS.append(str(word.strip(), encoding="utf-8"))
32
33
34 def convert(snippet, phrase):
35 class_names = [w.capitalize() for w in

random.sample(WORDS, snippet.count("%%%"))]
37 other_names = random.sample(WORDS, snippet.count("***"))
38 results = []
39 param_names = []
40
41 for i in range(0, snippet.count("@@@")):
42 param_count = random.randint(1,3)
43 param_names.append(', '.join(
44 random.sample(WORDS, param_count)))
45
46 for sentence in snippet, phrase:
47 result = sentence[:]
48
49 # fake class names
50 for word in class_names:
51 result = result.replace("%%%", word, 1)
52
53 # fake other names
54 for word in other_names:
55 result = result.replace("***", word, 1)
56
57 # fake parameter lists
58 for word in param_names:
59 result = result.replace("@@@", word, 1)
60
61 results.append(result)

return results
64
65
66 # keep going until they hit CTRL-D
67 try:
68 while True:
69 snippets = list(PHRASES.keys())
70 random.shuffle(snippets)
71
72 for snippet in snippets:
73 phrase = PHRASES[snippet]
74 question, answer = convert(snippet, phrase)
75 if PHRASE_FIRST:
76 question, answer = answer, question
77
78 print(question)
