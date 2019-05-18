"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""
def update_number_dict(number_dict, records, *num_indexes, dur_index):
    for record in records:
        for i in num_indexes:
            number_dict[record[i]] = number_dict.get(record[i], 0) + int(record[dur_index])
    return number_dict

def main():
    number_dict = dict()
    number_dict = update_number_dict(number_dict, calls, 0, 1, dur_index=-1)
    max_duration = max(number_dict.values())
    max_numbers = [num for num, dur in number_dict.items() if dur == max_duration]
    print(('{} spent the longest time, {} seconds, on the phone during '
           'September 2016.').format(','.join(max_numbers), max_duration))

if __name__ == '__main__':
    main()
