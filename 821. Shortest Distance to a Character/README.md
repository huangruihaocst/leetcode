# 821. Shortest Distance to a Character

## Solution

先找到所有的`C`，然后依次找最近的下标。
一开始没有想到只出现一次`C`的情况，所以会出现负数，也即没想到`big`会比当前下标还小的情况。加了绝对值就对了。

答案里有一个方法比较不错，但是复杂度相同。即先找一遍从左到右的最小距离，再找一遍从右向左的最小距离，然后对每个位置求最小值。
