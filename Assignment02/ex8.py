
#string called by variable name formatter
formatter = "{} {} {} {}"

#format the string called formatter, program should give 1234
print(formatter.format(1, 2, 3, 4))

#format the string called formatter
print(formatter.format("one", "two", "three", "four"))

#format the string called formatter
print(formatter.format(True, False, False, True))

#format the string called formatter
print(formatter.format(formatter, formatter, formatter, formatter))

#format the string called formatter
print(formatter.format(
   "Try your",
   "Own text here",
   "Maybe a poem",
   "Or a song about fear"
))
