# Youtube Downloader

This is a simple python cli (command line interface) for downloading youtube videos as **mp3** and **mp4**.


## Installation
Reqiurements: **Python and pip**

Donwload the latest release and extract the folder anywhere you like. Then execute the **'installer.bat'** (Windows) - This will install all requirements and dependencies.

## Usage

Open a command line in the folder you just downloaded.
Windows: Open the folder in the explorer and write 'cmd' in the path part.

Then you can start downloading the following way:

> ``python main.py <url> -t[mp3,mp4] or --type[mp3,mp4]``

-  The default type is mp3. You could change that in the code if you want to.

Example:
> ``python main.py https://www.youtube.com/watch?v=iSC4P1i9zmE --type mp4``

The files you downloaded will be in the root folder.

## Future updates
I am planning on adding a GUI. We will see when I am doing this.
