<img width="307" alt="Screen Shot 2022-07-13 at 10 30 44 PM" src="https://user-images.githubusercontent.com/107584891/178901635-d9df4c0a-cca1-4069-a81d-26410f5d57fb.png">

# Election_Analysis
## Analysis of Elections Result
## Project Overview
A Colorado Board of Elections employee has given the following tasks to complete the election audit of a recent local congressional election using a set of programmatic tools of Python, Visual Studio Code, and Git. We have to determine the total number of votes cast in the election.

I have created a python script and would read and write data, performed calculations on the counts, and used loops and conditional statements to report our analysis.
## Results:


How many votes were cast in this congressional election?
Total Votes: 369,711


Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
County Votes:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

Which county had the largest number of votes?
Denver

Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
# Winner: Diana DeGette
Winning Vote Count: 272,892
Winning Percentage: 73.8%

## Resources
Software: Python 3.7.7, Visual Studio Code, 1.47.3, Git 2.27

## Summary
The Election analysis shows that there were 369711 votes cast in the election. 
The candidates with their percentage of votes and their total number of votes:
Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)
The County Votes are as follows:
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)
The Largest County Turnout: Denver
The Winner of the election was Diana DeGette with Winning Percentage of 73.8% and 
272,892 number of votes.

## Challenge Overview
The data we need to retrieve.
Capture and calculate the total number of votes cast through looping.
Get a complete list of candidates who received votes.
Calculate the total number of votes each candidate received.
Calculate the percentage of votes each candidate won.
Determine the winner of the election based on popular vote.

## Challenge summary
Colorado saw three counties tally up to 369,711 votes. The biggest of the counties with a 82.8% was Denver. We processed the votes for three candidates of Charles, Diana, and Raymon. With 73.8% of the votes towards Diana DeGette, that is 272,892 of the 369,711 total votes.
## Election-Audit Summary
The election commission may wish to consider some additional functionality to the Python script used to develop this audit. For example, it might be interesting to discover the winning candidate by county. By simply adding an additional "if" statement to the current code, the number of candidates per county could be tallied, providing deeper insight into the voting patterns within a given county. It would also be interesting to find voter turnout by polling location. A polling location column would need to be added to the election_results_csv file, but the ability to drill deeply into polling locations would provide information on voter volume, and may assist in planning future voting locations based on the analysis. For example, the analysis may reveal that some polling locations are under utilized, while others have more voter participation than staff can manage, which would allow a more data-driven polling plan during future elections.

The provided Python coded audit application is robust and can be used on a much wider scale. The data provided for this audit includes three counties in the state, but the audit program can accomodate much larger data sets, and could be expanded to all counties in Colorado. I propose the election committee adopt this simple analysis tool as the state-wide solution for congressional election audits. Though simplistic in design, the application is powerful, customizable, repeatable and simple to execute.


