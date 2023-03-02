class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {

        val complements: MutableMap<Int, Int> = mutableMapOf()

        for (i in nums.indices) {
            val complementsIndex = complements[nums[i]]
            complementsIndex?.let { return intArrayOf(i, it) }
            complements += Pair(target - nums[i], i)
        }

        return nums
    }
}