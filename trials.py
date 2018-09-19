#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import gui, visual, core, data, event, logging, monitors
from psychopy.constants import (NOT_STARTED, STARTED,
                                STOPPED, FINISHED)
from pylsl import StreamInfo, StreamOutlet
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Labstreaminglayer
def LSL_initizialization(user_info):
    info = StreamInfo('Reading_Span_Test', 'Markers', 1, 0, 'string', str(user_info))
    outlet = StreamOutlet(info)
    raw_input('Setting LSL \nPlease press Enter for starting')
    return outlet


# Experiment information
def setting_exp(expName,expInfo):
    # Path
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)
    # Pop-up window
    # dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    # if dlg.OK == False:
    #     core.quit()  # user pressed cancel
    expInfo['date'] = data.getDateStr()  # add a simple timestamp
    expInfo['expName'] = expName

    # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['Participant'], expInfo['date'])

    # An ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(name=expName, version='',
                                     extraInfo=expInfo, runtimeInfo=None,
                                     originPath=None,
                                     savePickle=True, saveWideText=True,
                                     dataFileName=filename)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename + '.log', level=logging.WARNING)
    logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
    return thisExp



# Monitor
def setting_monitor(name, distance, expInfo):
    # Setup Monitor
    from win32api import GetSystemMetrics

    mon = monitors.Monitor(name)
    mon.setDistance(distance)
    mon_size = mon.getSizePix()
    if mon_size==None:
        mon_size=[GetSystemMetrics(0),GetSystemMetrics(1)]
    print(mon_size)
    # Setup Window
    win = visual.Window(
        size=mon_size, fullscr=True, screen=0,
        allowGUI=False, allowStencil=False,
        monitor=mon, color='black', colorSpace='rgb',
        blendMode='avg', useFBO=True,
        units='norm')
    expInfo['frameRate'] = win.getActualFrameRate()
    if expInfo['frameRate'] != None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess

    return win

# Instructions trial
def instructions_trial(win, text, endExpNow=endExpNow, routineTimer=routineTimer):
    instructPracticeClock = core.Clock()
    instruction_stimuli = visual.TextStim(win=win, name='instr1',
                             text=text, font='Arial',
                             pos=[-0.1, 0], height=0.1, wrapWidth=1.5, ori=0,
                             bold=True, depth=1,
                             color='white', colorSpace='rgb', opacity=1)

    # ------Prepare to start Routine "instructPractice"-------
    t = 0
    instructPracticeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_instruction = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructPracticeComponents = [instruction_stimuli, key_instruction]
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "instructPractice"-------
    while continueRoutine:
        # get current time
        t = instructPracticeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *instr1* updates
        if t >= 0.0 and instruction_stimuli.status == NOT_STARTED:
            # keep track of start time/frame for later
            instruction_stimuli.tStart = t
            instruction_stimuli.frameNStart = frameN  # exact frame index
            instruction_stimuli.setAutoDraw(True)

        # *ready1* updates
        if t >= 0.0 and key_instruction.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_instruction.tStart = t
            key_instruction.frameNStart = frameN  # exact frame index
            key_instruction.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_instruction.status == STARTED:
            theseKeys = event.getKeys()

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructPracticeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "instructPractice"-------
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

# recall trial
def recall(win, thisExp, save=False):
    endExpNow = False  # flag for 'escape' or other condition => quit the exp

    recall_clock = core.Clock()
    recall_cross = visual.ShapeStim(
        win=win, name='polygon', vertices='cross',
        size=(0.1, 0.1),
        ori=0, pos=(0, 0),
        lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
        fillColor=[1, 1, 1], fillColorSpace='rgb',
        opacity=1, depth=0.0, interpolate=True)
    t1 = 0
    recall_clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_recall = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [recall_cross, key_recall]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t1 = recall_clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon* updates
        if t1 >= 0.0 and recall_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            recall_cross.tStart = t1
            recall_cross.frameNStart = frameN  # exact frame index
            recall_cross.setAutoDraw(True)

        # *key_resp_2* updates
        if t1 >= 0.0 and key_recall.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_recall.tStart = t1
            key_recall.frameNStart = frameN  # exact frame index
            key_recall.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_recall.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_recall.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                key_recall.keys = theseKeys[-1]  # just the last key pressed
                key_recall.rt = key_recall.clock.getTime()
                continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    # -------Ending Routine "trial"-------

    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    blank_screen(win)

    if save:
        if key_recall.keys != None:  # we had a response
            return key_recall.rt
    routineTimer.reset()



# blank screen after each sentence
def blank_screen(win):

    blankClock = core.Clock()
    cross = visual.ShapeStim(
        win=win, name='cross', vertices='cross',
        size=(0.03, 0.03),
        ori=0, pos=(-0.9, 0.07),
        lineWidth=1, lineColor=[1, 1, 1], lineColorSpace='rgb',
        fillColor=[1, 1, 1], fillColorSpace='rgb',
        opacity=1, depth=0.0, interpolate=True)
    # ------Prepare to start Routine "blank"-------
    t = 0
    blankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [cross]
    for thisComponent in blankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon* updates
        if t >= 0.0 and cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            cross.tStart = t
            cross.frameNStart = frameN  # exact frame index
            cross.setAutoDraw(True)
        frameRemains = 0.0 + 0.3 - win.monitorFramePeriod * 0.75  # most of one frame period left
        if cross.status == STARTED and t >= frameRemains:
            cross.setAutoDraw(False)

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)

    routineTimer.reset()


# Practice trial
def practice_trial (win, sentences, thisExp, expInfo, endExpNow=endExpNow):
    practice_clock = core.Clock()
    trials = data.TrialHandler(nReps=1.0, method='sequential',
                                 extraInfo=expInfo, originPath=-1,
                                 trialList=data.importConditions(sentences),
                                 seed=None, name='practice')
    #text
    practice_text = visual.TextStim(win=win, name='practice_text',
                           text='',
                           font='Arial',
                           pos=[-0.1, 0], height=0.15, wrapWidth=1.7, ori=0,
                           color=1.0, colorSpace='rgb', opacity=1,
                           depth=0.0);

    span=[2,3]
    temp=0
    ntrial=0
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec ('{} = thisTrial[paramName]'.format(paramName))

    for thisTrial in trials:
        currentLoop = trials
        ntrial+=1
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec ('{} = thisTrial[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        t = 0
        if temp==span[0]:
            #continueRoutine = False
            recall_flag=True
            recall(win, thisExp)
            span.reverse()
            temp=0
        temp += 1
        practice_clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        practice_text.setText(sentences)
        practice_key = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [practice_text, practice_key]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = practice_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text* updates
            if t >= 0.0 and practice_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_text.tStart = t
                practice_text.frameNStart = frameN  # exact frame index
                practice_text.setAutoDraw(True)
            frameRemains = 0.0 + 7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_text.status == STARTED and t >= frameRemains:
                practice_text.setAutoDraw(False)

            # *key_resp_2* updates
            if t >= 0.0 and practice_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                practice_key.tStart = t
                practice_key.frameNStart = frameN  # exact frame index
                practice_key.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 7.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if practice_key.status == STARTED and t >= frameRemains:
                practice_key.status = STOPPED
            if practice_key.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #     print('abc')
        #     recall(win, expInfo)
        #     recall_flag=False
        #     temp=0
        # else:
        if temp!=span[0]:
            blank_screen(win)
        if currentLoop.nTotal == ntrial:
            recall(win, thisExp)

def experiment_trial (win, sentences, thisExp, expInfo,outlet, endExpNow=endExpNow):
    experiment_clock = core.Clock()
    trials = data.TrialHandler(nReps=1.0, method='sequential',
                               extraInfo=expInfo, originPath=-1,
                               trialList=data.importConditions(sentences),
                               seed=None, name='practice')
    # text
    experiment_text = visual.TextStim(win=win, name='experiment_text',
                                    text='',
                                    font='Arial',
                                    pos=[-0.1, 0], height=0.15, wrapWidth=1.7, ori=0,
                                    color=1.0, colorSpace='rgb', opacity=1,
                                    depth=0.0);

    span = [3, 5, 6, 4, 2, 3, 4, 2, 5, 6, 4, 6, 2, 3, 5, 2, 3, 6, 4, 5] # running four times random.sample(range(2,7),5)
    if expInfo['Session'] == '02':
        span = span[::-1]
    recall_time=0.0
    index = 0
    temp = 0
    ntrial = 0
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec ('{} = thisTrial[paramName]'.format(paramName))

    for thisTrial in trials:
        currentLoop = trials
        ntrial += 1
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec ('{} = thisTrial[paramName]'.format(paramName))

        # ------Prepare to start Routine "trial"-------
        t = 0
        if temp == span[index]:
            # continueRoutine = False
            outlet.push_sample(['Start_recall'])
            time.sleep(0.01)
            recall_time=recall(win, thisExp, save=True)
            blank_screen(win)
            trials.addData('recall.rt', recall_time)
            outlet.push_sample(['Finish_recall'])
            time.sleep(0.01)
            temp = 0
            index+=1

        temp += 1
        experiment_clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        experiment_text.setText(sentences)
        experiment_key = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [experiment_text, experiment_key]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = experiment_clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame

            # *text* updates
            if t >= 0.0 and experiment_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                experiment_text.tStart = t
                experiment_text.frameNStart = frameN  # exact frame index
                experiment_text.setAutoDraw(True)
                outlet.push_sample(['Start_sentence'])
                time.sleep(0.01)
            frameRemains = 0.0 + 7 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if experiment_text.status == STARTED and t >= frameRemains:
                experiment_text.setAutoDraw(False)

            # *key_resp_2* updates
            if t >= 0.0 and experiment_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                experiment_key.tStart = t
                experiment_key.frameNStart = frameN  # exact frame index
                experiment_key.status = STARTED
                # keyboard checking is just starting
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 7.0 - win.monitorFramePeriod * 0.75  # most of one frame period left
            if experiment_key.status == STARTED and t >= frameRemains:
                experiment_key.status = STOPPED
            if experiment_key.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])

                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    # a response ends the routine
                    experiment_key.keys = theseKeys[-1]  # just the last key pressed
                    experiment_key.rt = experiment_key.clock.getTime()
                    continueRoutine = False

            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished

            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()

        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)

        if temp != span[index]:
            blank_screen(win)

        if currentLoop.nTotal == ntrial:
            outlet.push_sample(['Start_recall'])
            time.sleep(0.01)
            recall_time=recall(win, thisExp, save=True)
            trials.addData('recall.rt', recall_time)
            outlet.push_sample(['Finish_recall'])
            time.sleep(0.01)



        if len(theseKeys) == 0:  # if the time is reached
            trials.addData('experiment_key_read.rt', 6.9999306492)
            outlet.push_sample(['time_sentence'])
            time.sleep(0.01)
        else:  # we had a response
            trials.addData('experiment_key_read.rt', experiment_key.rt)
            outlet.push_sample(['key_sentence'])
            time.sleep(0.01)


        routineTimer.reset()
        thisExp.nextEntry()

    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(thisExp.dataFileName + '.xlsx', sheetName='trials',
                       stimOut=params,
                       dataOut=['all_raw'])
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(thisExp.dataFileName + '.csv')
    thisExp.saveAsPickle(thisExp.dataFileName)
    logging.flush()


