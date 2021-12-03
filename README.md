# ML1

- stack.xlsx is a file formed by stack.py which collects information on remote jobs by web scraping from the webpages of stackoverflow.com,
similarly monster.xlsx is a file formed by monster.py which collects information on remote jobs from the webpages of monster.com,
and indeed.xlsx is a file formed by indeed.py which collects information on remote jobs from the webpages of indeed.com

- union.py file merges the stack, indeed  and monster excel files and produces union.xlsx and accuracies.xlsx

- accuracies.xlsx is the machine learning accuracy scores for the classifiers RandomForest, KNeighbors, DecisionTree, NaiveBayes GaussianNB and SVC.

## Explanation on the Columns of the excel file table union.xlsx

SKILLS:  words that appear on the page belonging to the fixed list (named skills in stack.py)  formed of 1208 words

\# SKILLS: number of words in SKILLS column

The 41 columns from "agile" to "windows" show the appeareance of the word. For example,
agile: is 1 if the word "agile" exists in the webpage, and 0 if "agile" does not exist

The 41 words agile, analysis, android, ... , windows are the words from the list skills (allwords in union.py) which appear in at least 500 webpages.

## Explanation on the Rows and Columns of the excel file table accuracies.xlsx

Example: The number on row magento and column NaiveBayes is the accuracy score according to NaiveBayes GaussianNB classifier where X is the 41 columns except the "magento" column and y is the "magento" column. Train-test split is done with test size 50 %.

