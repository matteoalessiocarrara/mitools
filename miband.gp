set datafile separator ','

set style line 1 linewidth 2 linecolor rgb "red"
set style line 2 linewidth 2 linecolor rgb "green"
set xtics border 3600 rotate # 1h tics

set xdata time
set timefmt "%s" # unix timestamp
set format x "%Y-%m-%d %H:%M"

set ytics nomirror
set y2tics
set y2range [0:2] # binary states axis


DATA_DIR=ARG1

system("ls ".DATA_DIR." | diff - DATA_FILES > /dev/null")  
if(GPVAL_SYSTEM_ERRNO != 0) {
	print "Invalid data directory: ".DATA_DIR
	print "ERRNO=".GPVAL_SYSTEM_ERRNO
	quit
	}
print "Data dir is correct. Files match."

HEART_SAMPLES=system("wc -l ".DATA_DIR."/heartrate.csv | cut -d ' ' -f1")
print "heart smaples=".HEART_SAMPLES

set samples HEART_SAMPLES


plot DATA_DIR."/heartrate.csv" using 1:2 with impulses lc "blue",\
     DATA_DIR."/heartrate.csv" using 1:2 smooth bezier ls 1,\
     DATA_DIR."/sleepcurve.csv" using 1:2 with fsteps axes x1y2 ls 2

pause -1

