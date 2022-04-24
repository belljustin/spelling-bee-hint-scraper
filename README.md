# NYT Spelling Bee Helper

My partner and I like to do the [New York Time's Spelling Bee](https://www.nytimes.com/puzzles/spelling-bee).
The NYT publishes a grid every day, similar to [this one](https://www.nytimes.com/2022/04/23/crosswords/spelling-bee-forum.html), which provides hints.

This tool allows the user to input their words and have the counts removed from the grid as they complete the puzzle.

## Instructions

```
git clone git@github.com:belljustin/spelling-bee-hint-scraper.git
cd spelling-bee-hint-scraper
pip install -r requirements
python main.py
```

Enter your words at the prompt and the counts will be updated.

It will catch some mistakes, such as wrong starting letters or a word entered multiple times, but not all input mistakes.
For example, it does not have a dictionary so it will continue erroneously if you enter an incorrect word.

## Example

```
4       5       6       7       8
E       1       0       0       0       0
L       0       0       2       0       0
N       0       0       1       1       0
P       12      4       3       0       1
U       0       2       1       0       0
V       1       0       0       1       0
EP-1
LI-1
LU-1
NI-2
PE-6
PI-8
PL-1
PU-5
UN-3
VE-1
VU-1

Next word:
```
