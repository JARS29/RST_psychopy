#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from trials import *

text_instructions="Bem-vindo ao experimento\n Na sequência, você vai encontar uma série de frases apresentadas em sequências de 2, 3, 4, 5, 6 sentenças (em ordem aleatória)\n"" \
""Sua tarefa vai ser ler as frases de forma natural em voz alta e tentar lembrar a última palavra de cada sentença.\n"


# Store info about the experiment session
expName = 'Reading Span Test'  # from the Builder filename that created this script
expInfo = {u'Session': u'01', u'Participant': u''}
thisExp=setting_exp(expName,expInfo)


#Setup monitor
win=setting_monitor('default', 80, expInfo)
instructions_trial(win, text_instructions)
