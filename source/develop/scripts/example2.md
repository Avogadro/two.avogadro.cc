# Example Plugin Script - Part 2
## Providing Input to Run Command
- The output of the script depends on the **input argument** as mentioned above in the docs.

- The testing molecule for running the command may be in **CJSON format**
```json
"chemicalJson": 1,
"atoms": {
    "coords": {
        "3d": [0.617532, -0.027246, 0.481009, 
               0.156663, 0.031752, -0.362419, 
               -0.774185, -0.004516, -0.11859],
    },
    "elements": {"number": [1, 8, 1]}
},
"bonds": {"connections": {"index": [1, 2, 1, 0]},
        "order": [1, 1]},
```

The above segment represent a water molecule in CJSON format.
So, an example input molecule for the replace or alloy command may look like:
```
echo '{"Find": "Hydrogen", 
"Percent": 50, 
"Replace": "Carbon",
"cjson": {"chemicalJson": 1,
          "atoms": {"coords": {"3d": [0.617532, -0.027246, 0.481009, 0.156663, 0.031752, -0.362419, -0.774185, -0.004516, -0.11859]},   
          "elements": {"number": [1, 1, 8, 1, 9, 1]}},      
          "bonds": {"connections": {"index": [1, 2, 1, 0]}, 
                    "order": [1, 1]}}
}'| python replace.py --run-command  
```

where 
- 'Find','percent','replace' represent the user inputs to the script interface options
- The --run-command signifies the input argument.

To run the plugin , as mentioned above, you must use ``--run-command`` as the input argument which will execute the  ``runCommand()`` function

## runCommand() Function
```python
def runCommand():
    # Read options from stdin
    stdinStr = sys.stdin.read()

    # Parse the JSON strings
    opts = json.loads(stdinStr)

    # Prepare the result
    result = {}
    result['cjson'] = replace_element(opts, opts['cjson']) #Operation Function and its arguments here
    return result
```

The `runCommand` function is responsible for executing the (in this example, element replacement) operation based on the user options and input data. 

1. **Read Options from Standard Input**:
   - `stdinStr = sys.stdin.read()`: This line reads data from the standard input (stdin).

2. **Parse JSON Data**:
   - `opts = json.loads(stdinStr)`: The `json.loads` function is used to parse the JSON data (in `stdinStr`) into a Python dictionary. 

3. **Element Replacement**:
   - `result['cjson'] = replace_element(opts, opts['cjson'])`:  It calls the `replace_element` function to perform the actual element replacement operation.
     - `opts` contains the user options, including the element to find, the percentage to replace, and the replacement element.
     - `opts['cjson']`  holds the molecular structure in CJSON format.
     - The `replace_element` function takes these options and the molecular structure and returns a modified structure with the specified element replacements.


4. **Return the Result**:
   - `return result`: contains the modified molecular structure in CJSON format.

In summary, the `runCommand` function acts as a bridge between the Avogadro environment and the element replacement operation. 

It reads user options, triggers the replacement operation, and returns the modified molecular structure. 

## Operation Function
This function gets executed through the runCommand() function. It is responsible for the required changes in the input molecule and thus, returns the modified molecule.
### Retrieving necessary components 
```python
def replace_element(opts, mol):
    original= element_dict.get(opts['Find'])
    percent = float(opts['Percent'])
    replace= element_dict.get(opts['Replace'])

    #Code to make Changes to the molecule here

```
Since opts is collective python dictionary which contains the user inputs(in this case, the element to find, the percentage to replace, and the replacement element) and input molecule, .get is used to retrieve the necessary components from the opts dictionary.
For example,
- `original = element_dict.get(opts['Find'])`: This line retrieves the atomic number of the element to be replaced, specified by the user in the "Find Element" option. It uses the element_dict dictionary to map the element name to its atomic number.
- `percent = float(opts['Percent'])`: This line obtains the user-specified percentage of atoms to be replaced with the new element.

### Support for Selection
- It is usually preferable to have selection support that is, for example, minor tweaks which indicate the atoms selected by the user such that **the changes must only be done on those specific atoms**
- Here the input also consists of an additional selected component which is a list indicating the atoms selected, **1 for selected atom and 0 for non selected atom**
For example:
```
echo '{"Find": "Hydrogen", 
"Percent": 50, 
"Replace": "Carbon",
"cjson": {"chemicalJson": 1,
          "atoms": {"coords": {"3d": [0.617532, -0.027246, 0.481009, 0.156663, 0.031752, -0.362419, -0.774185, -0.004516, -0.11859]},  
          "selected":[1,0,0,1,0,0],
          "elements": {"number": [1, 1, 8, 1, 9, 1]}},      
          "bonds": {"connections": {"index": [1, 2, 1, 0]}, 
                    "order": [1, 1]}}
}'| python replace.py --run-command  
```
- If no such component is present we consider all the atoms to have been selected.

Have a look at the code for selection support for the Alloy or Replace command
```python
    # check if the user has any atoms selected
    any_selected = False
    if 'selected' in mol['atoms']:
        for item in mol['atoms']['selected']:
            if item:
                any_selected = True
                break # we have *some* atoms selected

    atomic_numbers = mol['atoms']['elements']['number']
    indices = []

    for i, num in enumerate(atomic_numbers):
        if num == original:
            # two possibilities - nothing selected => do all atoms
            if not any_selected:
                indices.append(i)
            # or only do selected atoms
            elif mol['atoms']['selected'][i]:
                indices.append(i)

    occurences = len(indices)
    number_of_atoms = int((percent*occurences)/100)
    selected_indices = random.sample(indices, number_of_atoms)

    for index in selected_indices:
        atomic_numbers[index] = replace
```

Here, replacement takes place only for the selected atoms

```python
return mol 
```
Finally we get the modified molecule output in the **CJSON format**

## Sample Input and Output 
For example when we give the following input to the alchemy script:
```
echo '{"Find": "Hydrogen", 
"Percent": 50, 
"Replace": "Carbon",
"cjson": {"chemicalJson": 1,
          "atoms": {"coords": {"3d": [0.617532, -0.027246, 0.481009, 0.156663, 0.031752, -0.362419, -0.774185, -0.004516, -0.11859]},  
          "selected":[1,0,0,1,0,0],
          "elements": {"number": [1, 1, 8, 1, 9, 1]}},      
          "bonds": {"connections": {"index": [1, 2, 1, 0]}, 
                    "order": [1, 1]}}
}'| python replace.py --run-command
``` 
we get the following output:
```json
{"cjson": {"chemicalJson": 1, "atoms": {"coords": {"3d": [0.617532, -0.027246, 0.481009, 0.156663, 0.031752, -0.362419, -0.774185, -0.004516, -0.11859]}, "selected": [1, 0, 0, 1, 0, 0], "elements": {"number": [1, 1, 8, 6, 9, 1]}}, "bonds": {"connections": {"index": [1, 2, 1, 0]}, "order": [1, 1]}}}
```

Thus, indicating only 50% of the selected hydrogen atoms have been replaced with carbon.