# Answers shown as four different functions, you should just modify the one function as you go along.

# 1. Create a function called complex, which takes two integer parameters and returns a list containing both parameters

def complex(int1,int2):
  return([int1,int2])

# 2. Uncomment #2 below. Modify complex so that if only one parameter is used the second will default to zero

def complex(int1,int2=0):
  return([int1,int2])

# 3. Uncomment #3 below. Modify complex to take a third, optional parameter called out. out should default to "". If out is "string" complex should return a string in the for "int1 + int2i"

def complex(int1,int2=0,out=""):
  if out=="string":
    return(str(int1) + " + " + str(int2) +"i")
  return([int1,int2])

# 4. Uncomment #4 below and run your code. You should get the output "1 + -3i". Correct your code so it handles negative second parameters correctly

def complex(int1,int2=0,out=""):
  if out=="string":
    if int2 < 0:
      return(str(int1) + " - " + str(int2*-1) +"i")
    else:
      return(str(int1) + " + " + str(int2) +"i")
  return([int1,int2])
