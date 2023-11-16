# PEG

# check_existing_goals
Receives year and office id and checks if there are already records in the DB. If there are returns true, otherwise false

POST request
Incoming request data: {'year': number, 'officeId': number }
Output: boolean


# get_avarage_goal
Receives year and calculaters the avarage weight assigned to each person

POST request
Incoming request data: {'year': number }
Output: number