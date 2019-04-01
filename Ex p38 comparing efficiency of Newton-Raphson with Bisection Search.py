#Newton-Raphson for square root
#find x such that x**2-24 is within epsilon of 0
epsilon = 0.01
k=24.0
guess=k/2.0
NumIterations = 0
while abs(guess*guess - k) >= epsilon: 
    guess = guess-(((guess**2)-k)/(2*guess))
    NumIterations = NumIterations + 1
print('Square root of', k, 'is about', guess, '.', 'Number of Iterations =', NumIterations, '.')



#Compare efficiency of Newton-Raphson with Bisection Search for arbitrary user input. 
epsilon = 0.01
k=float(input('Enter a positive rational number.'))
guess=k/2.0
NumIterations = 0
while abs(guess*guess - k) >= epsilon: 
    guess = guess-(((guess**2)-k)/(2*guess))
    NumIterations = NumIterations + 1
print('According to Newton-Raphson, square root of', k, 'is about', guess, '.', 'Number of Iterations =', NumIterations, '.')

numGuesses = 0
low = 0.0
high = max(1.0, abs(k))
ans = (high + low)/2.0
while abs(ans**2 - abs(k)) >= epsilon:
    numGuesses += 1
    if ans**2 < abs(k):
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('According to Bisection search,', ans, 'is close to square root of', k, '.','Number of guesses =', numGuesses,'.')