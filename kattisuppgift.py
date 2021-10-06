def binarySearch(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binarySearch(alist[:midpoint],item)
	          else:
	            return binarySearch(alist[midpoint+1:],item)
	
	testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
	print(binarySearch(testlist, 3))
	print(binarySearch(testlist, 13))
  
  
  def main():
    #Läs in listan
    indata = input().strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()
