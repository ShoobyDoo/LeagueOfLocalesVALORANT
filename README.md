# League Of Locales: VALORANT
> Change the audio for VALORANT while keeping english text!

### Discussion
>Consider joining the [Discord Server](https://discord.gg/fzRK2Sb) for quick access to the community and for general discussion about 
upcoming features. Report bugs and more as well. Enjoy~!

### Supported Locales
* English
* Dutch
* Spanish
* French
* Indonesian
* Italian
* Japanese
* Korean
* Polish
* Portuguese
* Russian
* Malaysian
* Turkish
* Mandarin
 
 > *Please extract the files (.zip) before trying to launch!*

### Prerequisites
* [Python 3+](https://www.python.org/downloads/)
* [psutil 5.7.0+](https://pypi.org/project/psutil/) (Handled automatically by program)
* Add the '--disable-auto-launch' argument to the VALORANT shortcut seen [here](https://cdn.discordapp.com/attachments/584258352859709450/718136425735782440/9bfa32fae4ecce33e72078dadfa681b9.png)
* Have the VALORANT shortcut present on your desktop
* Must already have ENGLISH as your clients starting locale

### Installation

Start by downloading and installing Python from the link above. You will want to tick the "Add python to path" 
option when installing. 

Once Python is installed, double clicking the leagueoflocalesVALORANT.py file should open a command terminal with the script
started.

If it does not open in a command terminal, simply open cmd as administrator and navigate to where you've
extracted the source. 
(cd 'C:\Users\YOURUSERNAME\Desktop\LeagueOfLocalesVALORANT') if you extracted to your desktop for example.

Then, simply type py leagueoflocalesVALORANT.py and press enter. This should start the program.

### Screenshots with explanations

At this point, you should be up to here

![](https://cdn.discordapp.com/attachments/584258352859709450/718134484683194428/bb40d9c0309a798fe4193de88f945a69.png)

Go ahead and press y to allow the program to try and automatically install the dependency it requires. The program
will then automatically close and you will need to relaunch it.

![](https://cdn.discordapp.com/attachments/584258352859709450/718135427655139438/891640440258191ff05adc044eb1e987.png)

Upon restarting, you will be greeted with this screen. At this point, you will want to specify your drive install
location just by simply entering the letter of the drive where VALORANT is installed at. (For example, C)

![](https://cdn.discordapp.com/attachments/584258352859709450/718136813373489222/2253c7d4c420a32db20147d289a8c936.png)

Once you correctly enter the drive where VALORANT is installed, the program will then create a folder on your desktop
to store the english text files. Do not remove this folder as it will break the program. It must stay on the desktop in
no other folders. The program will then automatically scan your desktop for the VALORANT executable and start it. 

*Note: if you have not completed the 'add launch args' part of the prerequisite steps, please do so as if you are logged
into the client, the game will just automatically start.*

![](https://media.discordapp.net/attachments/584258352859709450/718138636939427920/fe5a9b5fc793d657837da508f9199821.png?)

At this point, the program will be prompting you for an entry, however you must first go to the client settings
and select the language you want the audio of. In this case, I select Korean. Do not do anything after selecting the
language, the program will continue from here. At this point, you want to tab back to leagueoflocalesVALORANT

![](https://cdn.discordapp.com/attachments/584258352859709450/718139277283819580/ba9e70830223c97937d66bbd4cf6324c.png)

Once you've selected your language on the client, you will want to enter the language you selected by either typing it
or entering the corresponding number. So in my case I chose Korean, so I can type Korean or just enter the corresponding
number.

![](https://cdn.discordapp.com/attachments/584258352859709450/718140709659476099/fa7a008e30bde26f20b3f94079ddd35c.png)
![](https://cdn.discordapp.com/attachments/584258352859709450/718140727032283206/69d7b74808fe6514f275194ed8a7846b.png)

Shown here, I enter 8 for korean and the program then will automatically kill the client process and after a short
delay, it will re-open the client. At which point you will notice that your client is patching with the newly selected
locale files.

![](https://cdn.discordapp.com/attachments/584258352859709450/718141853647765883/2719258d3e76bfbd01e790cae771042c.png)

At the end of the previous screenshot we saw the program is now prompting us to press ENTER once the client is done 
patching. Since my client is done, I press enter and the program will automatically copy over the necessary english text
files to the VALORANT game directory. Once the program says all steps completed, you can press ENTER one last time to
exit.

![](https://cdn.discordapp.com/attachments/584258352859709450/718142475201544233/7e099bde09a84b959e5d82971dc7df51.png)

Once the program closes, you can then simply just launch VALORANT and as you can see above, all UI Text elements are in
english, and audio is in Korean.

### End!

>*Thank you for reading through all that, hope you enjoy my program!*
>
>*If you have any questions or concerns, please don't hesitate to create a ticket on GitHub or join the Discord for support!*
