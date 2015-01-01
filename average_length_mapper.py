#!/usr/bin/python
"""
Post and Answer Length

We are interested to see if there is a correlation between the length of a post and the length of answers.

Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer
(just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get
the required result.
"""

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if(len(line)) == 19:
			the_id = line[0]
			body = line[4]
			node_type = line[5]
            
            
            # Output "Q" for questions, and "Z" for answers in the second column, to have questions appear before answers (just for posterity)
            if(node_type == 'question'):
                print "{0}\t{1}\t{2}".format(the_id, "Q", len(body))
            elif(node_type == 'answer'):
                print "{0}\t{1}\t{2}".format(abs_parent_id, "Z", len(body))

if __name__ == "__main__":
    mapper()