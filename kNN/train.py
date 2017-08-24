from math import log
from porter import PorterStemmer

poslines = []
neglines = []

stopwords= open(r'stopwords.txt', 'r').read().splitlines()
dataset= open('training_set.csv', 'r')

dataset.readline()

poslines=[]
neglines=[]

for data in dataset:
    datalines = data.split(",")[1].strip('"').split(' ')
    DataClass = data.split(",")[0]
    if int(DataClass)==0:
        poslines.append(datalines)  
    if int(DataClass)==1:
        neglines.append(datalines)
        
print "The total positive words are: ", len(poslines)
print "The total negative words are: ", len(neglines)


#there are total 6397 positives and negatives.
#taking first N as training set, and then testset for validation
N= 6397
poslinesTrain= poslines[:3201]
neglinesTrain= neglines[:3196]

model = open('model_file.csv', 'w')

trainset= [(x,1) for x in poslinesTrain] + [(x,-1) for x in neglinesTrain]


stemmer= PorterStemmer()

def getwords(sentence):
    
    #this method returns important words from a sentence as list
    w = sentence
    #remove all things that are 1 or 2 characters long (punctuation)
    w= [x for x in w if len(x)>2]
    #get rid of all stop words
    w= [x for x in w if not x in stopwords]
    #stem each word
	#add bigrams
    w= w + [w[i]+' '+w[i+1] for i in range(len(w)-1)]
    w= list(set(w))
    return w

freq={}
trainfeatures= []
for line,label in trainset:
    words= getwords(line)

    for word in words: 
        freq[word]= freq.get(word, 0) + 1   
        
    trainfeatures.append((words, label))
    
#evaluate the test set
testset= open('test_set.csv', 'r')
testset.readline()

output = open("prediciton_file.csv", 'w') 

Ntr= len(trainset)
print Ntr
wrong=0
for testdata in testset:
    testwordssplit = testdata.split()
    testwords= getwords(testwordssplit)
    
    results=[]
    
    for trainwords, trainlabel in trainfeatures:
   
		#find all words in common between these two sentences
        commonwords= [x for x in trainwords if x in testwords]
        score= 0.0
		
        for word in commonwords:
            score += log(Ntr/freq[word])
            model.write("Word: " +str(word) + ",")
            model.write("Probablity: " + str(score))
   
        results.append((score, trainlabel))

    results.sort(reverse=True)

    toplab= [x[1] for x in results[:10]]
    numones= toplab.count(1)
    numnegones= toplab.count(-1)
	
    if numnegones> numones:
        output.write("0," + testdata)
    else:
        output.write("1," + testdata)
output.close()

    