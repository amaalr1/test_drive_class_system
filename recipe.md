# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ Car.                       │
│                            │
│ - Tyres - list of strings
| - tyre_position - list of tyre positions
│ - latest_readings() - list │
│ - Historical_readings() 
     │
│   => [cars ...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Tyre                    │
│                         │
│ - tyre_pressure - integer│
│ - tyre tread depth - float
│- 
│ - tyre_position() - return position│
│    attribute = position - string                     │
└─────────────────────────┘
```
┌────────────────────────────┐
│ Tyre_readings                │
│  -historical_readings - list                        │
│ - latest_readings -        │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘


┌─────────────────────────┐
│           Car           │
│ ─────────────────────── │
│ - tyres: Dict[str, Tyre]│
│ + add_reading(...)      │
│ + get_summary()         │
└────────────┬────────────┘
             │ 1-to-many
             ▼
┌─────────────────────────┐
│          Tyre           │
│ ─────────────────────── │
│ - position: str         │
│ - readings: List[Reading]
│ + add_reading(...)      │
│ + get_latest_reading()  │
└────────────┬────────────┘
             │ 1-to-many
             ▼
┌─────────────────────────┐
│         Reading         │
│ ─────────────────────── │
│ - date: date            │
│ - pressure: float       │
│ - tread_depth: float    │
└─────────────────────────┘

_Also design the interface of each class in more detail._

```python
class Reading:
    # User-facing properties:
    #   tyre_pressure: integer 
    #    tyre_tread_depth : float

    def __init__(self , tyre_pressure , tyre_tread_depth):
        self.tyre_pressure = tyre_pressure
        self.tyre_tread_depth = tyre_tread_depth
        self.reading_date = datetime.datetime.now() # 2026-10-15 with time 





class Car:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self):
        self.tyre_positions = []
        # creating an empty list to put tyre position
        # Side-effects:
        #   None
        pass # No code here yet

    def add_tyre_positions(self , Tyre):
        position = Tyre.tyre_position()
        self.tyre_positions.append(position)


        #
        #
        #
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

class Tyre():
    def __init__(self , position):
        # tyre_position - string 
        # readings = [] - list of all the reaadings
        #  
        #
    def add_reading(self , reading)
    # parameters 
    # reading - tyre object reading 
    # returns:
    #   a list containing the reading added
    # side_effects: 
    #    adding a reading in the list 

    def get_latest_reading(self , reading)
     # parameters 
    # reading - tyre object reading 
    # return :
    #   the whole latest object depending on the date and time


class Car():
    def __init__():
        # tyres - dictionary of Tyre objects
        self.tyres = {}
        #
        #
        #
    def add_reading():




```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
