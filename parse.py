import sys
import textfsm
from tabulate import tabulate

template = sys.argv[1]
input_file = sys.argv[2]

f = open(template)
output = open(input_file).read()

re_table = textfsm.TextFSM(f)

header = re_table.header
result = re_table.ParseText(output)

print(tabulate(result, headers=header))
