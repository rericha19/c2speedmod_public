# What is it
It is a small Crash 2 romhack that allows you to play at various player speeds and scales in several modes, including:
- custom (control speed and scale any time, separately)
- random each level or warp room
- random each fruit
- random each crate
- random each item
- randomly changing periodically/aperiodically
- random each spin

**It is based on pal crash 2 and you need to have the Crash 2 pal rom already, what's being released is just a patch.**

# How to use
You can apply an xdelta patch using a program called DeltaPatcher (https://github.com/marco-calautti/DeltaPatcher/releases).
The original file is the European (PAL) release of Crash 2 (.bin). 
If you want to make sure you are using the same original file, you can do it using certutil (Win11).
```
PS C:\...stuff> certutil -hashfile "Crash Bandicoot 2 - Cortex Strikes Back (Europe).bin" sha256
SHA256 hash of Crash Bandicoot 2 - Cortex Strikes Back (Europe).bin:
363ef6e65479ee6fc67cbc285262ff697356ab58b5ca5765c82258666650cf8b
```
sha256 after patch (v1): `63f2e859d3a08398229a8ce0bed9a454c86206f9e363919e5338b67837fe6b39` 

# Info
The files used to create the object responsible for player scale/change, as well as documentation can be found in **/misc**.
These include minor things - script used to determine available object type to be occupied by the object for example,
but the most interesting are following files found in **misc/gooc**:
- **notes.txt** - file detailing the solution (e.g. changes made in willc/exe and differences between levels)
- **goocLSe2C.gooc** and **SModC.gooc** - source files for the title screen and the actual player object manipulator
- **smod_util.gooc** - utility file that defines constants, generic subs and subs for setting/getting values
- **goolstdlib(2).gooc** - version of standard gool library used with previous files
- **comp.bat** - batch file used to compile output GOOL nsentry files that are used in levels, uses mandude's gooc compiler
