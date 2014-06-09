my-dirty-script-collection
==========================
Little script which adds lyrics to mp3 files from text files with the same track numbering.
0 byte files are tweaked as instrumental
E.g.:
Track 1 gets lyrics from a file called {1}
```
apply_lyrics.py -musicPath /Path/To/MusicAlbum --lyricsPath /Path/To/Lyrics/
```

Where /Path/To/MusicAlbum should be a directory containing mp3 files which have at least the track No ID3Tag
For Example:
```
21:16:06 loki-afro@computer:/Path/To/MusicAlbum~$ls -lshtr
34128 -rwxr-xr-x  1 loki-afro  staff    17M Jun  9 20:27 09 In Melancholy Moonless Acheron.mp3
15896 -rwxr-xr-x  1 loki-afro  staff   7.8M Jun  9 20:27 08 Manisolas from Misandria.mp3
38128 -rwxr-xr-x  1 loki-afro  staff    19M Jun  9 20:27 07 This Place Has Been Passed.mp3
66760 -rwxr-xr-x  1 loki-afro  staff    33M Jun  9 20:27 06 Mount Meru.mp3
21328 -rwxr-xr-x  1 loki-afro  staff    10M Jun  9 20:27 05 The Land Beyond the Pole.mp3
38408 -rwxr-xr-x  1 loki-afro  staff    19M Jun  9 20:27 04 The Solar Burial.mp3
45664 -rwxr-xr-x  1 loki-afro  staff    22M Jun  9 20:27 03 The God in Ruins.mp3
57520 -rwxr-xr-x  1 loki-afro  staff    28M Jun  9 20:27 02 The Self-Made Man.mp3
24352 -rwxr-xr-x  1 loki-afro  staff    12M Jun  9 20:27 01 The Sadness of Vultures.mp3
```

and /Path/To/Lyrics/ should have the following structure:
```
1:17:22 loki-afro@computer:/Path/To/Lyrics/~$ls -lshtr
8 -rw-r--r--  1 Zarathustra  staff   530B Jun  3 21:58 9
0 -rw-r--r--  1 Zarathustra  staff     0B Jun  3 21:58 8
8 -rw-r--r--  1 Zarathustra  staff   149B Jun  3 21:58 7
8 -rw-r--r--  1 Zarathustra  staff   887B Jun  3 21:58 6
0 -rw-r--r--  1 Zarathustra  staff     0B Jun  3 21:58 5
8 -rw-r--r--  1 Zarathustra  staff   295B Jun  3 21:58 4
8 -rw-r--r--  1 Zarathustra  staff   1.4K Jun  3 21:58 3
8 -rw-r--r--  1 Zarathustra  staff   619B Jun  3 21:58 2
0 -rw-r--r--  1 Zarathustra  staff     0B Jun  3 21:58 1 #instrumental
```
