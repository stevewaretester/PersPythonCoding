# PersPythonCoding
I made two different attempts for this particular task, which I will outline below.

## OneStringReturn
This method is closest to the spec - a function that prints a string and returns it, with the test_allStrings matching this output perfectly.

## DataReturn
This version prints the strings in function, then returns the values. There's 3 tests that then check these individual variables, as the function is called and the values set in the setUP of the test.

## Thoughts
This is a bit of a messy function, given that it has 3 values - ideally there should be 3 functions to keep the code atomic, perhaps linking into properties that can store the other values for optimisation. Then each function can have a discrete unit test that tests just its output.
Likewise, a different test framework other than the default unit test might have offered more functionality and better test penetration.

But given the spec, I feel both my solutions match the requirements of this code test.