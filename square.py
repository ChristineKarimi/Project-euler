#sum square difference

def main():
   # finding sum of the squares.

   a = sum([i**2 for i in range(101)])    # finding the square of the sum.
   b = sum(range(101))**2                 # Results.
    print(b - a)
    if __name__ == '__main__':
    main()