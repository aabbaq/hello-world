## 1796. 字符串中第二大的数字

简单题，用来练习Java代码

```java
class Solution {
    public int secondHighest(String s) {
        int length = s.length();
        int first = -1, second = -1;
        for (int i=0; i<length; i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                int num = c - '0';
                if (num > first) {
                    second = first;
                    first = num;
                } else if (num < first && num > second) {
                    second = num;
                }
            }
        }
        return second;
    }
}
```

---

```go
func secondHighest(s string) int {
    first, second := -1, -1
    for _, c := range s {
        if unicode.IsDigit(c) {
            num := int(c-'0')
            if num > first {
                second = first
                first = num
            } else if num < first && num > second {
                second = num
            }
        }
    }
    return second
}
```

