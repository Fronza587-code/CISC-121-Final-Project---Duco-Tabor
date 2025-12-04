# CISC-121-Final-Project---Duco-Tabor - Jump Search

## Screenshot of test


## Step 1: Algorithm Choosing
I have chosen to visualise Jump Search for this project. I think a core part of the course was searching algorithms, and as a beginner in computer programming and coding I had not even really considered the option of any other search than linear search, let alone its complexity. I picked Jump Search as I believe it is a nice first step of a searching algorithm that is better than linear search, but not immediately the jump to binary search. I think visualising its role of an algorithm lying between linear and binary search is very suitable for a project like this.

## Step 2: Plan using computational thinking

### Decomposition:
The main goal of the algorithm is to improve the efficiency compared to ordinary Linear Search. We pick a block size, step, which mathamatically is proven to be most effective as sqrt(n) where n is len(arr).  We then jump by step until the block's last element >= target (or end). We then apply linear search within that block to find the target value of the array. We also implement a kind of early exit/failsafe, when the left bound gets larger than the array size n. We do this within the linear search part too, when the left bound becomes equal to either the right bound (step, in this case) or the array length n.

Inputs: Array, Target
Constraint: the array has to be sorted in non-decreasing order, with length n >= 0. In addition, I won't be going into negative integers either, as it creates extra work but does not really influence the end result of the visualisation.
Core Goal: Find the target in this given array, or indicate that the target is not present if the array does not contain the target. Some extra failsafe possibilities such as the one for empty list could be added later.

### Pattern Recognition:
Not really applicable for deployment of Gradio apps, as very simple blocks are used and the algorithm of choice does not have very repetitive steps exepct for incrementing step. 

### Abstraction & Algorithm Design:
The rough, non-UI based implementation of Jump Search was coded from class material and memory and only focuses on core functionality. The GUI update for this part will follow later, below. The GUI part is mostly the visualisation of what is going to be shown to the user (moving step, then applying linear, and so on), but also a text box to type in a list and a target, the input for the algorithm.

#### GUI Update 1:
<img width="2882" height="911" alt="image" src="https://github.com/user-attachments/assets/aaeb6184-c720-420e-b13b-68e65293119f" />
<img width="2506" height="1579" alt="image" src="https://github.com/user-attachments/assets/4ef7202e-432f-49cc-b86b-812c72a970ce" />

After some tinkering and watching both the videos on OnQ about the project, I succeeded in getting a working version of Jump Search as an app, with two textboxes for user input of the list and the target value. The Gradio site iself, 'getting started with blocks', was very helpful. One of the main struggles was getting the user input as correct arguments for the jumpSearch function to handle, as it took a while to find on the Gradio website that for multiple inputs for arguments one has to use a dictionary. I also placed a placeholder within the textbox to point out to the user that they should use no spaces or commas for their input list.

#### GUI Update 2:
Instead of immediately moving on to visualisation, I first wanted to handle some edge cases. I changed the input to only with spaces (and using .split() to separate, since otherwise the list could only contain single digit numbers. I also provided a failsafe for empty lists, commas, and not non-decreasing lists. I also added a markdown with a general introduction to the app. Now I am ready to move on to the actual visualisation of the algorithm.

AI Disclaimer: I provided ChatGPT 5.1 with a sceeenshot of my code and the prompt: "Are there any edge-cases for this code that I have missed? Please only indicate the edge-case as input, and not how to fix the bug." This led me to include failsafes for when either the target or list only contains spaces, and that I had to use the .split() method without an argument (instead of .split(" ")) to improve robustness. This was an easy fix, but funnily enough when I checked in with ChatGPT 5.1 again later, it still hallucinated that I had not fixed the .split() argument edge case. I DID NOT USE ANY AI TO WRITE ANY OF THE CODE!

#### Some screenshots:
<img width="1491" height="1414" alt="image" src="https://github.com/user-attachments/assets/d668bac8-4bc8-48c6-b372-86c3a11e4702" />
<img width="2887" height="1117" alt="image" src="https://github.com/user-attachments/assets/d41c43ae-40e1-4c35-a8df-4eb64066767c" />
<img width="2854" height="1012" alt="image" src="https://github.com/user-attachments/assets/68371e03-7dab-4c51-a88b-32162cb4bfc9" />
<img width="2827" height="991" alt="image" src="https://github.com/user-attachments/assets/091a4e9c-ff96-49b5-9e5c-400c89bbd892" />

#### GUI Update 3:
Well, hours later, we reached a new milestone. I have now succesfully incorporated a logging system into the algorithm, that shows the algorithm's steps as it Jump Searches. This was done by myself and again helpful information on Gradio's website really paved the way. 
<img width="2861" height="1467" alt="image" src="https://github.com/user-attachments/assets/95ff5e4f-4ca6-4754-a0d1-99152f50f77d" />
<img width="1492" height="1453" alt="image" src="https://github.com/user-attachments/assets/0167772a-49b2-4864-af9c-552463bed054" />















