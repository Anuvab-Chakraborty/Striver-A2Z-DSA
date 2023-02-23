def rev(l, start, end):
    if start < end:
        l[start], l[end] = l[end], l[start]
        rev(l, start + 1, end - 1)


l = [1, 2, 3, 4, 5]
start = 0;
end = len(l) - 1
rev(l, start, end)
print(*l)
