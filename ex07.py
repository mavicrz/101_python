largest= None
smallest= None
while True:
    n= input ("Enter many numbers you wish and then write done:")
    if n == "done":
        break
    try:
        num= int (n)
        if num > largest:
            largest= num
        elif smallest is None:
            smallest= num
        elif num < smallest:
            smallest= num
        else:
            continue
    except:
        print ("Invalid input")
print ("Maximum is", largest)
print ("Minimum is", smallest)
