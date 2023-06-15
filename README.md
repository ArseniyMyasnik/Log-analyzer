# Log-analyzer
Creates two reports from log file about user activities on server

This script creates two .csv files from logs. The first one contains types of errors and their count, sorted from the most common error to the least common error. The second one contains a list of all users who have used the system and how many INFO and ERROR messages they've generated. This report is sorted by username.

Example of log file:
Jun 16 13:47:24 ubuntu.local ticky: ERROR Ticket doesn't exist (Arseniy)
