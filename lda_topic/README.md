# LDA - Topic Modeling

### this is a short snippet that takes advantage of the LdaModel class in the gensim package. 

Basically, it reads a list of excerpts from medical journals and clusters them into topics. 

#### The following contants can be changed to see the impact on the results

LONG_WORD_LEN = 12 # word length considered long and dumped to file for review (ignored)
NUM_OF_TOPICS = 5  # number of topic to produce for LDA
NUM_OF_PASSES = 10 # number of passes for LDA model (needed to improve randomization)
NUM_OF_WORDS = 6   # number of words to include in each topic 

#### Input file
https://nlp.stanford.edu/software/tmt/tmt-0.4/

#### The output
Running two trials to see if any difference between runs

Trial 1
avg words/entry: 79.72
(0, '0.016*"gene" + 0.009*"sequence" + 0.008*"cell" + 0.007*"expression" + 0.005*"transcription" + 0.005*"dna"')
(1, '0.006*"cell" + 0.006*"study" + 0.005*"rna" + 0.004*"%" + 0.003*"method" + 0.003*"cancer"')
(2, '0.010*"patient" + 0.007*"%" + 0.005*"study" + 0.005*"data" + 0.003*"level" + 0.003*"effect"')
(3, '0.013*"dna" + 0.006*"cell" + 0.006*";" + 0.005*"sequence" + 0.004*"%" + 0.004*"study"')
(4, '0.014*"sequence" + 0.010*"gene" + 0.010*"dna" + 0.010*"protein" + 0.008*"region" + 0.008*"rna"')


Trial 2
avg words/entry: 79.72
(0, '0.007*"gene" + 0.006*"site" + 0.006*"dna" + 0.006*"study" + 0.006*"%" + 0.005*"sequence"')
(1, '0.005*"%" + 0.004*"patient" + 0.004*"cell" + 0.004*"group" + 0.003*"dna" + 0.003*"activity"')
(2, '0.014*"dna" + 0.011*"gene" + 0.006*"sequence" + 0.006*"cell" + 0.004*"region" + 0.004*"promoter"')
(3, '0.012*"sequence" + 0.009*"cell" + 0.008*"gene" + 0.006*"protein" + 0.005*"data" + 0.004*"analysis"')
(4, '0.010*"protein" + 0.010*"rna" + 0.010*"dna" + 0.009*"sequence" + 0.008*"cell" + 0.005*"\'"')

#### You can see that each trial produces 5 "topics" with the 6 most relevent words. Now a domain knowledge expert can define appropriate topics for each. 