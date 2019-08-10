import os
import sys
current_script = os.path.realpath(__file__)
src_path = os.path.join(os.path.split(current_script)[0], "../src/")
src_path = os.path.realpath(src_path)
sys.path.append(src_path)
