#!/usr/bin/python
"""
Top Tags

We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

For an extra challenge you can think how to get a top 10 list of tags, where they are ordered by some weighted score by your choice.
"""

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if(len(line)) == 19:
			node_type = line[5]
            tagnames = line[2]
            if(node_type == 'question'):
                tags = tagnames.split()
                for tag in tags:
                    writer.writerow([tag, id])

if __name__ == "__main__":
    mapper()