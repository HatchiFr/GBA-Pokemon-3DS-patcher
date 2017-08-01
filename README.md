# GBA Pokemon 3DS Patcher
A little utility to patch GBA roms for 3DS.

## Dependencies
 * Python 3
 * [Colorama](https://pypi.python.org/pypi/colorama) (Install it using `pip install colorama`)

## Usage
Call it from a command line using `patch.py <rom.gba>` or `python patch.py <rom.gba>` with the rom in the same folder.  
If the ROM is known from the database (located at the root), it will perform a check of hash before and after patching.  
**WARNING : This tool overwrites the original ROM without warning**

This tool will use "Precise" patching if your ROM is known in the databse, or "Generic" if it's not. Precise only check your hash to check that the patching was done properly.

If you have some ROM which is unknown by the patcher, feel free to fill a PR with the updated database or drop me an issue with the hash of your ROM before and after the patching, and the full name of it.

## FAQ
*What does it do ?*  
It fixes a GBA rom to be used with AGB_FIRM of the 3DS.

*Everybody already has the CIA VC of these ROMs*  
Probably. My next job requires me to learn Python, so I took cinq minutes to create this to train myself. I made it open-source so if someone ever requires it, it'll be there.

*Why would I use this instead of AmeenX's patching method ?*
Hex-editing is not convenient for everyone. This is a pretty simple way of patching it. As I've said, you don't need to use it, it was just a little training.

*Why is your code so messy ?*
It's my first Python project. I am a SysAdmin, not a developper, I just code few things when I need/want to. I'll be happy to answer any PR and/or discuss with you if you have some constructive feedback about how my code quality should be improved.

## Credits
 - AmeenX : Original [patching method](https://gbatemp.net/threads/fixes-for-all-gba-pokemons-save-issue-with-agb_firm.390508/)
 - Hakujou : Patcher