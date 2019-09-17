#! /usr/bin/python
import os


INPUT_DIR = "input"
OUTPUT_DIR = "output"


def main():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for input_filename in os.listdir(INPUT_DIR):
        output_filename = "%s.out" % input_filename
        print("Converting %s to inter-arrival times and saving as %s..." % (input_filename, output_filename))
        with open("%s/%s" % (INPUT_DIR, input_filename), 'r') as infile, open("%s/%s" % (OUTPUT_DIR, output_filename), 'w+') as outfile:
            previous_pkts = 0
            start_time = None
            for line in infile:
                values = [s for s in line.split()]
                if values[1] == '7.0.0.2' or values[1] == '1.0.0.2':
                    pkts_to_send = int(values[4]) - previous_pkts
                    time = int(round(float(values[0]) * 1000))
                    previous_pkts = int(values[4])
                    for pkts in range(pkts_to_send):
                        if start_time == None:
                            start_time = time
                        output = time - start_time
                        outfile.write("%d\n" % output)

if __name__ == '__main__':
    main()
