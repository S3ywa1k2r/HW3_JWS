def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
        
        
    
def main():
    for i in range(0,15,2):
        print("{0:d}! = {1:d}".format(i,factorial(i)))
    

if __name__ == "__main__":
	main()
