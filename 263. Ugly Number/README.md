# 263. Ugly Number

## Solution

把所有`2, 3, 5`因子都除掉即可。

注意枚举常数的时候`list`比`tuple`快。
如`[2, 3, 5]`而非`(2, 3, 5)`。