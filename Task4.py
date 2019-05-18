"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

from Task1 import update_number_set

def main():
    out_call_set = set()
    out_call_set = update_number_set(out_call_set, calls, 0)
    other_set = set()
    other_set = update_number_set(other_set, calls, 1)
    other_set = update_number_set(other_set, texts, 0, 1)
    print('These numbers could be telemarketers: ')
    for number in sorted(out_call_set.difference(other_set)):
        print(number)

if __name__ == '__main__':
    main()

# The program assumes that the definition of telemarketer is ONLY that from
# TASK 4 and NOT from TASK 3 (otherwise it would be debatable if numbers that
# starts with area code 140 are "possible" telemarketers, as they're "definitely"
# telemarketers according to TASK 3)
# Another reason for doing this is that the company probaly want to identify non-obvious
# telemarketers, and not obvious telemarketers that starts with a certain area code.
# To summarize, no assumption on the area code of telemarketers is made.
