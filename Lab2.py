
def main():
 print("ET0735(DevOps for AIoT) - Lab 2 - Introduction to Python")
 display_main_menu()
 num_list=get_user_input()
if __name__ == "__main__":
    main()
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average():
    floatlist=[]
    average=sum(floatlist)/len(floatlist)
    print("Average is " + average)
    return average
    

def get_user_input():
   floatlist=[]

   x = input()
   x.split(", ")
   floatlist = [float(value) for value in x]
   return floatlist
   
def find_min_max():
   floatlist=[]
   Max=max(floatlist)
   print("Max is" + Max)
   Min=min(floatlist)
   print("Min is" + Min)

def sort_temperature():
   sortednumbers = sorted(floatlist=[])
   print(sortednumbers)

def calc_median_temperature():
   floatlist=[]
   n = len(floatlist=[])
   if n % 2 ==1:
      median = floatlist=[n//2]
   else:
      middle1 = floatlist=[n//2-1]
      middle2 = floatlist=[n//2]
      median = (middle1 + middle2) / 2
   
   print (median)
   return median
