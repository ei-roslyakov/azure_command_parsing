import sys
import textfsm

template = sys.argv[1]
raw_text_data = sys.argv[2]

re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

# print(', '.join(re_table.header))

for row in data:
    print(row)
