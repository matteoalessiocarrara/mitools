#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2018 Matteo Alessio Carrara <sw.matteoac@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# processing of the raw csv

import csv, os, datetime
from sys import argv


class Raw:
    def __init__(self, fname):
        self._fname = "/" + fname
    
    
    def _custom_proc(self, inrow):
        return inrow
    

    # TODO Fix timezone
    def _time_converter(self, timestamp):
        return str(datetime.datetime.utcfromtimestamp(float(timestamp)).strftime('%Y-%m-%d %H:%M:%S'))


    def proc(self):
        with open(datadir + self._fname, "r") as inf:
            with open(procdir + self._fname, "w") as outf:
                outcsv = csv.writer(outf)
                header = True
                for inrow in csv.reader(inf):
                    if header:
                        header = False
                        outcsv.writerow(inrow)
                    else:
                        outcsv.writerow(self._custom_proc(inrow))


class Hr(Raw):
    def _custom_proc(self, inrow):
        return [self._time_converter(inrow[0]), inrow[1]]


class Sleep(Raw):
    def _custom_proc(self, inrow):
        t1 = self._time_converter(inrow[0])
        t2 = self._time_converter(inrow[1])
        return [t1, t2] + inrow[2:]


class Steps(Raw):
    def _custom_proc(self, inrow):
        return [self._time_converter(inrow[0])] + inrow[1:]


datadir = argv[1] + "/"
procdir = datadir + "/processed/"
os.mkdir(procdir)

Hr("heartrate.csv").proc()
Sleep("sleep.csv").proc()
Steps("steps.csv").proc()
