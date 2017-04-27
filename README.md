This is for a Kaggle competition, https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries
"predict the number of inquiries a new listing receives"
The competition ended earlier than I expected, so this is abortive (ie the .r is basically just data wrangling)

##  parse.py ###
For both test and training sets, writes a csv for each feature (from two large json files which are too big to upload to github)


### join-anly.r ###
For both training and test sets, joins all features into a single data frame.
To Do: use a single for loop for both joins
