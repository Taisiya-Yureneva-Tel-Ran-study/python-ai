## HW#31

### Implementation of the Game of Life algorithm

##### For a space that is populated:
* Each cell with one or no neighbors dies, as if by solitude.

* Each cell with four or more neighbors dies, as if by overpopulation.

* Each cell with two or three neighbors survives.

##### For a space that is empty or unpopulated:
* Each cell with three neighbors becomes populated.

#### The implementation stops once the image is stable. 
However, sometimes it is impossible to reach the stable state - for example, a row of 3 live cells will always alternate between 2 states. That's why there is a limit of 50 iterations.