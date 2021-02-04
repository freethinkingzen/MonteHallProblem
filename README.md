# Monte Hall Problem
**A toy program to test the results of the Monte Hall Problem in probability and statistics**

## Background
The problem plays on the *Let's Make a Deal* TV show and gets its name from the original host
Monte Hall.

On *Let's Make a Deal* Monte Hall would present a contestant with three doors and tell them
that behind one of the doors was their dream car, but behind the other two were **ZONKS**
which was the show's word for something the contestant wouldn't necessarily want. Often, in
the formulation of this problem, ZONKS are represented as goats.

### For the game:
- Monte would ask the contestant to choose one door.
- Monte would then open one of the ZONK doors to reveal, in our case, a goat.
- Monte would ask the contestant if they wanted to keep their door, or switch to the other
  unopened door.

### Intuition Fails Us
The intuition most people have is that there is a 1/3 chance for getting the car at the
beginnning and no increase or decreas in chance for keeping the original door or switching to a new one.

Often, trying to argue any different will be met with *LOTS* of resistance because it seems 
rediculous to assert that keeping a door or switching would have any meaningful benefit.
However, **YOUR CHANCES ACTUALLY INCREASE WHEN YOU SWITCH TO A NEW DOOR!**

### Explanation 1
**Player Picks Door 1**
| Door 1 | Door 2 | Door 3 |
|--------|--------|--------|
|**ZONK**|**CAR** |**ZONK**|
| Closed | Closed | Closed |
| 1/3    | 1/3    | 1/3    |

| Door 1 | Door 2 | Door 3 |
|--------|--------|--------|
|**ZONK**|**CAR** |**ZONK**|
| Closed | Closed | Open   |
| 1/3    | 1/3    | 1/3    |

__________      ____________________


## Table
**Player Picks Door 3**
| Door 1 | Door 2 | Door 3| Keep Door | Switch Door |
|--------|--------|-------|-----------|-------------|
| Goat   | Goat   |**CAR**| **CAR**   | Goat        |
| Goat   | **CAR**| Goat  | Goat      | **CAR**     |
| **CAR**| Goat   | Goat  | Goat      | **CAR**     |
