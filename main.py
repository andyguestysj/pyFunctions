# 1. Create a function called complex, which takes two integer parameters and returns a list containing both parameters

def complex(int1,int2=0,out=""):
  if out=="string":
    return(str(int1) + " + " + str(int2) +"i")
  return([int1,int2])

# 2. Uncomment #2 below. Modify complex so that if only one parameter is used the second will default to zero

# 3. Uncomment #3 below. Modify complex to take a third, optional parameter called out. out should default to "". If out is "string" complex should return a string in the for "int1 + int2i"

# 4. Uncomment #4 below and run your code. You should get the output "1 + -3i". Correct your code so it handles negative second parameters correctly

def main():

  print(complex(1,2)) # should output [1,2]

  #2 print(complex(1)) # should output [1,0]

  #3 print(complex(1,out="string")) # should output 1 + 0i

  #4 print(complex(1,-3,out="string")) # will initially output 1 + -3i, should output 1 - 3i



if __name__ == "__main__":
  main()

