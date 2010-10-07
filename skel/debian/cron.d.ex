#
# Regular cron jobs for the skel package
#
0 4	* * *	root	[ -x /usr/bin/skel_maintenance ] && /usr/bin/skel_maintenance
