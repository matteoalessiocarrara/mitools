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

import time, os
from sys import argv
from sqlite2csv import sqlite2csv


# db schema last updated 2018/06/14

# CREATE TABLE `heartrate` (`time` integer primary key,`hr` integer);

# CREATE TABLE `sleep` (`id` integer primary key,`start_time` integer,`end_time`
# integer,`awake` integer,`deep` integer,`light` integer,`stages` text,`deleted`
# integer,`manually` integer);

# CREATE TABLE `steps` (`time` integer primary key,`intensity` integer,`steps`
# integer,`category` integer);


# what to export from the database
# tuple: (tablename, columns)
tables =[
            ("heartrate", "time, hr"),
            ("sleep", "start_time, end_time, deep, light"),
            ("steps", "time, intensity, steps, category")
        ]

dbname = argv[1]
EXPDIR = str(time.time()) + "_exp"
os.mkdir(EXPDIR)
exporter = sqlite2csv.Exporter(dbname, EXPDIR)

for t in tables:
	exporter.run(t[0], t[1])




