#! /usr/bin/python
import os

if __name__ == "__main__":

	DELAY_15_r2= "scripts/myScripts/queueDelay15-r2"
	DELAY_10_r2= "scripts/myScripts/queueDelay10-r2"
	DELAY_15_r4= "scripts/myScripts/queueDelay15-r4"
	DELAY_10_r4= "scripts/myScripts/queueDelay10-r4"
	DELAY_15_r6= "scripts/myScripts/queueDelay15-r6"
	DELAY_10_r6= "scripts/myScripts/queueDelay10-r6"
	
	THROUGHPUT_1_r2= "scripts/myScripts/throughput1delay10-r2"
	THROUGHPUT_1_r4= "scripts/myScripts/throughput1delay10-r4"
	THROUGHPUT_1_r6= "scripts/myScripts/throughput1delay10-r6"
	
	THROUGHPUT_2_r2= "scripts/myScripts/throughput2delay10-r2"
	THROUGHPUT_2_r4= "scripts/myScripts/throughput2delay10-r4"
	THROUGHPUT_2_r6= "scripts/myScripts/throughput2delay10-r6"

	THROUGHPUT_3_r2= "scripts/myScripts/throughput3delay10-r2"
	THROUGHPUT_3_r4= "scripts/myScripts/throughput3delay10-r4"
	THROUGHPUT_3_r6= "scripts/myScripts/throughput3delay10-r6"

	THROUGHPUT_4_r2= "scripts/myScripts/throughput4delay10-r2"
	THROUGHPUT_4_r4= "scripts/myScripts/throughput4delay10-r4"
	THROUGHPUT_4_r6= "scripts/myScripts/throughput4delay10-r6"

	THROUGHPUT_5_r2= "scripts/myScripts/throughput5delay10-r2"
	THROUGHPUT_5_r4= "scripts/myScripts/throughput5delay10-r4"
	THROUGHPUT_5_r6= "scripts/myScripts/throughput5delay10-r6"

	THROUGHPUT_6_r2= "scripts/myScripts/throughput6delay10-r2"
	THROUGHPUT_6_r4= "scripts/myScripts/throughput6delay10-r4"
	THROUGHPUT_6_r6= "scripts/myScripts/throughput6delay10-r6"

	THROUGHPUT_7_r2= "scripts/myScripts/throughput7delay10-r2"
	THROUGHPUT_7_r4= "scripts/myScripts/throughput7delay10-r4"
	THROUGHPUT_7_r6= "scripts/myScripts/throughput7delay10-r6"

	THROUGHPUT_8_r2= "scripts/myScripts/throughput8delay10-r2"
	THROUGHPUT_8_r4= "scripts/myScripts/throughput8delay10-r4"
	THROUGHPUT_8_r6= "scripts/myScripts/throughput8delay10-r6"

	THROUGHPUT_9_r2= "scripts/myScripts/throughput9delay10-r2"
	THROUGHPUT_9_r4= "scripts/myScripts/throughput9delay10-r4"
	THROUGHPUT_9_r6= "scripts/myScripts/throughput9delay10-r6"

	THROUGHPUT_10_r2= "scripts/myScripts/throughput10delay10-r2"
	THROUGHPUT_10_r4= "scripts/myScripts/throughput10delay10-r4"
	THROUGHPUT_10_r6= "scripts/myScripts/throughput10delay10-r6"

	THROUGHPUT_11_r2= "scripts/myScripts/throughput11delay10-r2"
	THROUGHPUT_11_r4= "scripts/myScripts/throughput11delay10-r4"
	THROUGHPUT_11_r6= "scripts/myScripts/throughput11delay10-r6"

	THROUGHPUT_12_r2= "scripts/myScripts/throughput12delay10-r2"
	THROUGHPUT_12_r4= "scripts/myScripts/throughput12delay10-r4"
	THROUGHPUT_12_r6= "scripts/myScripts/throughput12delay10-r6"

	THROUGHPUT_13_r2= "scripts/myScripts/throughput13delay10-r2"
	THROUGHPUT_13_r4= "scripts/myScripts/throughput13delay10-r4"
	THROUGHPUT_13_r6= "scripts/myScripts/throughput13delay10-r6"

	THROUGHPUT_14_r2= "scripts/myScripts/throughput14delay10-r2"
	THROUGHPUT_14_r4= "scripts/myScripts/throughput14delay10-r4"
	THROUGHPUT_14_r6= "scripts/myScripts/throughput14delay10-r6"

	THROUGHPUT_15_r2= "scripts/myScripts/throughput15delay10-r2"
	THROUGHPUT_15_r4= "scripts/myScripts/throughput15delay10-r4"
	THROUGHPUT_15_r6= "scripts/myScripts/throughput15delay10-r6"

	THROUGHPUT_31_r2= "scripts/myScripts/throughput31delay10-r2"
	THROUGHPUT_31_r4= "scripts/myScripts/throughput31delay10-r4"
	THROUGHPUT_31_r6= "scripts/myScripts/throughput31delay10-r6"


	TEST = "scripts/test"

	print("Start .........................................")
	os.system("mkdir logs")
	os.system("mkdir results")


	############################


	# Throughput 1 delay 10 

	os.system(THROUGHPUT_1_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput1Delay10_log_r2 THROUGHPUT_1_r2> results/throughput1Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput1Delay10_log_r2> results/throughput1Delay10-delay-r2.html")

	os.system(THROUGHPUT_1_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput1Delay10_log_r4 THROUGHPUT_1_r4> results/throughput1Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput1Delay10_log_r4> results/throughput1Delay10-delay-r4.html")

	os.system(THROUGHPUT_1_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput1Delay10_log_r6 THROUGHPUT_1_r6> results/throughput1Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput1Delay10_log_r6> results/throughput1Delay10-delay-r6.html")

	# Throughput 2.0 delay 10

	os.system(THROUGHPUT_2_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput2Delay10_log_r2 THROUGHPUT_2_r2> results/throughput2Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput2Delay10_log_r2> results/throughput2Delay10-delay-r2.html")

	os.system(THROUGHPUT_2_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput2Delay10_log_r4 THROUGHPUT_2_r4> results/throughput2Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput2Delay10_log_r4> results/throughput2Delay10-delay-r4.html")

	os.system(THROUGHPUT_2_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput2Delay10_log_r6 THROUGHPUT_2_r6> results/throughput2Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput2Delay10_log_r6> results/throughput2Delay10-delay-r6.html")	


	# Throughput 3 delay 10

	os.system(THROUGHPUT_3_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput3Delay10_log_r2 THROUGHPUT_3_r2> results/throughput3Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput3Delay10_log_r2> results/throughput3Delay10-delay-r2.html")

	os.system(THROUGHPUT_3_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput3Delay10_log_r4 THROUGHPUT_3_r4> results/throughput3Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput3Delay10_log_r4> results/throughput3Delay10-delay-r4.html")

	os.system(THROUGHPUT_3_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput3Delay10_log_r6 THROUGHPUT_3_r6> results/throughput3Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput3Delay10_log_r6> results/throughput3Delay10-delay-r6.html")	

	# Throughput 4 delay 10

	os.system(THROUGHPUT_4_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput4Delay10_log_r2 THROUGHPUT_4_r2> results/throughput4Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput4Delay10_log_r2> results/throughput4Delay10-delay-r2.html")

	os.system(THROUGHPUT_4_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput4Delay10_log_r4 THROUGHPUT_4_r4> results/throughput4Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput4Delay10_log_r4> results/throughput4Delay10-delay-r4.html")

	os.system(THROUGHPUT_4_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput4Delay10_log_r6 THROUGHPUT_4_r6> results/throughput4Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput4Delay10_log_r6> results/throughput4Delay10-delay-r6.html")	

	# Throughput 5 delay 10

	os.system(THROUGHPUT_5_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput5Delay10_log_r2 THROUGHPUT_5_r2> results/throughput5Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput5Delay10_log_r2> results/throughput5Delay10-delay-r2.html")

	os.system(THROUGHPUT_5_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput5Delay10_log_r4 THROUGHPUT_5_r4> results/throughput5Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput5Delay10_log_r4> results/throughput5Delay10-delay-r4.html")

	os.system(THROUGHPUT_5_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput5Delay10_log_r6 THROUGHPUT_5_r6> results/throughput5Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput5Delay10_log_r6> results/throughput5Delay10-delay-r6.html")	

	# Throughput 6 delay 10

	os.system(THROUGHPUT_6_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput6Delay10_log_r2 THROUGHPUT_6_r2> results/throughput6Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput6Delay10_log_r2> results/throughput6Delay10-delay-r2.html")

	os.system(THROUGHPUT_6_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput6Delay10_log_r4 THROUGHPUT_6_r4> results/throughput6Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput6Delay10_log_r4> results/throughput6Delay10-delay-r4.html")

	os.system(THROUGHPUT_6_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput6Delay10_log_r6 THROUGHPUT_6_r6> results/throughput6Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput6Delay10_log_r6> results/throughput6Delay10-delay-r6.html")	

	# Throughput 7 delay 10

	os.system(THROUGHPUT_7_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput7Delay10_log_r2 THROUGHPUT_7_r2> results/throughput7Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput7Delay10_log_r2> results/throughput7Delay10-delay-r2.html")

	os.system(THROUGHPUT_7_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput7Delay10_log_r4 THROUGHPUT_7_r4> results/throughput7Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput7Delay10_log_r4> results/throughput7Delay10-delay-r4.html")

	os.system(THROUGHPUT_7_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput7Delay10_log_r6 THROUGHPUT_7_r6> results/throughput7Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput7Delay10_log_r6> results/throughput7Delay10-delay-r6.html")	

	# Throughput 8 delay 10

	os.system(THROUGHPUT_8_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput8Delay10_log_r2 THROUGHPUT_8_r2> results/throughput8Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput8Delay10_log_r2> results/throughput8Delay10-delay-r2.html")

	os.system(THROUGHPUT_8_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput8Delay10_log_r4 THROUGHPUT_8_r4> results/throughput8Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput8Delay10_log_r4> results/throughput8Delay10-delay-r4.html")

	os.system(THROUGHPUT_8_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput8Delay10_log_r6 THROUGHPUT_8_r6> results/throughput8Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput8Delay10_log_r6> results/throughput8Delay10-delay-r6.html")	

	# Throughput 9 delay 10

	os.system(THROUGHPUT_9_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput9Delay10_log_r2 THROUGHPUT_9_r2> results/throughput9Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput9Delay10_log_r2> results/throughput9Delay10-delay-r2.html")

	os.system(THROUGHPUT_9_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput9Delay10_log_r4 THROUGHPUT_9_r4> results/throughput9Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput9Delay10_log_r4> results/throughput9Delay10-delay-r4.html")

	os.system(THROUGHPUT_9_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput9Delay10_log_r6 THROUGHPUT_9_r6> results/throughput9Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput9Delay10_log_r6> results/throughput9Delay10-delay-r6.html")	

	# Throughput 10 delay 10

	os.system(THROUGHPUT_10_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput10Delay10_log_r2 THROUGHPUT_10_r2> results/throughput10Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput10Delay10_log_r2> results/throughput10Delay10-delay-r2.html")

	os.system(THROUGHPUT_10_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput10Delay10_log_r4 THROUGHPUT_10_r4> results/throughput10Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput10Delay10_log_r4> results/throughput10Delay10-delay-r4.html")

	os.system(THROUGHPUT_10_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput10Delay10_log_r6 THROUGHPUT_10_r6> results/throughput10Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput10Delay10_log_r6> results/throughput10Delay10-delay-r6.html")	

	# Throughput 11 delay 10

	os.system(THROUGHPUT_11_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput11Delay10_log_r2 THROUGHPUT_11_r2> results/throughput11Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput11Delay10_log_r2> results/throughput11Delay10-delay-r2.html")

	os.system(THROUGHPUT_11_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput11Delay10_log_r4 THROUGHPUT_11_r4> results/throughput11Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput11Delay10_log_r4> results/throughput11Delay10-delay-r4.html")

	os.system(THROUGHPUT_11_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput11Delay10_log_r6 THROUGHPUT_11_r6> results/throughput11Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput11Delay10_log_r6> results/throughput11Delay10-delay-r6.html")	

	# Throughput 12 delay 10

	os.system(THROUGHPUT_12_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput12Delay10_log_r2 THROUGHPUT_12_r2> results/throughput12Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput12Delay10_log_r2> results/throughput12Delay10-delay-r2.html")

	os.system(THROUGHPUT_12_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput12Delay10_log_r4 THROUGHPUT_12_r4> results/throughput12Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput12Delay10_log_r4> results/throughput12Delay10-delay-r4.html")

	os.system(THROUGHPUT_12_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput12Delay10_log_r6 THROUGHPUT_12_r6> results/throughput12Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput12Delay10_log_r6> results/throughput12Delay10-delay-r6.html")	

	# Throughput 13 delay 10

	os.system(THROUGHPUT_13_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput13Delay10_log_r2 THROUGHPUT_13_r2> results/throughput13Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput13Delay10_log_r2> results/throughput13Delay10-delay-r2.html")

	os.system(THROUGHPUT_13_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput13Delay10_log_r4 THROUGHPUT_13_r4> results/throughput13Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput13Delay10_log_r4> results/throughput13Delay10-delay-r4.html")

	os.system(THROUGHPUT_13_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput13Delay10_log_r6 THROUGHPUT_13_r6> results/throughput13Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput13Delay10_log_r6> results/throughput13Delay10-delay-r6.html")	

	# Throughput 14 delay 10

	os.system(THROUGHPUT_14_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput14Delay10_log_r2 THROUGHPUT_14_r2> results/throughput14Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput14Delay10_log_r2> results/throughput14Delay10-delay-r2.html")

	os.system(THROUGHPUT_14_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput14Delay10_log_r4 THROUGHPUT_14_r4> results/throughput14Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput14Delay10_log_r4> results/throughput14Delay10-delay-r4.html")

	os.system(THROUGHPUT_14_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput14Delay10_log_r6 THROUGHPUT_14_r6> results/throughput14Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput14Delay10_log_r6> results/throughput14Delay10-delay-r6.html")
	
	# Throughput 15 delay 10

	os.system(THROUGHPUT_15_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput15Delay10_log_r2 THROUGHPUT_15_r2> results/throughput15Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput15Delay10_log_r2> results/throughput15Delay10-delay-r2.html")

	os.system(THROUGHPUT_15_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput15Delay10_log_r4 THROUGHPUT_15_r4> results/throughput15Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput15Delay10_log_r4> results/throughput15Delay10-delay-r4.html")

	os.system(THROUGHPUT_15_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput15Delay10_log_r6 THROUGHPUT_15_r6> results/throughput15Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput15Delay10_log_r6> results/throughput15Delay10-delay-r6.html")	

	# Throughput 31 delay 10

	os.system(THROUGHPUT_31_r2)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput31Delay10_log_r2 THROUGHPUT_31_r2> results/throughput31Delay10-throughput-r2.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput31Delay10_log_r2> results/throughput31Delay10-delay-r2.html")

	os.system(THROUGHPUT_31_r4)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput31Delay10_log_r4 THROUGHPUT_31_r4> results/throughput31Delay10-throughput-r4.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput31Delay10_log_r4> results/throughput31Delay10-delay-r4.html")

	os.system(THROUGHPUT_31_r6)
	os.system("./plot_scripts/mm-throughput-graph 500 ./logs/throughput31Delay10_log_r6 THROUGHPUT_31_r6> results/throughput31Delay10-throughput-r6.html")
	os.system("./plot_scripts/mm-delay-graph ./logs/throughput31Delay10_log_r6> results/throughput31Delay10-delay-r6.html")	


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



