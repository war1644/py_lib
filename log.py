#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import time
import json
import types


class Log(object):

    @staticmethod
    def info(content):
        Log.add(content, 'info.txt')

    @staticmethod
    def error(content):
        Log.add(content, 'error.txt')

    @staticmethod
    def warn(content):
        Log.add(content, 'warn.txt')

    @staticmethod
    def checkDir():
        logDir = os.path.join(os.getcwd(), "logs")
        dateDir = time.strftime("%Y%m%d", time.localtime())
        logDir = os.path.join(logDir, dateDir)
        haveDir = os.path.exists(logDir)
        if not haveDir:
            os.makedirs(logDir)
        return logDir

    @staticmethod
    def add(content, fileName='log.txt'):
        try:
            logDir = Log.checkDir()
            curTime = time.strftime("%H:%M:%S", time.localtime())
            fileName = os.path.join(logDir, fileName)
            content
            f = open(fileName, 'a')
            if type(content) != str:
                content = json.dumps(content)
            f.write('Time: '+curTime+'\nData: '+content+'\n\n')
            f.close()
            return True
        except Exception as err:
            print(1, err)
