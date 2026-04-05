class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bound(l):
            low=0
            high=len(nums)-1
            ans=-1
            while(low<=high):
                mid=(low+high)//2
                if(nums[mid]==target):
                    ans=mid
                    if(l=='left'):
                        high=mid-1
                    else:
                        low=mid+1
                    
                elif(nums[mid]>target):
                    high=mid-1
                else:
                    low=mid+1
            return ans
        return [bound('left'),bound('right')]
            
        