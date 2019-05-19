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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def starts_with(number, code):
    return number.find(code) == 0

def update_banga_set(banga_set, records, out_index, in_index):
    banga_code = '(080)'
    tele_code = '140'
    for record in records:
        if starts_with(record[out_index], banga_code):
            if starts_with(record[in_index], tele_code):
                banga_set.add(tele_code)
            elif starts_with(record[in_index], '('):
                end = record[in_index].find(')') + 1
                banga_set.add(record[in_index][:end])
            else:
                banga_set.add(record[in_index][:4])
    return banga_set

def compute_banga_in_out_percentage(records, out_index, in_index):
    banga_code = '(080)'
    banga_out_count = 0
    banga_in_count = 0
    for record in records:
        if starts_with(record[out_index], banga_code):
            banga_out_count += 1
            if starts_with(record[in_index], banga_code):
                banga_in_count += 1
    return (banga_in_count / banga_out_count) * 100

def main():
    banga_set = set()
    banga_set = update_banga_set(banga_set, calls, 0, 1)
    print('The numbers called by people in Bangalore have codes:')
    for code in sorted(banga_set):
        print(code)
    print(('{} percent of calls from fixed lines in Bangalore are calls to other '
           'fixed lines in Bangalore.').format(round(compute_banga_in_out_percentage(calls, 0, 1), 2)))

if __name__ == '__main__':
    main()
