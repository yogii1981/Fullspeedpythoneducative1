# List [] , tupble = (), dict = {}


# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement


def check_age(age):
    if age > 40:
        print("Older than 40")
    elif age > 30 and age <= 40:
        print("Between 30 and 40")
    else:
        print("Other")


age = int(input("Enter the age:"))
print(check_age(age))

# For the construct - For loop


names = ['raj', 'meha', 'silk']
for i in enumerate(names):
    print(i)

names = ['raj', 'meha', 'silk']  # list containing names
for i, name in enumerate(names):
    print("index: {0}".format(i))
    print("Value: {0}".format(name))

###############
print("----Leetcode--- twosumproblem")


class Solution:
    def twosum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complementMap = dict()

        for i in range(len(nums)):
            num = nums[i]
            complement = target - num  # i =1

            if num in complementMap:
                return [complementMap[num], i]
            else:
                complementMap[Complement] = i

        # if num in complementMap:
        #     return [complementMap[num], i]
        # else:
        #     complementMap[complement] = i

    def bruteForceTwoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                sum = nums(i) + nums(j)
                if sum == target:
                    return [i, j]
