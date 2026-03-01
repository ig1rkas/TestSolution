import time
import tracemalloc
import builtins
from pprint import pprint

# if u need to work with google files
import os
from google.colab import drive
drive.mount('/content/drive', force_remount=True)
os.chdir('/content/drive/MyDrive/your/path')

class CreateTest:
    def __init__(self, taskNumber: int, inpData=[], ):
        if inpData:
            with open(f"input_task{taskNumber}", "w") as file:
                for string in inpData:
                    if string.__class__ == list:
                        file.write(" ".join(list(map(str, string))) + "\n")
                    else:
                        file.write(str(string) + "\n")
            print("Test created")
            return
        print("No data for write")


class TestSolution:
    def __init__(self, taskNumber: int):
        self.inpFile = open(f"input_task{taskNumber}", "r").readlines()
        self.outputFile = open(f"output_task{taskNumber}", "w")
        self.input_s_i = 0

    def input(self):
        self.input_s_i += 1
        return self.inpFile[self.input_s_i - 1].rstrip()

    def print(self, *args, end='\n'):
        if len(args) == 1:
            args = args[0]
            if args.__class__ in [int, float, bool]:
                args = str(args)
        else:
            args = " ".join(list(map(str, list(args))))
        self.outputFile.write(args + end)
        pprint(args)
        

    def testFunction(self, solution_func, checkMemory=True):
        original_print = builtins.print
        original_input = builtins.input
        builtins.print = self.print
        builtins.input = self.input
        
        
        if checkMemory:
            tracemalloc.start()
        time_start = time.perf_counter()
        
        solution_func()
        
        time_end = time.perf_counter()
        
        builtins.input = original_input
        builtins.print = original_print
        print(f"Time to solve: {round(time_end - time_start, 3)} sec")
        if checkMemory:
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics("lineno")
            total_size = sum(stat.size for stat in top_stats)
            print(f"Total allocated size: {round(total_size / 10**6, 3)} MB")
            tracemalloc.stop()
        
# test using
        
def solution(): # solution function
    n = int(input())
    for i in range(n):
        print(input()[::-1])

# create test
CreateTest(
    inpData=[
        2, 
        [2, 3],
        [2, 3]
    ],
    taskNumber=1
)
# check solution 
TestSolution(1).testFunction(solution_func=solution)
