# CISC-121-Final-Project---Duco-Tabor - Jump Search

## Screenshot of test


## Step 1: Algorithm Choosing
I have chosen to visualise Jump Search for this project. I think it is fun because I does not actually get used in practice (as said in class), but it is a nice bridge from linear to binary search and I think a visualisation of it is very suitable for a project like this.

## Step 2: Plan using computational thinking

### Decomposition:
The main goal of the algorithm is to improve the efficiency compared to ordinary Linear Search. We pick a block size, step, which mathamatically is proven to be most effective as sqrt(n) where n is len(arr).  We then jump by step until the block's last element >= target (or end). We then apply linear search within that block to find the target value of the array. We also implement a kind of early exit/failsafe, when the left bound gets larger than the array size n. We do this within the linear search part too, when the left bound becomes equal to either the right bound (step, in this case) or the array length n.

Inputs: Array, Target
Constraint: the array has to be sorted in ascending order, with length n >= 0.
Core Goal: Find the target in this given array, or indicate that the target is not present if the array does not contain the target. Some extra failsafe possibilities such as the one for empty list could be added later.

### Abstraction & Algorithm Design:
The rough, non-UI based implementation of Jump Search was coded from class material and memory and only focuses on core functionality. The GUI update for this part will follow later, below.

GUI Update: xxx

### Pattern Recognition:
Not really applicable for deployment of Gradio apps, as very simple blocks are used.



