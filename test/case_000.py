# -*- coding: utf-8 -*-
'''

'''
import json
import urllib2
import unittest


class Test_summarizer(unittest.TestCase):

    def runTest(self):
        text = """
        Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.But, in a larger sense, we cannot dedicate—we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom— and that government of the people, by the people, for the people, shall not perish from the earth.
        """
        text.decode('utf-8', 'ignore')
        print 'Starting test'
        d = {
            "text": text,
            "extract_percent": 40,
            }
        #req = urllib2.Request('http://ec2-50-17-103-0.compute-1.amazonaws.com/summarizer')
        req = urllib2.Request('http://127.0.0.1:8004/summarize')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(d)).read()
        response = json.loads(response)
        summary = response['summary'].encode('utf-8', 'ignore')
        print 'Summary:\n%s' % summary
        #self.assertEqual(best_answer.lower(), 'harold ramis')

if __name__ == '__main__':
    unittest.main()