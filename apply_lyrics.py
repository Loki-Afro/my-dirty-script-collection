
from mutagen.id3 import ID3, USLT
import sys
import getopt
import os
from os import listdir
from os.path import isfile, join


def main(argv):
        music_disc_path = ''
        lyrics_dir = ''
        try:
                opts, args = getopt.getopt(argv, "hm:l:", ["musicPath=", "lyricsPath="])
        except getopt.GetoptError:
                print_help()
                sys.exit(2)
        for opt, arg in opts:
                if opt == '-h':
                        print_help()
                        sys.exit()
                elif opt in ("-m", "--musicPath"):
                        music_disc_path = arg + '/'
                elif opt in ("-l", "--lyricsPath"):
                        lyrics_dir = arg + '/'
        print 'music_disc_path is ', music_disc_path
        print 'lyrics_dir is ', lyrics_dir
        if not music_disc_path or not lyrics_dir:
                print_help()
                sys.exit(2)
        for_each_mp3file(music_disc_path, lyrics_dir)


def print_help():
    print 'apply_lyrics.py -m <musicPath> -l <lyricsPath>'


def for_each_mp3file(music_disc_path, lyrics_dir):
    only_files = [f for f in listdir(music_disc_path) if isfile(join(music_disc_path, f))]
    for a_file in only_files:
            mp3_file = music_disc_path + a_file
            id3 = ID3(mp3_file)
            file_name_to_search_for = str(id3["TRCK"])
            if file_name_to_search_for.index('/') > 0:
                file_name_to_search_for = file_name_to_search_for[:file_name_to_search_for.index('/')]
            apply_lyrics(mp3_file, id3, lyrics_dir + file_name_to_search_for)


def apply_lyrics(mp3_file, tags, lyrics_file):
    print lyrics_file
    if not os.path.exists(lyrics_file):
        print 'ERROR: No lyrics file found:', lyrics_file, '...skipping'
        return
    else:
        lyrics = open(lyrics_file).read().strip()

    lyrics = lyrics.decode('utf8')

    if len(tags.getall(u"USLT::'en'")) != 0:
        print "Removing Lyrics."
        tags.delall(u"USLT::'en'")
        tags.save(mp3_file)

    tags[u"USLT::'eng'"] = (USLT(encoding=3, lang=u'eng', desc=u'desc', text=lyrics))
    print 'Added USLT frame to', mp3_file
    tags.save(mp3_file)

if __name__ == "__main__":
    main(sys.argv[1:])
