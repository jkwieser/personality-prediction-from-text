# Personality Prediction from Text
## Description
- Data on personality types was gathered (MBTI and big five) for further information, see below.
- The situation on the data was evaluated. There is much more MBTI data available which is scientifically less reliant, but there is only very few data on the BIG FIVE traits. Machine Learning algorithms thrive on data so a approach created to combine MBTI and BIG Five data. 
- The data from three different sources was converted in mutual form and preprocessed to the needs of ML algorithms
- features from text were extracted to vectorize the data with bags of words and GloVe approach
- several supervised classification learning algorithm were used and trained to predict on future unknown text
- the results of the classifiers were evaluated
- a predictor was developed who predicts traits and visualizes them:

![Image](https://github.com/joegog/personality-detection-text/blob/master/docu/predict.PNG?raw=true)

## Motivation
Inspired by [the paper from sentic.net](https://sentic.net/deep-learning-based-personality-detection.pdf) this topic was chosen during  studies at University of applied Sciences Wiener Neustadt, Computer Science, Data Science. Some time was spent on [Dr. Jordan B. Petersons Personality lectures](https://www.youtube.com/playlist?list=PL22J3VaeABQApSdW8X71Ihe34eKN6XhCi) and some understanding was gathered on the BIG FIVE personality model and its applications. As I'm continuously stunned by the complexity of the human psyche, the motivations and desires of human beings I am of course also fascinated by Machine Learning applications, which are nothing else than the pursue to reverse engineer the human brain and discover the yet unknown algoritm of the human brain. 
So this first machine learning python application marks my start in the huge world of machine learning and artificial intelligence, please be critical.

## The big five personality model
The Big Five personality traits, also known as the five-factor model (FFM) and the OCEAN model, is a taxonomy, or grouping, for personality traits.
The five factors are:
- Openness to experience (inventive/curious vs. consistent/cautious)
- Conscientiousness (efficient/organized vs. easy-going/careless)
- Extraversion (outgoing/energetic vs. solitary/reserved)
- Agreeableness (friendly/compassionate vs. challenging/detached)
- Neuroticism (sensitive/nervous vs. secure/confident)

Quoted from and further information: https://en.wikipedia.org/wiki/Big_Five_personality_traits

## The Myers–Briggs Type Indicator 
The Myers–Briggs Type Indicator (MBTI) is an introspective self-report questionnaire indicating differing psychological preferences in how people perceive the world and make decisions. 


| _             | Subjective                | Objective                           |
| ------------- |:-------------:            | --------------------------------:   |
| Deductive     | **I**ntuition/**S**ensing |  **I**ntroversion/**E**xtraversion	|
| Inductive     | **F**eeling/Thinking      |   **P**erception/**J**udging        |

The combinations as four pairs of preferences lead to 16 possible combinations aka types. The 16 types are typically referred to by an abbreviation of four letters—the initial letters of each of their four type preferences (except in the case of intuition, which uses the abbreviation "N" to distinguish it from introversion). For instance:

ESTJ: extraversion (E), sensing (S), thinking (T), judgment (J)
INFP: introversion (I), intuition (N), feeling (F), perception (P)
 	              	
Quoted from and further information: https://en.wikipedia.org/wiki/Myers%E2%80%93Briggs_Type_Indicator

## Differences and commonalities of the Big Five and MBTI

Adrian Furnham 1996 concludes a corellation of his 1996 paper [The big five versus the big four: the relationship between the Myers-Briggs Type Indicator (MBTI) and NEO-PI five factor model of personality](https://www.sciencedirect.com/science/article/abs/pii/0191886996000335) concludes a correlation between these traits from:

|  MBTI            |  Big Five                           |
| :-------------:            | --------------------------------:   |
| **I**ntuition/**S**ensing |  Openness to experience (corellates with N)   |
|  **F**eeling/Thinking      |   Agreeableness (correlates with F)       |
|  **P**erception/**J**udging      |   Conscientiousness (correlates with J)        |
|  **I**ntroversion/**E**xtraversion      |   Extraversion (correlates with E)       |
|  not available in MBTI              |   Neuroticism       |

## Goal of this project
- Predicting personality traits in high accuracy with classifiers trained from text data which is labeled with the personality types.
- gathering familiarty with machine learning core concepts
- trying to find an approach to combine MBTI data with BIG FIVE data to increase amount of data to train machine learning classifiers

### Results

| EXT | NEU| AGR | CON | OPN|
| :-------------:| :--------:   |  :--------:   |  :--------:   | :--------:   |
|   77.18    | 61.74|  75.51  | 70.34 | 80.39 |

for detailed results 

# Tech overview 
## data for training
### stream of consciousness essays "data/essays.csv"
This is the scientific gold standard from psychology, controlled environment collected stream of consciousness by James Pennebaker and Laura King labelled with Big Five personality traits. See: http://web.archive.org/web/20160519045708/http://mypersonality.org/wiki/doku.php?id=wcpr13

### emotion lexicon "data/Emotion_Lexicon.csv"
For scentence filtering a lexicon containing ~ 14,000 words was used. Further Information:
https://www.saifmohammad.com/WebPages/NRC-Emotion-Lexicon.htm

### (MBTI) Myers-Briggs Personality Type Dataset "mbti_1.csv"
From [Kaggle](https://www.kaggle.com/datasnaek/mbti-type): This data was collected through the [PersonalityCafe forum(https://www.personalitycafe.com/forum/), as it provides a large selection of people and their MBTI personality type, as well as what they have written.

### scraped data from reddit from "typed_comments.csv"
Props to Matej Gjurković, and his 2018 paper [Reddit: A Gold Mine for Personality Prediction](https://www.researchgate.net/publication/325445581_Reddit_A_Gold_Mine_for_Personality_Prediction) who provided me his scraped data from personality subreddits, where people show their personality types in the forum and therfore provide labelled text comments and posts.
I cannot share the data.

## Used Methods

### Classification
- SVM (sklearn)
- Decision Tree (sklearn)
- Naive Bayes (sklearn)
- Logistic Regression (sklearn)
- Random Forest (sklearn)

### Feature extraction
- Bags of Words (sklearn CountVectorizer)
- GloVe pretrained https://nlp.stanford.edu/projects/glove/

### scentence filtering
- scentences which contain no emotional charge (meaning they contain no word of the emotion lexicon) will be removed before further preprocessing.


### combining MBTI and BIG FIVE data
MBTI and BIG FIVE data was combined on the corellating traits. therefore the trait "neuroticism" from big five was lost. this explains the weaker results in the trait Neuroticism (NEU)

# repo overview / how to use

## if you just want to run with my pretrained models
1) just work with predict.ipynb and use your own text on the variable "text"
2) done, have fun predicting
3) if you want, check analysis_results.ipynb - this compares the feature extractions and classifiers in their score

## if you want to train on your own (with gloVe)
1) download glove pretrained models and put in the folder data/pretrained:
  - http://nlp.stanford.edu/data/glove.840B.300d.zip
  - http://nlp.stanford.edu/data/glove.6B.zip
2) run preprocessing.ipynb
   - choose the data you want to combine (essays, kaggle mbti, and if you have access reddit) 
   - this saves the preprocessed data in data/essays
   - this is required for further use to run the models
3)  run model_glove.ipynb for using preprocessing with GloVe
    OR
    run model_bow.ipynb for using preprocessing with Bags of Words and sklearn CountVectorizer
4) work with predict.ipynb and use your own text on the variable "text"
5) if you want, check analysis_results.ipynb - this compares the feature extractions and classifiers in their score

further info: essay.py
the class to save various data about the essays required


