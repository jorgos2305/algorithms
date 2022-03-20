class Algorithm:
    """
    This class contains implementations of different sorting and searching algorithms.
    These implementations are not optimized, they just serve the purpose of learning, you can use them with you own objects.
    Remember to overload the special methods for comparisons

    Check out my Java versions :)

    Enjoy!
    """
   
    @staticmethod
    def selection_sort(elements:list) -> None:
        """
        Sorts inplace.
        Algorithm explanation:
        1. Start looping through the array starting at the index 0 and mark that element and its index as the minimum
        2. Start a second loop scanning all elements starting at index i + 1, we do not need to consider the element we already marked
        3. Keep comparing the elements to the smallest_element and updating this value when you've found an smaller element.
        4. At the end of the inner loop you will have found an element that is smaller than the element marked on the outer loop
        5. Swap the element at index i with the smallest_element
        """
        for i in range(len(elements)):
            index_of_smallest = i                       # keep track of the current index and the current element at this index
            smallest_element = elements[i]              # assume that the first element is the smallest of the array
            for j in range(i+1, len(elements)):         # starting with the next element, search the array for an smaller element
                if elements[j] < smallest_element:
                    index_of_smallest = j
                    smallest_element = elements[j]
            
            elements[i], elements[index_of_smallest] = elements[index_of_smallest], elements[i] # swap
    
    @staticmethod
    def insertion_sort(elements:list) -> None:
        """
        Sorts inplace.
        Algorithm explanation:
        Think of the algorithm as running backwards, at least that is how I picture it.
        1. Starting at index 1 (not at 0!) up to the the length of the list (exclusive)
        2. Start a second loop that works it way backwards from the element selectsd in the previous step to index 0, comparing the current elemetn with its predecesor
        3. if the predecesor is larger than the current element, swap them
        4. if it is not, then, just break out of the loop, because the left part of the list has been already sorted.
           it also works without the break statement, but takes longer because runs all comparisons eventhough it does not need to swap anything
        """
        for i in range(1, len(elements)):
            for j in range(i, 0, -1):
                if elements[j-1] > elements[j]:
                    elements[j-1], elements[j] = elements[j], elements[j-1]
                else:
                    break # this statement give us the O(n) performance in the best case
    
    @staticmethod
    def bubble_sort(elements:list) -> None:
        """
        Sorts inplace.
        Algorithm explanation.
        The target of the algorithm is to push the largest value top the top (or to the right side of the array) as bubbles going up.
        1. starting to loop at the 0 index up to one before the last position of the array
        2. we estart a second loop going from position 0 up to one before the last position - i
           we can stop every loop at the last position -i because the right part of the array has already been sorted, so we can skip some comparisons
        3. while loop we assume that the array is already sorted. Ba doing this we can increment the speed a little, because at the moment when we do not make any swaps it means the array is sorted
           so we do not need to keep sorting
        """
        for i in range(len(elements)-1):
            for j in range(len(elements) - 1 - i):    # we loop up to length - 1 because we compare the current elemenmt to the next, so if we reached the last element and added 1 to that, it will cause an exception
                sorted = True   # Assume that the array is already sorted, this means no swaps performed
                if elements[j] > elements[j+1]:
                    elements[j], elements[j+1] = elements[j+1], elements[j]
                    sorted = False
            if sorted: # this mean we have loop over the whole array and no swaps were necessary
                break
    
    @staticmethod
    def mergesort(array):
        if len(array) <= 1:
            return array
        m = len(array)//2

        left = Algorithm.mergesort(array[:m])
        right = Algorithm.mergesort(array[m:])
        sorted_arr = Algorithm._merge(left, right)

        return sorted_arr
    
    @staticmethod
    def _merge(left, right):
        left_index = 0
        right_index = 0
        inversion_counter = 0
        merged = list()
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                inversion_counter += len(left) - left_index
                right_index += 1
        
        merged.extend(right[right_index:]) # while doing this I made the mistake of using append(), 
        merged.extend(left[left_index:])   # which appended an empty list to the array thus creating a problem in the while loop
                                           # because comparison could be made anymore   
        return merged, inversion_counter
    
    def quick_sort(self, start, end):
        """
        Implementation of quick sort algorithm.
        """
        if end < start:
            return

        if end - start <= 1: # there are only 2 or 1 elements left to sort
            if self.elements[start] > self.elements[end]:
                self.elements[start], self.elements[end] = self.elements[end], self.elements[start]
            return
        
        partition_index = self._partition(start, end)
        self.quick_sort(start, partition_index-1)
        self.quick_sort(partition_index+1, end)

    def _partition(self, start, end):
        pivot = self.elements[start]
        low = start + 1
        high = end

        # Step 1 - check the elements at each index and compare them to the pivot
        while low < high: # check that the elements at the lower indexes are lower/less than the pivot
            while self.elements[low] <= pivot and low < high:
                low += 1 # as long as the elements from the left are lower/less than the pivot increment the index
            while self.elements[high] > pivot and low < high:
                high -= 1 # as long as the elements from the right are higher/more then the pivot decrease the index
            self.elements[low], self.elements[high] = self.elements[high], self.elements[low] # swap the elements

        # Step 2 - after having checked all element check one last time if the element at the low index is greater than the pivot, if it is swap them
        if self.elements[low] > pivot:
            low -=1
        
        # Step 3 - swap the pivot and the element at the low index
        self.elements[start], self.elements[low] = self.elements[low], self.elements[start]

        return low # returns the partition index, so that the smaller sub arrays can be sorted


    def binary_search(self, to_find):
        return self._binary_search(to_find, 0, self.length)

    def _binary_search(self, to_find, start, end):
        if end - start <= 1:
            return self.elements[start] == to_find or self.elements[end] == to_find # base case, the array has 2 or less elements, so fo find is either in one of those or is not
        
        middle = start + ((end - start) // 2)
        if self.elements[middle] == to_find:
            return True
        elif to_find > self.elements[middle]:
            return self._binary_search(to_find, middle+1, end)
        else:
            return self._binary_search(to_find, start, middle-1)
    
    def binary_search_iteration(self, to_find):
        low = 0
        high = self.length - 1
        while low < high:
            middle = (high - low) // 2
            if self.elements[middle] == to_find:
                return True
            if to_find > self.elements[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return False

    def __str__(self) -> str:
        return f"{self.elements}"

if __name__ == '__main__':
    tot_count = 0
    elements = [2,3,9,2,2]

    print(elements)
    s = Algorithm.mergesort(elements)
    print("----------")
    print(s)