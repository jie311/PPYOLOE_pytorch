#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os

from ppyoloe.exp import ExpE as MyExp

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.depth = 1.33
        self.width = 1.25
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]

        self.basic_lr_per_img = 0.02 / 64.0