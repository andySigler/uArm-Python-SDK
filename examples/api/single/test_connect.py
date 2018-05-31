#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, UFactory, Inc.
# All rights reserved.
#
# Author: Vinman <vinman.wen@ufactory.cc> <vinman.cub@gmail.com>

import os
import sys
import time
import threading
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from uarm.wrapper import SwiftAPI
from uarm.utils.log import logger

"""
测试连接和断开的接口
"""

# logger.setLevel(logger.INFO)

# swift = SwiftAPI('COM9')
swift = SwiftAPI(filters={'hwid': 'USB VID:PID=2341:0042'})

while True:
    try:
        swift.connect()
        swift.disconnect()
        print('thread count:', len(threading.enumerate()), time.time())
    except:
        pass
