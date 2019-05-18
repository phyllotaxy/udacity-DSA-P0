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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

def update_number_set(number_set, records, *indexes):
    for record in records:
        for i in indexes:
            number_set.add(record[i])
    return number_set

def main():
    number_set = set()
    number_set = update_number_set(number_set, texts, 0, 1)
    number_set = update_number_set(number_set, calls, 0, 1)
    print(('There are {} different telephone numbers in the '
           'records.').format(len(number_set)))

if __name__ == '__main__':
    main()
