# -*- coding: utf-8 -*-

def sumup(inputs):
    """Input: An array of n integers nums,
       Output: An array output such that output[i] is equal to the sum of all
       the elements of nums except nums[i]."""
    return map(lambda x: sum(inputs) - x, inputs)

if __name__ == '__main__':
# =============================================================================
#     Writing the test case in main.
# =============================================================================
    INPUT = [1, 2, 3, 4]  #declaring the input for the testcase
    print sumup(INPUT)
    