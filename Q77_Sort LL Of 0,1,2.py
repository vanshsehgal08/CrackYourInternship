def sortList(self):

	# initialise count of 0 1 and 2 as 0
		count = [0, 0, 0]

		ptr = self.head

		# count total number of '0', '1' and '2'
		# * count[0] will store total number of '0's
		# * count[1] will store total number of '1's
		# * count[2] will store total number of '2's 
		while ptr != None:
			count[ptr.data]+=1
			ptr = ptr.next

		i = 0
		ptr = self.head

		# Let say count[0] = n1, count[1] = n2 and count[2] = n3
		# * now start traversing list from head node,
		# * 1) fill the list with 0, till n1 > 0
		# * 2) fill the list with 1, till n2 > 0
		# * 3) fill the list with 2, till n3 > 0 
		while ptr != None:
			if count[i] == 0:
				i+=1
			else:
				ptr.data = i
				count[i]-=1
				ptr = ptr.next

