'''
Write a function to calculate the median of a stream of integers.

Median is calculated as (N+1)/2 where N is the number of digits.
For example, if the stream of digits is 1,2,3,4,5.
Then the first median will be taken with just the first element i.e. N is 1 So,
(N+1)/2 = 2/2 =1.
The second median will be taken among first two elements i.e (2+1)/2 =1.5
Similarly third will be taken among first three elements i.e (3+1)/2 = 2
And so on…
'''


def calculate_median(stream):
    n = 1
    medians = []
    for n in stream:
        median = (n+1)/2
        medians.append(median)
        n += 1
    print(medians)


calculate_median([1, 2, 3, 4, 5])
