import time
import re

def process_problem(*args):
    tic = time.perf_counter()
    result = args[0](args)
    toc = time.perf_counter()
    txt = repr(args[0])
    pattern = "\\s"
    x = re.split(pattern, txt)
    print(f'{(toc-tic):0.4f}s {x[1]} = {result}')
