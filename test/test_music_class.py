from lib.music_class import *

def test_music_class_exist():
    result = Music()
    assert isinstance(result, Music) is not None 

def test_return_empty_song_list():
    result = Music()
    result.show_songs()
    assert result.list_track == []

def test_add_song():
    result = Music()
    result.add("Desert rose")
    assert result.list_track == ["Desert rose"]

def test_return_list_of_one_song():
    result = Music()
    result.add("Desert rose")
    result.show_songs()
    assert result.list_track == ["Desert rose"]

def test_return_list_of_two_songs():
    result = Music()
    result.add("Desert rose")
    result.add("On the floor")
    result.show_songs()
    assert result.list_track == ["Desert rose", "On the floor"]
