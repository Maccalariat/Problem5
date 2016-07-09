"""
Project Euler Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import cProfile
import time

def main(k):
    start = 232792559
    found = False
    broken = False


    while found == False:
        start += 1
        broken = False
        for div in range(2, k):
            if start % div != 0:
                broken = True
                break
        if broken == True:
            continue
        else:
            return(start)


if __name__ == '__main__':

    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))

    cProfile.run('m = main(21)')
    print("the smaallest number divisible with no remainder by range(1, 20) = " , m )

    # print(list)

    print("--- %s seconds ---" % (time.time() - start_time))

