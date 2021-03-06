# 697. Degree of an Array

## Solution

先找到每个元素出现的次数以及数组的`degree`，然后遍历数组，
对于出现次数正好等于`degree`的元素，找到它第一次出现和最后一次出现的位置，就能找到如果以它为最多元素的数组长度。
找到这个数对于所有次数等于`degree`的元素中的最小值即可。

我和最快的方法一样，但是只击败了6.46%...

原因：

1. 最主要的原因竟然是，答案特判了一下`degree == 1`的情况，这种情况下直接返回`1`即可。
但是在我的算法里这种情况最浪费时间，因为要遍历整个数组，复杂度变为`O(n ^ 2)`，`n`为数组长度。

2. 还有颠倒数组不需要每次都在从后往前找的时候做，提前算出来备用。

3. 在计算距离的时候`last`本来最后还要减一，但是在计算实际最短数组的时候还得加一，抵消了都不用写。

4. 统计出现次数的时候，用`collections.Counter`要比遍历加`dict`更快。