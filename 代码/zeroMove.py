{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 12, 0, 0, 0]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l = [0,1,0,2,0,3,12]\n",
    "class Solution:\n",
    "    def moveZeroes(self, nums):\n",
    "        \"\"\"\n",
    "        Do not return anything, modify nums in-place instead.\n",
    "        \"\"\"\n",
    "        # 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置\n",
    "        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。\n",
    "        \n",
    "        # 循环遍历数组，当遇到非零元素的时候替换掉前面0元素\n",
    "        # j 记录最新非零元素的位置\n",
    "        j = 0\n",
    "        for i in range(len(nums)):\n",
    "            if nums[i] != 0:\n",
    "                nums[j] = nums[i]\n",
    "                if i != j:\n",
    "                    nums[i] = 0\n",
    "                j += 1\n",
    "        return nums\n",
    "\n",
    "        \n",
    "s = Solution()\n",
    "s.moveZeroes(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3, 12, 0, 0, 0]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "l = [0,1,0,2,0,3,12]\n",
    "class Solution:\n",
    "    def moveZeroes(self, nums):\n",
    "        \"\"\"\n",
    "        Do not return anything, modify nums in-place instead.\n",
    "        \"\"\"\n",
    "        # 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置\n",
    "        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。\n",
    "        \n",
    "        # 循环遍历数组，当遇到非零元素的时候替换掉前面0元素\n",
    "        # j 记录最新非零元素的位置\n",
    "        count = 0\n",
    "        for i in range(len(nums)):\n",
    "            if nums[i] == 0:\n",
    "                count += 1\n",
    "            elif count > 0:\n",
    "                nums[i - count], nums[i] = nums[i], 0\n",
    "        return nums\n",
    "\n",
    "        \n",
    "s = Solution()\n",
    "s.moveZeroes(l)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "l = [0,1,0,2,0,3,12]\n",
    "class Solution:\n",
    "    def moveZeroes(self, nums):\n",
    "        \"\"\"\n",
    "        Do not return anything, modify nums in-place instead.\n",
    "        \"\"\"\n",
    "        # 循环记录0元素的个数，并且遇到非0元素时候，将非0元素替换到0元素的位置\n",
    "        # count 记录0元素的个数， i - count实际上是记录了零元素的位置。\n",
    "        \n",
    "        # 循环遍历数组，当遇到非零元素的时候替换掉前面0元素\n",
    "        # j 记录最新非零元素的位置\n",
    "        i = 0\n",
    "        for j in range(len(nums)):\n",
    "            if nums[j] != 0:\n",
    "                nums[i], nums[j] = nums[j], nums[i]\n",
    "                i += 1\n",
    "        return nums\n",
    "\n",
    "s = Solution()\n",
    "s.moveZeroes(l)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
