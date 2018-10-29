class FizzBuzz:
    def __init__(self,num,string):
        self.num = num
        self.string = string

    def ans_fizzbuzz(self,x):
        if x % self.num ==0:
            print("{} {}".format(x, self.string))


def main():
    f = FizzBuzz(3,"fizz")
    b = FizzBuzz(5,"buzz")

    for i in range(1,101):
        f.ans_fizzbuzz(i)
        b.ans_fizzbuzz(i)

if __name__ == "__main__":
    main()
