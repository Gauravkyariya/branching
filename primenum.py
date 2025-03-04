def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers_up_to(limit):
    """Return a list of prime numbers up to a given limit."""
    primes = [n for n in range(2, limit + 1) if is_prime(n)]
    return primes

# Example usage
limit = 50
print(f"Prime numbers up to {limit}: {prime_numbers_up_to(limit)}")
