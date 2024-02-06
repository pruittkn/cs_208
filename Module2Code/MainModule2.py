# Author: Katie Pruitt
# Purpose: Direct proof that the square of every odd integer is also odd
import random

def check_parity(var: int):
    ########################################################
    #   check_parity() will return 0 if var can be expressed as 2k for
    #   soem integer k and is thus even.
    #   check_parity() will return 1 if var can be expressed as 2k + 1 for
    #   some integer k and is thus odd.
    #
    #   check_parity() will also return the value of k.
    ########################################################

    parity = var % 2
    k = var // 2
    return parity, k


if __name__ == '__main__':
    # THEOREM: The square of every odd integer is also odd
    #
    # PROOF:
    # Let n be an odd integer. We shall prove that n^2 is an odd integer.
    #
    # For sake of compilation, I assign n to be a random odd
    # integer between 1 and 1001, though the value does not matter.

    n = random.randrange(1, 1001, 2)

    # Since n is odd, n = 2k + 1 for some integer k
    # The function check_parity(n) verifies that n is odd and returns the value of k
    # for a given value of n
    parity, k = check_parity(n)

    if (parity == 1):
        print("n is odd, therefore n = 2k + 1 for some integer k")
        print(f"In this particular example, {n} = 2 * {k} + 1")
    else:
        print("n is even, therefore n = 2k for some integer k")
        print(f"In this particular example, {n} = 2 * {k}")

    # We can plug (2k + 1) for n into the expression n^2 to get:
    # n^2 = (2k + 1)^2
    #     = 4k^2 + 4k + 1
    #     = 2(2k^2 + 2k) + 1

    # Since k is an integer, 2k^2 + 2k is also an integer
    # Therefore, n^2 can be expressed in the form 2m + 1,
    # where m = 2k^2 + 2k is an integer.
    #
    # Therefore, n^2 is odd. ∎
    n_squared = pow((2*k + parity),2)

    # Below, I verify that n^2 is also odd
    parity_nsquared, k_nsquared = check_parity(n_squared)

    if (parity_nsquared == 1):
        print("n^2 is odd, therefore n^2 = 2m + 1 for some integer m")
        print(f"In this particular example, {n_squared} = 2 * (2*{k}^2 + 2{k}) + 1 = 2 * {k_nsquared} + 1")
    else:
        print("n^2 is even, therefore n^2 = 2m for some integer m")
        print(f"In this particular example, {n_squared} = 2 * (2*{k}^2) = 2 * {k_nsquared}")
