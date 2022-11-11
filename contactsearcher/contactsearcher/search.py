"""Search for an email address given a fragment of a job description."""

from typing import List

import csv

# note: see https://docs.python.org/3/library/csv.html


def search_for_email_given_job(job_description: str, contacts: str) -> List[List[str]]:
    """Search for and return job description(s) given an email address."""
    contacts_list = []
    for line in contacts:
        contact = line.split(",")
        for item in contact:
            if " " in item:
                item.replace(",", "")
            ind_words = item.split(" ")
            for word in ind_words:
                if word.lower() == job_description.lower():
                    contacts_list.append(contact)
    return contacts_list
