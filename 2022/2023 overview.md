### --- Day 1: Calorie Counting ---

- Find the highest number in a list
- Find the 3 highest numbers in a list and sum them

### --- Day 2: Rock Paper Scissors ---

- Calculate total score when playing according to a set of rules
- Calculate total score when playing to a changed set of rules

### --- Day 3: Rucksack Reorganization ---

- Find common items in two strings, use ASCII value of characters to calculate their priority
- Find common items in groups of 3 strings, calculate priority for each group and sum them

### --- Day 4: Camp Cleanup ---

- Check if a range is completely included in another range
- Check if a range overlaps with another range

### --- Day 5: Supply Stacks ---

- Parse crate diagram
- Move crates from one stack to another and determine which crate ends up on top of each stack
- Move multiple crates at once and determine which crate ends up on top of each stack

### --- Day 6: Tuning Trouble ---

- Loop through a string and detect at which position you find the first occurrence of a sequence of 4 characters that are all different
- Same, but in a sequence of 14 characters

### --- Day 7: No Space Left On Device ---

- Walk through a file system and count the number of directories smaller than a specified size; report sum of those sizes
- Find smallest directory that, if deleted, would free up enough space to get below a certain threshold
Reading the input, i.e. mapping the filesystem is the biggest challenge here. 

### --- Day 8: Treetop Tree House ---

- Read in a grid with trees and their heights; find the number of trees visible from outside the grid.
- Calculate a scenic score for each tree, that reflects its viewing distances in all 4 directions. Find the highest scenic score on the map.

### --- Day 9: Rope Bridge ---

- Trace the head of a "rope" across a grid, tail follows head according to specified rules. Keep count of how many positions were visited by the tail at least once.
- Tail now consists of 10 knots instead of one, which means there is now a large number of types of motion for the tail.

### --- Day 10: Cathode-Ray Tube ---

- Keep track of a value that changes according to a set of instructions
- Use the value, combined with the cycle number to translate the signal to a display on a CRT screen. Mostly lots of modulo stuff and plenty opportunity for off-by-one errors.

### --- Day 11: Monkey in the Middle ---

- Monkeys throwing around items according to rules related to how worried you are about the item. Monkeys perform a division test, and the outcome (boolean) determines which monkey it goes to next. Worry level changes depending on which monkey the item goes to. Worry level is divided by 3 each round to keep it in check.
- In part 2, the division by 3 no longer applies. To keep calculations feasible, a number needs to be found that, if you divide the worry level by it, will return the same test outcome for all of the monkeys that would be produced had the number not been modified. The product of each monkeys division test number is quite high but enough to keep calculations in check.

### --- Day 12: Hill Climbing Algorithm ---

- Find the shortest path to the highest point in a grid from a specified start location. Accessibility of neighbouring positions depends on differences in altitude: you can increase only one, but decrease as much as you want. BFS algorithm.
- Find the shortest path to the highest point from any point in the grid with the lowest altitude.

### --- Day 13: Distress Signal ---

- Check the order of pairs of packets containing lists or ints, according to specified rules. eval() and recursion are the keywords here.
- Sort all packets and determine the position of two marker packets. Requires implementing a sort algorithm.

### --- Day 14: Regolith Reservoir ---

- Sand pours into a cave. Plot the walls of the cave on a grid. Drop sand into it from a start location and see where each unite of sand ends up, according to specified rules. See how many units of sand come to rest until the remaining sand starts pouring into the abyss below. 
- There is actually a flour below. See how many units of sand come to rest until the cave entrance gets blocked. 

### --- Day 15: Beacon Exclusion Zone ---

- You have data from sensors on a grid that each detect one beacon, i.e. the one that is closest to them. Figure out which positions on a specified y-coordinate are not covered by the sensors and therefore might contain a beacon.
- Within a specified search, space, figure out the one position that is not covered by any of the sensors. Search space is very large so plotting each individual point is not feasible. Ranges will have to be used. Possible strategy: calculate the range of positions detected by each sensor at each y-coordinate, merge the ranges and see at which y-coordinate there are two non-overlapping ranges. 

### --- Day 16: Proboscidea Volcanium ---

- This was one of the hardest problems of 2022. You have to open valves to release pressure. Find the best order of opening valves in order to release as much pressure as possible in 30 minutes. This is a graph search problem. BFS will not work as there are too many permutations. 
Solved this using a priority queue with states, where states with a theoretical maximum below the current max are immediately discarded.
- Part 2 is the same but with 2 players and a bit less time. 

### --- Day 17: Pyroclastic Flow ---

- Tetris. Except the rocks don't rotate, fall in the same repeating order and just pile up. They move left and right as a result of jets of hot gas coming out of the walls.
Part 1 is calculating how high the tower will be after 2022 rocks have fallen. 
- Part 2 is calculating how high the tower will be after 1000000000000 rocks have fallen. Since this obviously can not be plotted on a grid, you need to find periods in the events that allow you to predict the height of the tower after that many rounds.
I figured this one out by basically reverse engineering the example. You need to search for patterns; in my case I found a pattern in the downward moves of the rocks, which presumably reflect the period in "tower shape". This allowed me to calculate how much height was added to the tower per tower shape period, and after adding an offset and calculating the added height for this offset, I was able to figure out how high the tower will be. Despite only half understanding what I was doing, I still got the right number pretty quickly, resulting in my best overall ranking of the year.

### --- Day 18: Boiling Boulders ---

- Calculate the surface area of a lava droplet that consists of 3D cubes. Part 1 consists of simply calculating the total surface area, which can be done by counting the number of cube faces that have neigbhours (these are not surface areas).
- Part 2 involves calculating only the surface area on the outside of the lava droplet (some of the surface area may be air pockets inside the droplet). The best way to do this seems to be through a flood fill algorithm. Define an area around the droplet and fill it in using a BFS strategy. Coordinates that can't be reached from the outside but aren't lava either are air pockets and will not be counted. Took me a while to figure that out, it was the first time I ever heard the term "flood fill algorithm".

### --- Day 19: Not Enough Minerals ---

The hardest puzzle of 2022, and the last one I solved, using mostly ideas I didn't come up with myself, unfortunately. My goal was to at least write all my own code. Still it took me quite a while.
- You have to build robots that harvest ore, clay, obsidian and geodes. You need ore and clay to build and obsidian harvesting robot, and ore and obsidian to build a geode robot. How much of each you need depends on a blueprint. Calculate the maximum number of geodes you can harvest in 24 minutes for each of 30 blueprints.
- In part 2, you have to do this for 32 minutes, but only for the first 3 blueprints.
A path finding algorithm with drastic pruning is needed to make this work. DFS recommended but haven't correctly implemented this. Ways to prune: avoid duplicates. Stop producing robots when you are already producing the maximum you could ever theoretically need.
Don't keep stock that exceeds the amount you could ever theoretically need; by capping it you reduce the number of states to investigate. Don't pursue states with a theoretical max geodes below the current best. If you choose not to build a robot you had the resources for, don't do it in any next rounds until you've at least built something else instead. 
After implementing all of these my solution was still very slow but at least it gave me a result. And with it being the last puzzle I solved I was happy enough with that.

### --- Day 20: Grove Positioning System ---

- Decrypt grove coordinates by "mixing" them. Most easily solved by using a circular linked list. Otherwise ends up being a huge mess of off-by-one errors.
- Part 2 involves mixing 10 times. Pretty straightforward once you get part 1 right.

### --- Day 21: Monkey Math ---

- Calculate a number using a recursive function. 
- Part 2 reverses the calculation. Can be solved mathematically but I went the lazy route and used a loop that narrowed down the lower and upper bounds until the correct number was found.

### --- Day 22: Monkey Map ---

- Trace a path on a strangely shaped grid. When you fall off one side, continue on the other side (wrap around).
- Part 2: map turns out to be a cube. This changes the rules of where to go when you fall off the edge. Rules depend on which face of the cube you're on. Requires either superhuman 3D visualization skills or DIY-ing a cube to help you visualize it. Theoretically not the hardest problem but required a huge amount of debugging for me before I got it to work.

### --- Day 23: Unstable Diffusion ---

- Elves spreading out evenly on a grid according to specified rules. After 10 rounds of spreading, define the smallest rectangle containing all elves and calculate number of empty grid tiles.
- Find the number of the first round where no elf moves.

### --- Day 24: Blizzard Basin ---

- Move from one position to another while avoiding blizzards that move through the grid in predictable patterns. Find the minimum time required to get from A to B.
- In part 2, you have to go back and forth between A and B twice because some elf forgot his snacks. 
Important in this puzzle is to read the instructions very carefully, and remember you don't need to keep track of the path, just of the current position of each state and the options from there. 
A lot of states disappear because at some point there is no way they can go without hitting a blizzard. This keeps the number of states in check. 

### --- Day 25: Full of Hot Air ---

- Decode a series of SNAFU numbers. SNAFU numbers are numbers that use powers of 5 (quinary numeral system), with the added complication that the digits are shifted, i.e. not 0-5 but -2 to 2. After decoding the numbers and calculating their sum, you have to encode the sum back into a SNAFU number.