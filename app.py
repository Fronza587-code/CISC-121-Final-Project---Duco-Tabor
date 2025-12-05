import gradio as gr
from math import sqrt



def build_dgts_indxs (arr, jump_checked, linear_checked, found_index):
    pairs = []
    for idx, value in enumerate(arr):
        label = None

        if found_index is not None and idx == found_index:
            label = "found"
        elif idx in jump_checked and idx in linear_checked:
            label = "jump + linear"
        elif idx in jump_checked:
            label = "jump"
        elif idx in linear_checked:
            label = "linear"

        pairs.append ((str(value), label))
    return pairs
    #Put list into GR.HighLight



def jumpSearch(li, tg):
    if not li:
        return [], "No user input."
    #Check if there is input.
    if li.isspace():
        return [], "Please enter numbers, not only spaces."
    for i in li:
        if i != " " and not i.isdigit():
            return [], "Other character than space or digit detected."
    #Check if the list only contains spaces and digits
    
    if not tg:
        return [], "No target value was given."
    if not tg.isdigit():
        return [], "Target value has to be a positive integer"
    target = int(tg)
    #Failsafes for target, and convert it to integer.

    arr = []
    splits = li.split()
    for i in splits:
        arr.append(int(i))
    #Convert the input to integers.

    #LOG START: Step 1
    log = []
    log.append(f"Array: {arr}")
    log.append(f"Target: {target}")
    log.append("")

    #HIGHLIGHT INI:
    jump_checked = []
    linear_checked = []
    found_index = None
    
    for j in range(len(arr)-1):
        if arr[j] > arr[j+1]:
            log.append("List is not sorted. Jump Search not started.")
            pairs = build_dgts_indxs(arr, jump_checked, linear_checked, found_index)
            return pairs, "\n".join(log)
    #Check if the array is sorted. If not so, jumpSearch will not work properly.

     #LOG: Step 2
    log.append("List is sorted. Start Jump Search.")
    log.append("")
    
    n = len(arr)
    step = int(sqrt(n))            #Calculate step / jump size
    prev = 0

    if n == 1:                       #Failsafe for if list has one element.
        log.append(f"Array has one element: {arr[0]}")
        linear_checked.append(0)
        if arr[0] == target:
            found_index = 0
            log.append("Target equals the only element in the list.")
        else:
            log.append("Target does not equal the only element. Target not in list.")

        pairs = build_dgts_indxs(arr, jump_checked, linear_checked, found_index)
        return pairs, "\n".join(log)
    
    #LOG: Step 3
    log.append(f"List length n = {n}!")
    log.append(f"Jump step size = root of n = {step}!")
    log.append("")
    log.append("Start Jump phase of Jump Search")
    log.append(f"First step value taken at index {step}, value {arr[step]}")

    while arr[int(min(step,n)-1)] < target:
        block_end = int(min(step,n)-1)       #index at end of current block, largest value
        jump_checked.append(block_end + 1)
        log.append(f"Target larger than the largest value in the current block: {arr[block_end]}, so lets jump on!")
        prev = step
        if prev >= n:
            log.append("Index has reached end of list, so target not in list.")
            pairs = build_dgts_indxs(arr, jump_checked, linear_checked, found_index)
            return pairs, "\n".join(log)
        if step < n:
            log.append(f"Move index to step index: {step}, value of index now {arr[prev]}.")
        else:
            log.append(f"Move index to step index: {step}, which is beyond the end of the list.")
        step += int(sqrt(n))
        if step < n:
            log.append(f"Increment step to: {step}, value of step now {arr[step]}.")
        else:
            log.append(f"Increment step to: {step}, which is beyond the end of the list.")
        
    #Increment steps until the target gets bigger than either the step or the length of the array.
    start_linear = prev
    
    #LOG: Step 4
    log.append("Finished Jump phase of Jump Search")
    log.append("")
    log.append(f"Algorithm settles on last step: {arr[int(min(step,n-1))]}!")
    log.append(f"Algorithm will start linear phase on following index: {prev}, value {arr[prev]} up to {arr[int(min(step,n-1))]}!")
    log.append("")
    log.append("Start Linear phase of Jump Search")
    
    #Start Linear Search part
    while arr[int(prev)] < target:
        if start_linear != 0:
            jump_checked.append(start_linear)
        linear_checked.append(prev)
        log.append(f"Checking if {arr[prev]} is target {target}...")
        prev += 1
        log.append(f"Incremented index by one. Now index is {prev}.")
        if prev == min(step,n):
            log.append("Finished Linear phase of Jump Search")
            log.append("Index has reached step value or end of list, so target not in list.")
            pairs = build_dgts_indxs(arr, jump_checked, linear_checked, found_index)
            return pairs, "\n".join(log)
    
    if arr[int(prev)] == target:              #Check if index value is target.
        linear_checked.append(prev)
        found_index = prev
        log.append(f"Checking if {arr[prev]} is target {target}...")
        log.append("Finished Linear phase of Jump Search")
        log.append(f"Target found at index {prev}!")
        pairs = build_dgts_indxs(arr, jump_checked, linear_checked, found_index)
        return pairs, "\n".join(log)
    else:
        log.append(f"Checking if {arr[prev]} is target {target}...")
        log.append("Finished Linear phase of Jump Search")
        log.append("Target not in list.")
        pairs = build_dgts_indxs(arr, jump_checked, linear_checked, found_index)
        return pairs, "\n".join(log)
    #Rest of edge cases failsafe.

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # A Visualisation of Jump Search -  by Duco Tabor CISC 121
    This little app will visualise how Jump Search works. Type in any list of positive numbers separated by spaces in one textbox,
    and the target value of which you want the index in the other textbox. Below you will see a visual representation of how the algorithm
    finds your target value.
    Note: Jump Search only works on lists in non-decreasing order.
    ## Explanation
    Jump Search is a searching algorithm for sorted lists that speeds up the process by jumping ahead in fixed steps (usually √n) instead of checking every element. 
    When a jump lands on a value greater than or equal to the target, the algorithm knows the target must lie within the previous block. 
    It then performs a simple linear search inside that block to find the exact position. This approach reduces the number of comparisons, 
    giving Jump Search a time complexity of O(√n), which is faster than linear search on large lists.
    """)
    li = gr.Textbox(label="Enter your list here!", placeholder="Type the list with numbers separated by spaces, not commas.")
    tg = gr.Textbox(label="Enter your target value here.", placeholder="Please enter only a positive integer, not any spaces.")
    gr.Markdown(
    """
    ## The Visualisation through highlighting
    In the legend below you can see which colours of highlight correspond to which part of the algorithm.
    Note that the visualisation is given in such a way that the Jump Index corresponds to the jump/step index the algorithm makes,
    not the value that the algorithm actually compares to the target. The latter is the last (and largest) of each block, as you can
    see in the log underneath. Lastly, the index of the jump from which on the algorithm starts the Linear Phase is highlighted
    in another colour for clarification.
    """)
    visual = gr.HighlightedText(label="Array Visualisation", combine_adjacent=False, show_legend=True)
    JumpSearchLog = gr.Textbox(label="Here you can see the log of the steps that the algorithm took!", lines=20)
    find_btn = gr.Button("Find your target!")
    find_btn.click(fn=jumpSearch, inputs=[li,tg], outputs=[visual, JumpSearchLog], api_name="Run")


demo.launch(theme=gr.themes.Citrus(),share=True)
