# Sentiment-Analysis---Movie-Reviews

Movie reviews are a crucial aspect of sensitizing an audience towards a movie.
They provide people with multiple perspectives and allow people to decide whether to watch a movie.
Movie reviews are far more personalized than statistical ratings or scores.
They embody the opinion of the reviewer, and are highly subjective in nature.
A crucial characteristic of the reviews is their sentiment, or overall opinion towards the subject matter.
As such, sentiment analysis is performed to systematically identify, extract, quantify, and study the reviews.

Sentences in reviews contain independent clauses that express different sentiments toward different aspects of a movie.
Labelling these articles with their sentiment would provide succinct summaries to readers.
The research paper implemented examines the effectiveness of applying machine learning techniques to the sentiment classification problem.
The method adopts a classifier approach of computing the sentiment of a clause from the prior sentiment scores assigned to individual words, taking into consideration the grammatical dependency structure of the clause, and delicately handling negative phrases.

The output sentiment scores can be used to identify the most positive and negative clauses or sentences with respect to particular movie aspects.
 
The problem statement involves:
  1. Building a classifier for polarity detection of movie reviews.
  2. Training and testing the classifier using a huge set of positive and negative reviews.
  3. Performing sentiment analysis and classification - Uncovering the attitude of the author on a particular topic from the      written text; alternatively known as “opinion mining” and “subjectivity detection”.
  4. Using natural language processing and machine learning techniques to find statistical and/or linguistic patterns in the
     text that reveal attitudes.

The objective is to solve the problem statement, and simultaneously determining the answers for the following:
  1. The degree to which the polarity of the movie reviews can be derived accurately.
  2. The important features which can be extracted from the raw text that have the greatest influence on the classification.
  3. Whether smaller data sets are more easily classified accurately than larger ones.

The problem of building a classifier for polarity detection involves two major steps.
The first step is to reduce the document to a feature vector.
The feature vector should embody characteristics of the document that lead to an intuitive suggestion towards the polarity.
All documents have been reduced to the adjectives present in them, under the assumption that adjectives carry major semantic weight that points towards its polarity.
After the construction of the feature vector, the next step is to build a classifier using an appropriate algorithm. 

The Naïve Bayes and kNN classifiers are used, along with some pre-processing steps.
The pre-processing steps are:
  1. Removal of “stop words”: Stop words are certain words which don’t make a difference to the result. These words are
     removed from the dataset so as to just concentrate on words that matter in predicting the polarity of the movie review.
     A very common English stop word list provided on (http://www.ranks.nl/resources/stopwords.html) is referred to for the
     stop word list.
  2. Stemming: Stemming is the process for reducing inflected/derived words to their stem, base or root form—generally a
     written word form. The stem is such that related words map to the same stem, even if this stem is not a valid word.
     Stemming is done via Porter Stemming algorithm, and results in: car, cars, car's, cars' => car
  3. Removal of any word of two characters or less: Such words are typically punctuations, and are thus removed. 

Naïve Bayes has higher percentages of accuracy for the testing datasets than kNN classification algorithm.
The reason for such performance is speculated to be the size of the data set: kNN performs better as the magnitude of the dataset increases.
The current size of the dataset causes the performance of kNN to dip.
For smaller datasets, Naïve Bayes can outperform KNN. 
Of note is the fact that using a lot of feature extraction methods can easily over-fit the dataset, resulting in poor performance against another dataset.
This can be observed while experimenting as Naïve-Bayes with stopword removal, stemming, different scoring pattern for positive and negative words.
The dataset overfitted and ended up with an accuracy of 25% with the second dataset. The accuracy was regained to back to normalcy after removing the different scoring pattern for positive and negative words based on a particular list of words.

The research paper being referred to is – “Thumbs up? Sentiment Classification using Machine Learning Techniques”; by Bo Pang and Lillian Lee and Shivakumar Vaithyanathan

The training dataset and first testing dataset is at: https://inclass.kaggle.com/c/cs6998/data

The second testing dataset is at: https://www.cs.cornell.edu/people/pabo/movie-review-data
