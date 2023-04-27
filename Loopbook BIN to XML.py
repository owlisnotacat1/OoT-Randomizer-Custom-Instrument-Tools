
# this script turns a loopbook bin into xml data you can copy paste
#   into a Seq64 1.0 xml bank so you can make instruments with new samples

import sys
import struct # use use it to read our binary piece by piece

fin = open(sys.argv[1], 'rb')
fin_buffer = fin.read()
fout = open(sys.argv[1] + ".txt", 'w')

iter = 0
while iter < len(fin_buffer):
  # spacer every 8 elements
  #if (iter - 8) % 32 == 0:
    #fout.write("\n")

  number = struct.unpack(">h", fin_buffer[iter:iter+2]) # what I had before
  # upack adds extra symbols, remove now
  number = number[0]
  
  #print("thing: " + str(number))   
  fout.write('                <element datatype="int16" ispointer="0" value="' + str(number) + '"/>\n')

  iter += 2
