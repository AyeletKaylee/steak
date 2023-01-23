# selection sort explained: https://www.youtube.com/watch?v=4CykZVqBuCw

def selection_sort(lst):
    indexing_length = range(len(lst) - 1)

    for i in indexing_length:
        min_value = i

        # all elements to the right of the curr element
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_value]:
                min_value = j

        # takes care of the switch
        if min_value != i:
            lst[min_value], lst[i] = lst[i], lst[min_value]

    return lst

print(selection_sort([7,8,9,8,7,6,5,6,7,8,9,0]))

# runtime:
# O(n²)

#    *******     **              **      ****  **  
#   **/////**   **             **/ **   */// *//** 
#  **     //** **   *******  **   // **/    /* //**
# /**      /**/**  //**///**//      //    ***   /**
# /**      /**/**   /**  /**             *//    /**
# //**     ** //**  /**  /**            *       ** 
#  //*******   //** ***  /**           /****** **  
#   ///////     // ///   //            ////// //   