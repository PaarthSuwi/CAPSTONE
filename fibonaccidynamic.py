def fibo(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    # Initialize the DP table with base cases
    dp = [0] * (n + 1)  # Create a list of size (n + 1)
    dp[0] = 0  # Base case: Fibonacci(0) = 0
    dp[1] = 1  # Base case: Fibonacci(1) = 1
    
    # Fill the DP table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # Recurrence relation
    
    # Return the nth Fibonacci number
    return dp[n]