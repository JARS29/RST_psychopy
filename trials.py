#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, monitors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine
endExpNow = False  # flag for 'escape' or other condition => quit the exp
def setting_exp(expName,expInfo):
    # Path
    _thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
    os.chdir(_thisDir)
    # Pop-up window
    dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
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

def setting_monitor(name, distance, expInfo):
    # Setup Monitor
    mon = monitors.Monitor(name)
    mon.setDistance(distance)
    mon_size = mon.getSizePix()
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

# Instructions
def instructions_trial(win, text, endExpNow=endExpNow):
    instructPracticeClock = core.Clock()
    instr1 = visual.TextStim(win=win, name='instr1',
                             text=text, font='Arial',
                             pos=[0, 0], height=0.1, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             depth=0.0)

    # ------Prepare to start Routine "instructPractice"-------
    t = 0
    instructPracticeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ready1 = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructPracticeComponents = [instr1, ready1]
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
        if t >= 0.0 and instr1.status == NOT_STARTED:
            # keep track of start time/frame for later
            instr1.tStart = t
            instr1.frameNStart = frameN  # exact frame index
            instr1.setAutoDraw(True)

        # *ready1* updates
        if t >= 0.0 and ready1.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready1.tStart = t
            ready1.frameNStart = frameN  # exact frame index
            ready1.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if ready1.status == STARTED:
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