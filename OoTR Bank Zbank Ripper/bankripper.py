#!/usr/bin/env python3

# Apr 2020 Isghj

# This script reads a modified Majora's Mask U0 (decompressed) rom 
#  and extracts the individual instrument sets from the audiobank
# along with the metadata from the audiobank index table (instrument count, percussion, other data)
#  this was created because Seq64 only extracts instrument sets as xml to include both as one file
#  and I hate XML parsing, just shove the binary, its easier

# more info MMR discord: https://discord.gg/8qbreUM

import binascii
import sys
import os
from time import strftime

# ref: https://docs.google.com/spreadsheets/d/1J-4OwmZzOKEv2hZ7wrygOpMm0YcRnephEo3Q2FooF6E/edit#gid=56702767
#audiobank_table_loc = 0xc776c0 // mm
#audiobank_loc       = 0x20700
#audiobank_table_len = 0x2a0     # currently seq64 cannot increase this, assume vanilla size
audiobank_table_loc = 0xB896A0
audiobank_loc       = 0xD390
audiobank_table_len = 0x270     # currently seq64 cannot increase this, assume vanilla size

if len(sys.argv) < 2:
  print("usage: python3 mm_bankripper.py decompressed_majoramask_USA.z64")
  sys.exit(1)

# load mm rom input
try:
  rom = open(sys.argv[1], "rb")
except FileNotFoundError:
  print("could not find file")

# make new folder with timestamp sorting
output_dir = strftime("%Y-%m-%d_%H%M")
if not os.path.exists(output_dir):
  os.makedirs(output_dir)
output_dir += "/"

# load mm audiobanktable
rom.seek(audiobank_table_loc)
audiobank_table = rom.read(audiobank_table_len )  

# debugging: check to make sure the table is in the right place
hexified_table_data = binascii.hexlify(audiobank_table)
if hexified_table_data[0:8] == b'00290000':
  print("Bank index found at regular location, extracting...")
else:
  print("WARNING: good chance the audiobank index table was moved to a different location")

# extract banks and meta
# starting with 16 because the first line is just 00 29 00 00 and 00 padding to the end of line
# I don't think that modifies anything else, don't see anything in the xml about it
bank_index = 0
audiobank_table_dmaspaced = [audiobank_table[i:i+16] for i in range(16, len(audiobank_table), 16)]
for dma in audiobank_table_dmaspaced:
  # four words(4x4 bytes): index address, length, and two words of metadata
  address  = int.from_bytes(dma[0:4], byteorder="big")
  length   = int.from_bytes(dma[4:8], byteorder="big")
#  if vanilla_bank_sizes[bank_index] != length:
  metadata = dma[8:16]
  bank_index_hex = hex(bank_index).lstrip("0x").zfill(2)
  file_name = output_dir + bank_index_hex
  print("Bank " + bank_index_hex + " is located at " + hex(audiobank_loc + address))
  print(" size: " + str(length))

  outfile = open(file_name + ".zbank", 'wb')
  rom.seek( audiobank_loc + address)
  outfile.write(rom.read(length))
  outfile.close()
  outfile = open(file_name + ".bankmeta", 'wb')
  outfile.write(metadata)
  outfile.close()
  bank_index += 1

print("Extraction complete in folder " + output_dir + ".")
