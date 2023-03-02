class Solution {
    fun compress(chars: CharArray): Int {

        var len = 0
        var index = 0

        while (index < chars.size) {
            var temp = index
            while (index + 1 < chars.size && chars[index + 1] == chars[index])
                index++
            chars[len++] = chars[index]
            if (temp != index) {
                for (ch in (index + 1 - temp).toString())
                    chars[len++] = ch
            }
            index++
        }

        return len
    }
}