# Monte Hall Problem
**A toy program to test the results of the Monte Hall Problem in probability and statistics**

## Program
The program will run, replicating the steps of the Monte Hall Problem as described below
at the expense of efficiency in order to replicate the problem with fidelity.

The only parameter to tune inside the MonteHall.py code is the ```ROUNDS``` constant that
is initially set to 1000 and can be set to different integer values from the command line.
This dictates the number of times the game is repeated. Like a coin flip, this chances can
deviate from the expected probability over the short term, but with enough trials will always
tend toward the actual probability.

### To Clone:
```git clone https://github.com/freethinkingzen/MonteHallProblem.git```

### Usage:
```
MonteHall.py [-h, --help] [ROUNDS]

optional arguments:
  -h, --help      display help message/usage and exit
  [ROUNDS]        Number of times to repeat the Monte Hall Problem
                  Must be integer value betwwen 1 and 10,000
```

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

### Explanation 1: Combining Probabilities
**Player Picks Door 1**
| Door 1 | Door 2 | Door 3 |
|--------|--------|--------|
|**ZONK**|**CAR** |**ZONK**|
| Closed | Closed | Closed |
| 1/3    | 1/3    | 1/3    |

| Door 1 | Door 2 \| Door 3 |
|:------:|:----------------:|
|**ZONK**|**CAR** \| **ZONK**|
| Closed | Closed \| Open   |
| 1/3    |       2/3        |

-**Keeping the first pick locks the contestant into a 1/3 probability of getting a car instead
of a ZONK.**

-**Switching is gives the contestant the combined probabilities of Monte's door and the other door**


### Explanation 2: Truth Table
**Player Picks Door 3**
| Door 1 | Door 2 | Door 3| Keep Door | Switch Door |
|--------|--------|-------|-----------|-------------|
| Goat   | Goat   |**CAR**| **CAR**   | Goat        |
| Goat   | **CAR**| Goat  | Goat      | **CAR**     |
| **CAR**| Goat   | Goat  | Goat      | **CAR**     |


## Results
 
- **Keep Original Door: 33%**

- **Switch Doors: 66%**

While these probabilities can underperform or overperform, these are the overall probabilities
and will more closely match these numbers with higher numbers of ROUNDS (Law of Large Numbers)
<table>
  <tr>
    <th></th>
    <th scope="col">10 Rounds</th>
    <th scope="col">50 Rounds</th>
    <th scope="col">100 Rounds</th>
    <th scope="col">500 Rounds</th>
    <th scope="col">1000 Rounds</th>
    <th scope="col">10000 Rounds</th>
  </tr>
  <tr>
    <th scope="row">Trial 1</th>
    <td><!---ROUNDS: 10---><b>Keep:</b> 50.00%</br><b>Switch:</b> 50.00%</td>
    <td><!---ROUNDS: 50---><b>Keep:</b> 40.00%</br><b>Switch:</b> 60.00%</td>
    <td><!---ROUNDS: 100---><b>Keep:</b> 29.00%</br><b>Switch:</b> 71.00%</td>
    <td><!---ROUNDS: 500---><b>Keep:</b> 32.80%</br><b>Switch:</b> 67.20%</td>
    <td><!---ROUNDS: 1000---><b>Keep:</b> 33.20%</br><b>Switch:</b> 66.80%</td>
    <td><!---ROUNDS: 10,000---><b>Keep:</b> 32.71%</br><b>Switch:</b> 67.29%</td>
  </tr>
  <tr>
    <th scope="row">Trial 2</th>
    <td><!---ROUNDS: 10---><b>Keep:</b> 80.00%</br><b>Switch:</b> 20.00%</td>
    <td><!---ROUNDS: 50---><b>Keep:</b> 24.00%</br><b>Switch:</b> 76.00%</td>
    <td><!---ROUNDS: 100---><b>Keep:</b> 31.00%</br><b>Switch:</b> 79.00%</td>
    <td><!---ROUNDS: 500---><b>Keep:</b> 34.00%</br><b>Switch:</b> 66.00%</td>
    <td><!---ROUNDS: 1000---><b>Keep:</b> 30.50%</br><b>Switch:</b> 69.50%</td>
    <td><!---ROUNDS: 10,000---><b>Keep:</b> 32.31%</br><b>Switch:</b> 67.69%</td>      
  </tr>
  <tr>
    <th scope="row">Trial 3</th>
    <td><!---ROUNDS: 10---><b>Keep:</b> 50.00%</br><b>Switch:</b> 50.00%</td>
    <td><!---ROUNDS: 50---><b>Keep:</b> 24.00%</br><b>Swithc:</b> 76.00%</td>
    <td><!---ROUNDS: 100---><b>Keep:</b> 28.00%</br><b>Switch:</b> 72.00%</td>
    <td><!---ROUNDS: 500---><b>Keep:</b> 34.40%</br><b>Switch:</b> 65.60%</td>
    <td><!---ROUNDS: 1000---><b>Keep:</b> 33.40%</br>Switch: 66.60%</td>
    <td><!---ROUNDS: 10,000---><b>Keep:</b> 33.67%</br><b>Switch:</b> 66.33%</td>
  </tr>
</table>
    
