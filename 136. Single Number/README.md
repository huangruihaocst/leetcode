# 136. Single Number

## Solution

答案的方法非常强。把所有数都异或起来，因为相同的数异或结果为`0`，而`0`异或任何数都是这个数本身，所以异或的结果就是这个数。