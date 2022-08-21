class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        cur_m = m
        i = 0
        j=0
        while (i < n):
            
            
            
            
            if(nums1[j] < nums2[i] and j < cur_m ):
                j = j + 1
            
            else:
                k = cur_m - j
                temp_m = cur_m
                while(k > 0):
                    
                    nums1[temp_m] = nums1[temp_m-1]
                    temp_m = temp_m - 1
                    k = k - 1
                cur_m = cur_m + 1
                    
                nums1[j] = nums2[i]
                j =  j + 1
                i = i + 1
                
                
                
                