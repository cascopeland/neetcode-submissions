class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i == "*":
                total = nums.pop() * nums.pop()
                nums.append(int(total))
            elif i == "-":
                total = -1 * (nums.pop() - nums.pop())
                nums.append(total)
            elif i == "+":
                total = nums.pop() + nums.pop()
                nums.append(total)
            elif i == "/":
                denom = nums.pop()
                total = int(nums.pop() / denom)
                nums.append(total)
            else:
                nums.append(int(i))
        return nums[0]