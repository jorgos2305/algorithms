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
    def mergesort(elements:list) -> list:
        """
        Implementation of the merge sort algorithm.
        Algorithm explation:
        The target of the algorithm is to divide the array of element into two sub-arrays and merge the elements back together already sorted.
        This is a recursive algorithim.
        1. Define base case: if the list has only one element or less, the list is already sorted so return it as it is.
        2. Find the Index of the element in the middle of the list.
        3. Divide the list into two sub-lists, one starting from the 0 index to index in the middle (exclusive), the other one from the middle to the end of the original list.
        4. Make recursive calls to the algorithm using the sub-lists just created.
        5. Merge the elements back together and return the sorted list.

        Args:
            elements (list): a list of objects to sorted

        Returns:
            list : a new sorted list of the objects stored in the original list
        """
        if len(elements) <= 1:  # Base case, if 1 or less elements, return the list as it is
            return elements
        m = len(elements) // 2  # This is the index of the element in the middle of the list

        left = Algorithm.mergesort(elements[:m]) # recursive calls using the sublists
        right = Algorithm.mergesort(elements[m:])
        
        sorted_arr = Algorithm._merge(left, right) # merge the elements back together

        return sorted_arr
    
    @staticmethod
    def _merge(left:list, right:list) -> list:
        """
        Merge algorithm to combine the elements of two different lists back together into 1 list.
        This method is supposed to be private and should not be accessed directly over the public interface.
        Algorithm explanation:
        1. Loop through both arrays
        2. compare the elements of the left list to the right list, add the smallest element to the list
           either left of right (this will sort the list from smallest to largest)
        3. If the element of the left list is smaller than the element in the right, increase the left index
        4. If the element of the right list is smaller than the element in the left, increase the right index
        5. When we break out of the loop, it mean we have reached the end of one of the lists
           that mean all the remaining elements of one list are larger than the other, so just add all elements to merged

        Args:
            left (list): list of objects to be merged with right
            right (list): list of objects to be merhed with left

        Returns:
            list: sorted list of elements from left and right
        """
        # keep track of the indexes
        left_index = 0
        right_index = 0
        
        merged = list()
        while left_index < len(left) and right_index < len(right): # loop through the lists
            if left[left_index] <= right[right_index]:             # compare left elements to right elements
                merged.append(left[left_index])                    # if left element smaller, add to merged
                left_index += 1
            else:
                merged.append(right[right_index])                  # if right element larger, add to merged
                right_index += 1
        
        merged.extend(right[right_index:]) # while doing this I made the mistake of using append(), 
        merged.extend(left[left_index:])   # which appended an empty list to the array thus creating a problem in the while loop
                                           # because comparison could not be made anymore   
        return merged
    
    @staticmethod
    def quick_sort(elements:list) -> None:
        """
        This method serves as a wrapper, for the _quick_sort method below

        Args:
            elements (list): list of elements to be sorted
        """
    
    @staticmethod
    def _quick_sort(elements:list, start:int, end:int) -> None:
        """
        Implementation of the quick sort algorithm. The list will be sorted in place.
        Algorithm explanation:
        1. Base case: if we only have one element, then just return. How many elements we have in the portion of the list is check via indexes,
        2. Calculate the partition index
        3. Make two recursive calls form the start up to the partiton index (exclusive) and from the partition index to the end

        Args:
            elements (list): list of elements to be sorted
            start (int): start index of the list
            end (int): end index of the list
        """

        if start >= end:
            return
        
        partition_index = Algorithm._partition(elements, start, end)
        Algorithm._quick_sort(elements, start, partition_index-1)
        Algorithm._quick_sort(elements, partition_index+1, end)

    @staticmethod
    def _partition(elements:list, start:int, end:int) -> int:
        """
        Algoirtihm explanation:
        1. The first element in the list is going to be the pivot
        2. The start index for the comparisons is the second element in the list, since the first one is the pivot already
        3. High index is the endex of the elements greater than the pivot

        Args:
            elements (list): list of the objects that will be sorted 
            start (int): start index of the part of the list that is to be sorted
            end (int): end index of the part of the list that is to be sorted

        Returns:
            int: partition index, all elements before the parition index are lower than the pivot, all elements after the partition index are greater than the pivot
        """
        # pivot is the element which wre are going to used for our comparisons
        pivot = elements[start]
        low = start + 1
        high = end

        # Step 1 - check the elements at each index and compare them to the pivot
        while low < high: # check that the elements at the lower indexes are lower/less than the pivot
            while elements[low] <= pivot and low < high:
                low += 1 # as long as the elements from the left are lower/less than the pivot increment the index
            while elements[high] > pivot and low < high:
                high -= 1 # as long as the elements from the right are higher/more then the pivot decrease the index
            elements[low], elements[high] = elements[high], elements[low] # swap the elements

        # Step 2 - after having checked all element check one last time if the element at the low index is greater than the pivot, if it is swap them
        if elements[low] > pivot:
            low -=1
        
        # Step 3 - swap the pivot and the element at the low index
        elements[start], elements[low] = elements[low], elements[start]

        return low # returns the partition index, so that the smaller sub arrays can be sorted

    @staticmethod
    def binary_search(elements, to_find):
        return Algorithm._binary_search(to_find, 0, len(elements))

    @staticmethod
    def _binary_search(elements, to_find, start, end):
        if end - start <= 1:
            return elements[start] == to_find or elements[end] == to_find # base case, the array has 2 or less elements, so fo find is either in one of those or is not
        
        middle = start + ((end - start) // 2)
        if elements[middle] == to_find:
            return True
        elif to_find > elements[middle]:
            return Algorithm._binary_search(to_find, middle+1, end)
        else:
            return Algorithm._binary_search(to_find, start, middle-1)
    
    @staticmethod
    def binary_search_iteration(elements:list, to_find:object):
        low = 0
        high = len(elements) - 1
        while low < high:
            middle = (high - low) // 2
            if elements[middle] == to_find:
                return True
            if to_find > elements[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return False

if __name__ == '__main__':
    tot_count = 0
    elements = 'Scorpions Rock You Like A Hurricane cover by Sershen Zaritskaya feat Violet Orlandi'.lower().split()

    print(elements)
    s = Algorithm._quick_sort(elements, 0, len(elements)-1)
    print("----------")
    print(elements)