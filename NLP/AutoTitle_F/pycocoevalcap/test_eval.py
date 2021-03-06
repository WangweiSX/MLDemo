#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2018/10/18 下午3:30 
# @Author : ComeOnJian 
# @File : test_eval.py 
import sys
sys.path.append('../')

from bleu.bleu import Bleu
from meteor.meteor import Meteor
from rouge.rouge import Rouge
from cider.cider import Cider

class EvalCap:
    ref_list = ['this is a reference sentence for sentence2 which was generated by your model']
    hyp_list = ['this is sentence2 which has been generated by your model']


    refs = {idx: [lines.strip()] for (idx,lines) in enumerate(ref_list)}
    hyps = {idx: [lines.strip()] for (idx,lines) in enumerate(hyp_list)}

    scorers = [
        (Bleu(4),['Bleu_1', 'Bleu_2', 'Bleu_3', 'Bleu_4']),
        # (Meteor(), "METEOR"),
        (Rouge(), "ROUGE_L"),
        (Cider(), "CIDEr")
    ]
    for scorer, method in scorers:
        print('computing %s score...' % (scorer.method()))
        score, scores = scorer.compute_score(hyps,refs)
        if type(method) == list:
            for sc, scs, m in zip(score, scores, method):
                # self.setEval(sc, m)
                print("%s: %0.3f" % (m, sc))
        else:
            # self.setEval(score, method)
            print("%s: %0.3f" % (method, score))
def setEval(score, method):
    pass



