# {{PROBLEM}} Class Design Sounds Track 

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Music:
    # User-facing properties:
    #   name: string

    def __init__(self, song_name):
        # Parameters:
        #   song_name: string
        # Side effects:
        pass # No code here yet

    def add(self, song_name):
        # Parameters:
        #   song_name: string representing list of songs
        # Returns:
        #   list of songs
        # Side-effects
        #   Add song name to the list of songs
        pass # No code here yet

    def show_songs(self):
        # Returns:
        #   List of songs
        # Side-effects:
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Check for the presents of the class
#
"""
result = Music()
# => True

"""
Check if songs list is empty
#
"""
result = Music()
resul.list_track 
# => True

"""
Given a song name return succesfully added the song
#
"""
song = Music("Desert rose")
song.add("On the floor")
song.add() # => ["Desert rose", "On the floor"]

"""
Return list of songs
#
"""
song = Music()
song.show_songs()
song.show_songs() # => ["Desert rose", "On the floor"]
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
