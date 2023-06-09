# What is it
It is a small Crash 2 romhack that allows you to play at various player speeds and scales in several modes, including:
- custom (control speed and scale any time, separately)
- random each level or warp room
- random each fruit, crate and/or
- randomly changing periodically/aperiodically
- random each spin

**It is based on pal crash 2 and you need to have the Crash 2 pal rom already, what's being shared is just a delta patch.**

# Video
https://youtu.be/KAK_-GjRT0g

# How to use it and play 
The releases consist of delta files that are to be applied to the original Crash 2 PAL (european) release (.bin file).

## Online romhacking.com patch method
You can apply a patch using the https://www.romhacking.net/patch/ site.   
Original ROM file checksums:   
CRC32:  f5e2ec49   
MD5:    10dabebd6a3efc1e1e9db4f8f3b864cb   
SHA-1:  b077862d2c6e1b8060c2eae2fe82e708b228de7c   

## DeltaPatcher method (alternative, offline)
You can apply a patch (e.g. **c2pal_speedmod_v1.xdelta**) using a program called DeltaPatcher (https://github.com/marco-calautti/DeltaPatcher/releases).
**Warning: overwrites the original file. IF IT DOES NOT WORK, DISABLE CHECKSUM VALIDATION IN DELTAPATCHER OPTIONS**
It is recommended to make sure you are using the same original file, on Win10 you can do it using **certutil**.

```
PS C:\...stuff> certutil -hashfile "Crash Bandicoot 2 - Cortex Strikes Back (Europe).bin" sha256
SHA256 hash of Crash Bandicoot 2 - Cortex Strikes Back (Europe).bin:
363ef6e65479ee6fc67cbc285262ff697356ab58b5ca5765c82258666650cf8b
```
sha256 after patch (v1): `63f2e859d3a08398229a8ce0bed9a454c86206f9e363919e5338b67837fe6b39` 

sha256 after patch (v2): `ea8cb5f5390d13868bc74062e1a69f6f8871dfec966125b9ad3f86038f0f0820`


# Info
The files used to create the object responsible for player scale/change, as well as documentation can be found in **/misc**.
These include minor things - script used to determine available object type to be occupied by the object for example,
but the most interesting are following files found in **misc/gooc**:
- **notes.txt** - file detailing the solution (e.g. changes made in willc/exe and differences between levels)
- **goocLSe2C.gooc** and **SModC.gooc** - source files for the title screen and the actual player object manipulator
- **smod_util.gooc** - utility file that defines constants, generic subs and subs for setting/getting values
- **goolstdlib(2).gooc** - version of standard gool library by gooc files
- **comp.bat** - batch file used to compile output GOOL nsentry files that are used in actual levels, 
               - uses mandude's gooc compiler, outputs several versions used by levels with special behavior (bear, hangrail etc)

# Changelog
v2 - warp room uses L2 instead of circle to toggle between range types

# How to make changes and experiment
In order to update the player modifier object in a level, you need to replace the level's SModC entry using CrashEdit or Dr.NSF.
Each level has its own copy of SModC, therefore in order to apply the change to the entire game you need to replace it in every NSF file separately.
To compile SModC, use gooc or the batch file (both CLI only). For more info about gooc see https://github.com/ManDude/goocdump .

If you have any questions or suggestions, feel free to create an issue.
