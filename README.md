My solution to:

https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/

The probability that the first contestant survives the xth round and the others do not is:

(.99^x)(1-.98^x)(1-.97^x)...(1-.90^x)

The solution represents the sum of these probabilities for x=1...infinity

This Python program runs until a percent change indictor in the accumulator is less than 0.0001%.
