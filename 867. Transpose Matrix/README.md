# 867. Transpose Matrix

## Solution

本身没什么难度。

注意`zip`的用法：把两个可循环的对象的每一项组合再组成新的列表。如：`zip([1, 2], [3, 4]) == [(1, 2), (3, 4)]`。

注意`*`和`**`的用法：是`unpack`的功能。把可循环的对象变成可对应位置的参数列表。如`sum(a, b)`是求`a`和`b`的和的函数，那么`sum(*(1, 2))`就可以把`tuple`的`(1, 2)`拆开最后运算`sum(1, 2)`。`**`是在`dict`中取`value`的值，而如果只有一个`*`则是取`key`。详情见[What does the Star operator mean? [duplicate]](https://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean)。

用`zip`和`*`做能大大降低编程难度。
