
import pandas as pd

# Loading the spam data
# ham is the label for non-spam messages
spam = pd.read_csv('../nlp-course/spam.csv')
spam.head(10)
print(spam.head())