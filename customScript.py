#! /usr/bin/python
import os

if __name__ == "__main__":

	DELAY_15_r2= "scripts/myScripts/queueDelay15-r2"
	DELAY_10_r2= "scripts/myScripts/queueDelay10-r2"
	DELAY_15_r4= "scripts/myScripts/queueDelay15-r4"
	DELAY_10_r4= "scripts/myScripts/queueDelay10-r4"
	DELAY_15_r6= "scripts/myScripts/queueDelay15-r6"
	DELAY_10_r6= "scripts/myScripts/queueDelay10-r6"

	TEST = "scripts/test"

	print("Start .........................................")
	os.system("mkdir logs")
	os.system("mkdir results")


	############################


	os.system(DELAY_15_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/queueDelay15_log_r2 DELAY_15_r2> results/queueDelay15-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/queueDelay15_log_r2> results/queueDelay15-delay-r2.html")

	os.system(DELAY_10_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/queueDelay10_log_r2 DELAY_10_r2> results/queueDelay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/queueDelay10_log_r2> results/queueDelay10-delay-r2.html")

	os.system(DELAY_15_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/queueDelay15_log_r4 DELAY_15_r4> results/queueDelay15-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/queueDelay15_log_r4> results/queueDelay15-delay-r4.html")

	os.system(DELAY_10_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/queueDelay10_log_r4 DELAY_10_r4> results/queueDelay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/queueDelay10_log_r4> results/queueDelay10-delay-r4.html")


	os.system(DELAY_15_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/queueDelay15_log_r6 DELAY_15_r6> results/queueDelay15-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/queueDelay15_log_r6> results/queueDelay15-delay-r6.html")

	os.system(DELAY_10_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/queueDelay10_log_r6 DELAY_10_r6> results/queueDelay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/queueDelay10_log_r6> results/queueDelay10-delay-r6.html")



