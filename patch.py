import os
import sys
import re
import hashlib
import json
from getpass import getpass
from colorama import Fore, Style, init

init(autoreset=True)

if len(sys.argv) != 2:
	print('Error: No input rom given')
	exit()
	
with open('patch_db.json', 'r') as file:
	db = json.loads(file.read())
	file.close()
	
start_pattern = b'\xD0\x88\x8D\x83\x42'
end_pattern = b'\\x24\x10\x49\x10\x68'

rom_file = open(sys.argv[1], "r+b")
rom_data = rom_file.read()
	
hasher = hashlib.md5()
hasher.update(rom_data)
hash = hasher.hexdigest()

print('Hash: ' + hash)

if db.get(hash):
	print('Patch mode: ', Fore.GREEN + Style.BRIGHT + 'Precise' + Style.RESET_ALL + ' [' + db[hash][0] + ']')
else:
	print('Patch mode: ' + Fore.YELLOW + Style.BRIGHT + 'Generic')

offset_start = re.search(start_pattern, rom_data)
if offset_start:
	offset_start = offset_start.end()
	print("Start offset: 0x%X" % offset_start)
else:
	sys.stderr.write("Couldn't find start offset")
	exit()
	
offset_end = re.search(end_pattern, rom_data)
if offset_end:
	offset_end = offset_end.start()
	print("End offset: 0x%X" % offset_end)
else:
	sys.stderr.write("Couldn't find end offset")
	exit()
	
length = offset_end - offset_start
print("Length to replace: %d" % length)
	
print()
sys.stdout.write('Zeroing it... ')
rom_file.seek(offset_start)
rom_file.write(b'\0' * length)
print('Done.')

print()
hasher = hashlib.md5()
rom_file.seek(0)
rom_data = rom_file.read()
hasher.update(rom_data)
hash_done = hasher.hexdigest()
sys.stdout.write('Final hash: ' + hash_done)

if db.get(hash):
	if db[hash][1] == hash_done:
		print(Fore.GREEN + Style.BRIGHT + ' [MATCH]')
	else:
		print(Fore.RED + Style.BRIGHT + ' [MISMATCH]')
	
print()	
file.close()
getpass("Press enter to quit...")