# CISC-121-Final-Project---Duco-Tabor - Jump Search
https://huggingface.co/spaces/Fronza587/CISC_121-Duco-Jump_Search_Visual

## Step 1: Algorithm Choosing
I have chosen to visualise Jump Search for this project. I think a core part of the course was searching algorithms, and as a beginner in computer programming and coding I had not even really considered the option of any other search than linear search, let alone its complexity. I picked Jump Search as I believe it is a nice first step of a searching algorithm that is better than linear search, but not immediately the jump to binary search. I think visualising its role of an algorithm lying between linear and binary search is very suitable for a project like this.

## Step 2: Plan using computational thinking

### Decomposition:
The main goal of the algorithm is to improve the efficiency compared to ordinary Linear Search. We pick a block size, step, which mathamatically is proven to be most effective as sqrt(n) where n is len(arr).  We then jump by step until the block's last element >= target (or end). We then apply linear search within that block to find the target value of the array. We also implement a kind of early exit/failsafe, when the left bound gets larger than the array size n. We do this within the linear search part too, when the left bound becomes equal to either the right bound (step, in this case) or the array length n. The algorithm thus consists of two main parts (a jump phase and a linear phase). Within these parts there are of course smaller substeps, and other failsafes also have to be incorporated into the algorithm.

Inputs: Array, Target
Constraint: the array has to be sorted in non-decreasing order, with length n >= 0. In addition, I won't be going into negative integers either, as it creates extra work but does not really influence the end result of the visualisation.
Core Goal: Find the target in this given array, or indicate that the target is not present if the array does not contain the target. Some extra failsafe possibilities such as the one for empty list could be added later.

### Pattern Recognition:
Not really applicable for deployment of Gradio apps, as very simple blocks are used and the algorithm of choice does not have very repetitive steps exepct for incrementing step. The algorithm first jumps and checks if the largest value of the previous block (aka the index to the left of the jump-index) is larger or smaller than the target. As long as it is smaller, it repetitively keeps jumping. When this condition becomes untrue, the linear phase starts a common linear-repetition of i += 1 increments.  

### Abstraction & Algorithm Design:
The rough, non-UI based implementation of Jump Search was coded from class material and memory and only focuses on core functionality. The GUI update for this part will follow later, below. The GUI part is mostly the visualisation of what is going to be shown to the user (moving step, then applying linear, and so on), but also a text box to type in a list and a target, the input for the algorithm. 

##### Flow chart of core algorithm:
<img width="661" height="1238" alt="image" src="https://github.com/user-attachments/assets/04f4e50e-13de-4c76-8399-a99df9b1a879" />

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

#### GUI Update 4:
I am going to make an actual visualisation now using gr.HighLightedText, to clearly show the jumps the algorithm makes. The input for this is list of (word, category) tuples, in which for my case the word category will be the array itself, and the category will show the indexes that need to be highlighted throughout the steps.

Update 4.5:
Okay, I am finally through. The debugging part in HighlightingGR took a lot longer than I expected, as I had to change one of the main outputs of my function to the actually Visualiser. I chose HighlightedText instead of the more complicated HTML method, as I doubt that I was going to add in major amounts of user interactivity into the HTML regardless, and the Highlighting Method is more straight-forword and easier to implement without making much of a visual difference. I also chose to exclude the actual act of comparison for the algorithm, as that would've cluttered things up. The Gradio website for Highlighting was not as helpful as I thought, so I needed a bit more of help from AI (ChatGPT 5) in this part, while still having 0 LINES of code written by AI itself. This might explain why my app.py is not the most clean or structured as a bot would make it.

Something that was nice was that apart from the extra function, I could usually insert lines of code that worked towards the Highlighting part in sections where I had already implemented stuff for the log of the notebook. Besides this I mainly needed to change all return statements to give the correct input to the build_dgts_indxs function. 

For debugging, the Hugging Face Running Log was really helpful with most fixes. If I could not determine the cause of the error myself, I often noticed that when asking ChatGPT, it would point me in the right direction of fixing the code but often suggested a solution that did not seem suitable for the project, and I often implemented a different solution. An example of this is in Line 85 of app.py, where AI seemed very set on visualising the jump values on the index of the last element in the previous block, as that is indeed the value that the algorithm compares the target to. This made the rest of the Highlighting part more complex. However, from a human perspective, the jump values themselves (step) were a lot more logical to visualise, so I implemented block_end + 1, a solution that AI disagreed with. Besides, the AI sometimes still had its occasional hallucinations. 

I also changed the theme of the Blocks(). 

## Step 5:
I have tried a lot of user inputs, including edge cases (see the screen recording in GitHub repository, as I could not add it in the MD). Below I show one of the edge cases not included in the screen recording.
<img width="2814" height="1496" alt="image" src="https://github.com/user-attachments/assets/90fbcbce-6fdc-46c3-91fc-fd9c95315d9f" />


## Hugging Face Link
https://huggingface.co/spaces/Fronza587/CISC_121-Duco-Jump_Search_Visual 

## Author
Duco Tabor. 

For other sources, GeeksForGeeks' website provided helpful information about the definitions of a lot of methods (e.g. https://www.geeksforgeeks.org/python/python-string-isalpha-method/). Furthemore, the website of Gradio itself was very useful for Gradio UI parts as well (e.g. https://www.gradio.app/docs/gradio/highlightedtext). 

Lastly, AI was used in the instances outscribed above, only ChatGPT 5.1. AI has not written a single part of code and only provided insights or debugging help. 

















