def song_decoder(song):
    return " ".join([x.replace(" ", "") for x in song.split("WUB") if x.isalpha()])

print (song_decoder("AWUBWUBWUBBWUBWUBWUBC"))