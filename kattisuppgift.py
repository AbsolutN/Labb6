def binary_search(alist, item):
	    if len(alist) == 0:
	        return False
	    else:
	        midpoint = len(alist)//2
	        if alist[midpoint]==item:
	          return True
	        else:
	          if item<alist[midpoint]:
	            return binary_search(alist[:midpoint],item)
	          else:
	            return binary_search(alist[midpoint+1:],item)
	
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_search(testlist, 3))
print(binary_search(testlist, 13))
  
def main():
    #Läs in listan
    indata = input("Ange en lista").strip()
    the_list = indata.split()
    #Läs in nycklar att söka efter
    key = input().strip()
    while key != "#":
        print(binary_search(the_list, key))
        key = input().strip()

main()

