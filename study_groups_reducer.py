#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    prev_thread = None
    current_thread = None
    authors = []

    for line in reader:
        if(len(line) == 2):
            current_thread, author = line

        if prev_thread and prev_thread != current_thread:
            writer.writerow([prev_thread, ','.join(authors)])
            authors = []

        prev_thread = current_thread
        authors.append(author)

    if prev_thread != None:
        writer.writerow([prev_thread, ','.join(authors)])

if __name__ == "__main__":
    reducer()