# k06 Readme
Team Blind Elmo

Lucas Lee (Lewis Cass), Zhaoyu Lin

# File I/O
- Used a `with` statement in order to automatically close the CSV file, which is good practice to reduce the risk of unwanted reading/modifying.
- The csv module included a `csv.reader()` method
    - Given the filename and separator character, it will return an iterable containing each line of the csv
    - Each line is represented as a list, with each element being a value in the csv

# Dictionaries
- Useful for storing pairs of data where one might want to access one via another
    - Given a certain key element, a dictionary can store a corresponding value
    - The value can be accessed via the key
    - For example, using dictionary `dict`, one can store a key-value pair with `dict[key] = value` and the value can be accessed using `dict[key]`
    - Looped through the iterable provided via `csv.reader()`, storing each pair of occupation and percentage in a dictionary as a key and value
- Preserves the order in which the keys/values were added
- Can access all the keys using `dict.keys()` and all the values using `dict.values()`
    - Used to weight each occupation by its respective percentage

# Lists
- Contains an ordered collection of values, which can be of differing data types
    - Indexed with integers, starting from zero and counting up
    - Can be preset with values, for example `list = [2,3,4]`
    - For example, using list `list`, one modify an already set index using `list[index] = new_value` and the value can be accessed using `list[index]`
    - Cannot set or access values beyond the current maximum index using `list[index]` notation
        - Can be appended to using list methods such as `list.append()`
- Converted dictionary keys and values to lists in order to utilize them as random weights and results for the random function that required a list

# Weighted Random Selection
- Imported the `random` library to use the `random.choices()` method
    - Takes a list of values to be chosen from and a corresponding list of weights
    - The weights determine the probability that its corresponding value will be chosen
    - Returns a list with k randomly selected choices, specified as a parameter to the function
- Used `random.choices()` on a two lists of dictionary values containing occupations and their corresponding percentage
    - Since dictionaries preserve order in both keys and values, the two lists are aligned, making sure each the index of each occupation is the index of its corresponding percentage

# Github-flavoured markdown
  - It's the formatting that GitHub supports
  - Used to make text easier to read and more digestible while being easier to write and understand than HTML
    - Containns many of the same features such as h1-6 headers, lists and tables
    - For example, using tilde for code blocks:
      - `list = [1,2,3]` is much easier to read than list = [1,2,3]
  - The best way to learn is to read the documentation [here](https://github.github.com/gfm/)!
