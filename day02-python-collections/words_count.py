def count():
    text = "Hello world! Welcome to the world of Python. Python is fun."
    words_count={}
    words=text.lower().replace('!','').replace('.','').split()
    for word in words:
        if(word in words_count):
         words_count[word]+=1
        else:
            words_count[word]=1
    for word,count in words_count.items():
        print(f"{word}:{count}")

def prime(num):
  

    num = int(input("Enter a number: "))

    if num <= 1:
        print(f"{num} is not a prime number")
    else:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

def main():
   count()
   prime(10)

if __name__=="__main__":
   main()


