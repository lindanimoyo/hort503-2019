# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

months1 = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#looks like another way to do formatting
print("Here are the days: ", days)

print("Here are the months: ", months)

print("""
   There's something going on here.
   With the three double-quotes.
   We'll be able to type as much as we like.
   Even 4 lines if we want, or 5, or 6.
""")

#looks like another way to do formatting, gives the same result as above
print(f"Here are the days: {days}")


print(f"Here are the months: {months}")

print(f"Here are the months: {months1}")
