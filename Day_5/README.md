# Coding Practices

This day will contain 3 examples, designed to get the students familiar with problems encounted when writing code in a collaborative fashion with many poeple. 


## (Example 1) Code Golf - And The Unreadability Problem

For this example we will have students write small code which incentivises them to accomplish a task in as few lines as possible, and then be forced to modify that code to change behavior. The goal is for students to learn the value of code readability. 

### Class is split into 2 groups
#### Group 1 
will be coding the ```fizzbuzz``` example

#### Group 2 
 will be coding the ```robotmove``` example

Useful syntax to help in the code golf excercise:
```
a%b #modulus
str.split() #split a string by delimeter into an array of strings
int(string_instance) #cast a string to a number such that math can be done upon it
```

All code made in the first example will be forced to be commited through git, and be tested through a test driven development mindset. TODO -> decide if we want the class to write any of their own tests for this example, or purely rely upon the provided tests when coding. 

## (Example 2) Class Inheritance Trap
### Class is split into 2 groups

#### Group 1 
students will inherit vehicle instance code which does an example from day 1 perfectly. 

#### Group 2 
will be given already working equivalent code which they have not seen before, which uses functional coding paradigm, without class objects, and without class inheritance. 


Both groups in the class will race to accomplish the creation of a ```vehiclemerge``` function routine given their own paradigm. After both groups have the code working, they will be given 10 minutes to refactor the code such that they feel it is the most easily added onto afterwards. Then the groups will be given an unknown task they cannot prepare for, and race to see who can add functionality fastest with the different paradigm. It should become obvious that in this particular example, using class inheritance and class instances is both slower, and harder to maintain than using objects with static functions. 











