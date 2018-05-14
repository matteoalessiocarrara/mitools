#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Matteo Alessio Carrara <sw.matteoac@gmail.com>
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

import sqlite3
from sys import stdout


def exp(sel, table):
	print(sel)
	for row in c.execute("SELECT %s FROM %s" % (sel, table)):
		for col in row:
			col = str(col)
			out = col + "\n" if col == str(row[-1]) else col + ", "
			stdout.write(out)
	stdout.write("\n")
	

db = sqlite3.connect("miband")
c = db.cursor()

# CREATE TABLE `heartrate` (`time` integer primary key,`hr` integer);
exp("time, hr", "heartrate")

# CREATE TABLE `sleep` (`id` integer primary key,`start_time` integer,`end_time` 
# integer,`awake` integer,`deep` integer,`light` integer,`stages` text,`deleted` 
# integer,`manually` integer);
exp("start_time, end_time, awake, deep, light, stages", "sleep")

# CREATE TABLE `steps` (`time` integer primary key,`intensity` integer,`steps` 
# integer,`category` integer);
exp("time, intensity, steps, category", "steps")
