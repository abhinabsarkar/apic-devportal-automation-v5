import sys, time
from time import sleep

# sys.stdout.write("Processing: ")
# sys.stdout.flush()
# some_list = [0] * 100
# for idx, item in enumerate(some_list):
#     msg = "item %i of %i" % (idx, len(some_list)-1)
#     sys.stdout.write(msg + chr(8) * len(msg))
#     sys.stdout.flush()
#     sleep(0.02)

# sys.stdout.write("DONE" + " "*len(msg)+"\n")
# sys.stdout.flush()

def update_progress(job_title, progress):
    length = 20 # modify this to change the length
    block = int(round(length*progress))
    msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
    if progress >= 1: msg += " DONE\r\n"
    sys.stdout.write(msg)
    sys.stdout.flush()

# Test
for i in range(100):
    time.sleep(0.1)
    update_progress("Processing", i/100.0)
update_progress("Processing", 1)