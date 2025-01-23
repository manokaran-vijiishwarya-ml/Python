try:
    n = 0
    # n=5
    # n=110
    # n=-1
    res = 100 / n
    
# except ZeroDivisionError:
#     print("You can't divide by zero!")
except Exception as e:
    print(e)
   
else:
    print("Result is", res)
    
finally:
    print("Execution complete.")