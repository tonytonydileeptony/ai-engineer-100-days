def max_value(nums):
     x=0
     for num in nums:
          if x<num:
               x=num

     print(" greatest number "+str(x) )

def main():
     nums=[1,2,3,99,199,0]
     max_value(nums)
if __name__=="__main__":
     main()
