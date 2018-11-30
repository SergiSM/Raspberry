#!/usr/bin/python3
# -*- coding: utf-8 -*-

v = [ ["cu1", "gr1", "as1", "pr1"],
      ["cu2", "gr2", "as2", "pr2"],
      ["cu3", "gr3", "as3", "pr3"],
      ["cu4", "gr4", "as4", "pr4"] ]

def cas_1_linia(assig):
    cu = ""
    ass = ""
    pr = ""
    for vv in v:
        if vv[2] in assig:
          cu = vv[0]  
          ass = vv[2]
          pr = vv[3]

    return (cu, ass, pr)

cu, ass, pr = cas_1_linia("cu2-as2")
print (cu, ass, pr)
