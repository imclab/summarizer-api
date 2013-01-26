# -*- coding: utf-8 *-*
'''
The following is a naive, unsupervised text summarizer.
It extracts N of the text's most salient sentences.
Salience is defined as the average of the tf-idf weights of the
words in a sentence.

'''
from nltk import sent_tokenize, word_tokenize
from collections import Counter
from math import log10


class Tfidf_summarizer():

    def __init__(self):
        pass

    def summarize(self, text, extract_percent):
        sentences = sent_tokenize(text)
        #collections_tokens = word_tokenize(text)
        #collection_counter = Counter(collections_tokens)
        sent_saliences = []
        scored_sents = []
        num_to_extract = 4

        for index, sentence in enumerate(sentences):
            sent_salience = 0
            sent_tokens = word_tokenize(sentence)
            sent_counter = Counter(sent_tokens)
            for token in sent_tokens:
                tf = sent_counter[token]
                idf = log10(len(sentences) / sent_counter[token])
                tfidf = tf * idf
                sent_salience += tfidf
            normalized_salience = sent_salience / len(sent_tokens)
            sent_saliences.append(normalized_salience)
            scored_sents.append((normalized_salience, sentence, index))

        scored_sents.sort(key=lambda tup: tup[0], reverse=True)
        selected_sents = sorted(
            scored_sents[:num_to_extract], key=lambda tup: tup[2])
        #print 'Original text:\n%s\nNumber of sentences: %s\n\n' % (
            #text, len(sentences))
        #print 'Extracted text:\n%s\nNumber of sentences: %s' % (
            #' '.join([i[1] for i in selected_sents]), num_to_extract)
        result = dict()
        result['summary'] = ' '.join(
            [i[1] for i in selected_sents])
        return result