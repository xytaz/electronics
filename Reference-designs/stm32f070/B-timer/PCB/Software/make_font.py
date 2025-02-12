
symbols = [[
# 0
1,1,1,
1,0,1,
1,0,1,
1,0,1,
1,1,1,
],[
# 1
0,1,0,
1,1,0,
0,1,0,
0,1,0,
1,1,1,
],[
# 2
1,1,1,
0,0,1,
1,1,1,
1,0,0,
1,1,1,
],[
# 3
1,1,1,
0,0,1,
1,1,1,
0,0,1,
1,1,1,
],[
# 4
1,0,1,
1,0,1,
1,1,1,
0,0,1,
0,0,1,
],[
# 5
1,1,1,
1,0,0,
1,1,1,
0,0,1,
1,1,1,
],[
# 6
1,1,1,
1,0,0,
1,1,1,
1,0,1,
1,1,1,
],[
# 7
1,1,1,
0,0,1,
0,0,1,
0,1,0,
0,1,0,
],[
# 8
1,1,1,
1,0,1,
1,1,1,
1,0,1,
1,1,1,
],[
# 9
1,1,1,
1,0,1,
1,1,1,
0,0,1,
1,1,1,
],[
# : = 10
0,0,0,
0,1,0,
0,0,0,
0,1,0,
0,0,0,
]]

byte = 0
rows = 5
cols = 3

txt = '''#include <avr/pgmspace.h>

const static uint16_t __attribute__ ((progmem)) symbols[] = {
'''

for c in range(len(symbols)):
  word = 0
  symbols[c][00:03] = symbols[c][00:03][::-1]
  symbols[c][03:06] = symbols[c][03:06][::-1]
  symbols[c][06: 9] = symbols[c][06: 9][::-1]
  symbols[c][ 9:12] = symbols[c][ 9:12][::-1]
  symbols[c][12:15] = symbols[c][12:15][::-1]
  for b in range(rows*cols):
    word |= (symbols[c][b]<<b)
  txt += hex(word)+", "
txt = txt[:-2]

txt += '''
};
'''

with open("font.h", "w") as f:
    f.write(txt)

print("Needs "+str(2*len(symbols))+" bytes of space")

