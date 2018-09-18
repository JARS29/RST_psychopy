#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trials import *

experiment_session = int(raw_input("Qual o numero da secao? "))
text_instructions = "Bem-vindo ao experimento\nA seguir, você vai encontar uma série de frases apresentadas em sequências de 2, 3, 4, 5, 6 sentenças (em ordem aleatória).\n" \
                    "Sua tarefa vai ser ler as frases de forma natural, em voz alta e tentar lembrar a última palavra de cada sentença.\nUm simbolo '+' vai parecer no momento quando você deve " \
                    "dizer as palavras a serem lembradas (em qualquer ordem).\n \n" \
                    "Vamos praticar, presione qualquer tecla para começar um sesão de prática."

text_instructions_s1 = "Preparado?\nVamos começar com o experimento. Presione qualquer tecla para começar a primeira sessão."

text_final_s1 = "Pronto!!!\nA primeira sessão terminou. Aguarde ao experimentador para responder as perguntas."

text_instructions_s2 = "Preparado?\nVamos começar com o experimento. Presione qualquer tecla para começar a segunda sessão."

text_final_s2 = "Pronto!!!\nO experimento terminou. Aguarde ao experimentador para responder as perguntas dessa sessão.\n \n" \
                "Muito obrigado pela participação."


# Store info about the experiment session
expName = 'Reading Span Test'  # from the Builder filename that created this script

if experiment_session == 1:
    # Experiment setting
    expInfo = {u'Session': u'01', u'Participant': u''}
    thisExp = setting_exp(expName, expInfo)

    # Labstreaminglayer setting
    outlet=LSL_initizialization(str(expInfo[u'Session']+'-'+expInfo[u'Participant']))

    # Setup monitor
    win = setting_monitor('default', 80, expInfo)
    # Instructions trial
    instructions_trial(win, text_instructions)

    # Practice trial
    sentences_practice = 'common\sentences_practice.xlsx'
    practice_trial(win,sentences_practice,thisExp,expInfo)

    # Final instructions before experiment
    instructions_trial(win, text_instructions_s1)

    # Experiment session 1

    # Sentences_session _1
    sentences_s1 = 'common\sentences_s1.xlsx'
    experiment_trial(win,  sentences_s1, thisExp, expInfo, outlet)

    #Final message session 1
    instructions_trial(win, text_final_s1)

    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()

elif experiment_session == 2:
    # Experiment setting
    expInfo = {u'Session': u'02', u'Participant': u''}
    thisExp = setting_exp(expName, expInfo)

    # Labstreaminglayer setting
    outlet=LSL_initizialization(expInfo[u'Session']+expInfo[u'Participant'])

    # Setup monitor
    win = setting_monitor('default', 80, expInfo)

    # Instructions for the second session
    instructions_trial(win, text_instructions_s2)

    # Experiment session 2

    # Sentences_session 2
    sentences_s2 = 'common\sentences_s2.xlsx'
    experiment_trial(win, sentences_s2, thisExp, expInfo, outlet)

    # Final message session 2 and experiment
    instructions_trial(win, text_final_s2)

    thisExp.abort()  # or data files will save again on exit
    win.close()
    core.quit()