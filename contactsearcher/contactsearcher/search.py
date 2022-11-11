"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    # generates empty list
    contacts_list = []
    # opens and reads the csv file
    with open(contacts, mode='r') as csv_file:
        contact_reader = csv.reader(csv_file, delimiter=',')
        # iterates through the lines in the file
        for row in contact_reader:
            # searches the descriptions
            if job_description.lower() in row[1].lower():
                contacts_list.append(row)

    return contacts_list
