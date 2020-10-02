# Open for Contributions

## Please follow these steps if you wish to contribute to the project

1. Go through the Issues to see if, what you want is already in discussion.

2. Open a new Issue if you do not find what you need. Describe the bug, feature request, problems, additions you might want or anything clearly in the Issue message.

3. Mention in the Issue that you want to work on it.

4. Wait for the approval from the Maintainers of this project before startig to work on it.

5. Create a pull request after making the changes and mention the Issue number that your pull request is related to.

6. Make the required changes if the reviewer asks for them. 

7. That's it! Your pull request will be merged once everything seems okay.

## Special steps to be followed while contributing to this repo

1. All the new functions must be added in the `./functions` directory.

2. The filename for the particular function must be very clear. Use lower case alphabets and hyphens only.

3. Everything else will be automatacially called. Just run the `app.py` file from the root directory and attach a screenshot of the added function to the PR.

4. Refer other function files to keep the structure similar.

5. Every file must have a function named `calc` with required parameters. 

6. Depending on the value of `should_print`, it should print the results or just return otherwise.

```python
    # example for add.py
    
    def calc(should_print=False):

    print("""
    Name: Addition
    Operation : Addition of 2 numbers 
    Inputs : a->int/float , b->int/float
    Outputs: c=>a+b ->float
    Author : suyashsonawane  
    \n
    """)

    a = float(input("Enter a >>"))
    b = float(input("Enter b >>"))

    result = {}
    result['inputs'] = [a, b]
    result['outputs'] = [a + b]

    if should_print:
        print(f"Solution {result['outputs'][0]}")
    else:
        return result
```
