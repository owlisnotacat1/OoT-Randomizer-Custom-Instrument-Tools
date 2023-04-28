# Creating A Customm Instrument Bank

For This tutorial I will be using Seq64 V1 which can be found [here](https://github.com/sauraen/seq64/releases/tag/V1.0)

##Things you will learn how to do

*Make a custom instrument bank for OoTR
*make a custom instrument sample for OoTR

Make sure that .py files are set to open with Python for the bank ripper to work
Custom samples should be in wav format for proper conversion to vadpcm.bin
An OoT 1.0 Decompressed rom is required for the instrument bank creation process you need to find this yourself
To get a zbank/bankmeta file you need to create a custom bank using seq64 save it to a bank slot I usually use bank 0x25 then save it to rom. After that you need to take
the rom to OoTR Bank Ripper and drag the rom onto the "drop you rom here.bat" then you select the zbank/bankmeta that you saved over in Seq64 and drag it over to the
music folder that the sequence is in. After you need to set the bank in the meta file to "-" for the randomizer to recognise that you are using a custom bank. If your
bank uses a custom sample make sure that the offset for the sample in the bank matches the respective sample in the meta file so the randomizer knows what sample is for
what instrument
Your .meta file should look like this
VVVVV
CUSTOM MUSIC NAME HERE
-
bgm/fanfare here
categories here
ZSOUND:soundnamehere.zsound:12345678
^^^^^
N64SoundTool is useful for extracting samples from other N64 games you can also use it to import samples but its not as accurate as the sound files that Sample Creation
Tools create
