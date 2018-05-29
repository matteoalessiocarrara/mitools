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

# This script is used to create csv data from "Mi Band Master" android app database

import sqlite3
import time
import os
from sys import stdout, stderr, argv


class Table:
	def _filename(self, table):
		return table
		
	def _process(self, data):
		return data
		
	def exp(self, sel, table):
		of = open("%s/%s.csv" %(EXPDIR, self._filename(table)), "w")
		c.execute("SELECT %s FROM %s" % (sel, table))
		for row in self._process(c.fetchall()):
			for i in range(len(row)):
				col = str(row[i])
				out = col + ", " if i != (len(row) - 1) else col + "\n"
				of.write(out)
		of.close()
		
class Sleep(Table):
	def _filename(self, table):
		return "sleepcurve"
		
	def _process(self, data):
		newdata = []
		for row in data:
			newdata.append([row[0]+7200, 1])
			newdata.append([row[1]+7200, 0])
		return newdata
		
class Sleep2(Table):
	def _filename(self, table):
		return "sleeptime"
		
	def _process(self, data):
		newdata = []
		for row in data:
			newdata.append(list(row)+[row[0]+row[1]])
		return newdata
		
class Heart(Table):
	def _process(self, data):
		newdata = []

		for row in data:
			tmp = list(row) # time, hr
			tmp[0] = tmp[0] + 7200 # fixing timezone
			newdata.append(tmp)

		return newdata
	





# CREATE TABLE `heartrate` (`time` integer primary key,`hr` integer);
Heart().exp("time, hr", "heartrate")

# CREATE TABLE `sleep` (`id` integer primary key,`start_time` integer,`end_time` 
# integer,`awake` integer,`deep` integer,`light` integer,`stages` text,`deleted` 
# integer,`manually` integer);
Sleep().exp("start_time, end_time", "sleep")
Sleep2().exp("deep, light", "sleep")

# CREATE TABLE `steps` (`time` integer primary key,`intensity` integer,`steps` 
# integer,`category` integer);
Table().exp("time, intensity, steps, category", "steps")


def export_table(tname):
	with open("%s/%s.csv" %(EXPDIR, tname), "w") as of:
		pass



dbname = argv[1]

db = sqlite3.connect(dbname)
c = db.cursor()

EXPDIR = str(time.time()) + "_exp"
os.mkdir(EXPDIR)

# db schema last updated 2018/06/14



# CREATE TABLE `heartrate` (`time` integer primary key,`hr` integer);
	c.execute("SELECT time, hr FROM heartrate")
	for row in self._process(c.fetchall()):


		for i in range(len(row)):
			col = str(row[i])
			out = col + ", " if i != (len(row) - 1) else col + "\n"
			of.write(out)





