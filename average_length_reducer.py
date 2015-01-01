#!/usr/bin/python

import sys
import csv

def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    prev_question = None
    current_question = None
    type = None
    length = question_length = answer_count = total_answer_length = 0

    for line in reader:
        if(len(line) == 3):
            current_question, type, length = line

            if(type == 'Q'):
                question_length = length
            else:
                answer_count = answer_count + 1
                total_answer_length = total_answer_length + int(length)

        if prev_question and prev_question != current_question:
            if answer_count > 0:
                average_answer_length = total_answer_length / answer_count
            else:
                average_answer_length = 0

            print "{0}\t{1}\t{2}".format(prev_question, question_length, average_answer_length)
            question_length = answer_count = total_answer_length = 0

        prev_question = current_question

    if prev_question != None:
            if answer_count > 0:
                average_answer_length = total_answer_length / answer_count
            else:
                average_answer_length = 0

            print "{0}\t{1}\t{2}".format(prev_question, question_length, average_answer_length)

if __name__ == "__main__":
    reducer()