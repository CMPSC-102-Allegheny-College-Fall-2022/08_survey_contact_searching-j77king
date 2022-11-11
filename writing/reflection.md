# Contact Searching

## Jake King

## Program Output

### What is the output from running the following commands?

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "engineer":

joe70@yahoo.com is a Network engineer
torresjames@white.info is a Electrical engineer
grahamjoel@castillo-gilbert.net is a Engineer, technical sales
gsutton@miller.com is a Engineer, maintenance
gharris@villarreal-snow.com is a Water engineer
williamsondavid@lopez.com is a Automotive engineer
ronald83@yahoo.com is a Maintenance engineer
zmarshall@yahoo.com is a Control and instrumentation engineer
christopher35@yahoo.com is a Civil engineer, consulting
jacquelinedavid@hotmail.com is a Engineer, electronics
espinozadaryl@hill-maddox.com is a Engineering geologist
edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

- `poetry run contactsearcher --job-description "neer" --contacts-file input/contacts.txt`

```
The contacts file contains 100 people in it! Let's get searching!

  We are looking for contacts who have a job related to "neer":

joe70@yahoo.com is a Network engineer
torresjames@white.info is a Electrical engineer
grahamjoel@castillo-gilbert.net is a Engineer, technical sales
gsutton@miller.com is a Engineer, maintenance
gharris@villarreal-snow.com is a Water engineer
williamsondavid@lopez.com is a Automotive engineer
ronald83@yahoo.com is a Maintenance engineer
zmarshall@yahoo.com is a Control and instrumentation engineer
christopher35@yahoo.com is a Civil engineer, consulting
jacquelinedavid@hotmail.com is a Engineer, electronics
espinozadaryl@hill-maddox.com is a Engineering geologist
edwardsjacob@gmail.com is a Chemical engineer

Wow, we found some contacts! Email them to learn about your job!
```

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### The source code statement that makes the `search` module available to `main`

```
from .search import search_for_email_given_job
```

This statement works because it looks at the file "search" located in the same directory as the main file, indicated by the period before search. Then, it imports the function needed from the search module.

#### The source code statement that extracts the current job description for a contact

```
if job_description.lower() in row[1].lower():
```

In this if statement, row[1] is the current job description. The program is therefore able to search this job description for the job_description value input in the command line.

#### Invocation of the function called `search_for_email_given_job`

```
 list_of_matches = search_for_email_given_job(job_description, contacts_file)
```

This line creates a list of matches (returned from the search function). To call the search function, it needs to pass two variables: the job_description given in the command line and the contacts_file also given in the command line.

#### Test case for the function called `search_for_email_given_job`

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### Execute trace of the `contactsearcher` program

TODO: Explain each function call that takes place for the following run of the program
TODO: Write at least one paragraph to explain every function call when running `contactsearcher`

TODO: Your discussion should start with the invocation of the `contactsearcher`
function in the `main` module, explain all of the subsequent function calls in
the correct order, and then show how the program's control returns to the
`contactsearcher` function in the `main` module.

- `poetry run contactsearcher --job-description "engineer" --contacts-file input/contacts.txt`

## Professional Assessment

### So far this semester, what is one area in which you have struggled? How did you overcome this challenge?

TODO: Provide a one-paragraph response that answers this question in your own words.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own words.
