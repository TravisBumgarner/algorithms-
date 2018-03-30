def merge_sort(a, side):
    print(side, a)
    if len(a) == 1:
        return a

    elif len(a) == 2:
        return a if a[0] < a[1] else [a[1], a[0]]

    else:
        mid = int(len(a) / 2)

        a_left = merge_sort(a[:mid], '{} -> left'.format(side))
        a_right = merge_sort(a[mid:], '{} -> right'.format(side))

        out = []

        l = 0
        r = 0

        while len(out) < len(a):

            if a_left[l] < a_right[r]:
                out.append(a_left[l])
                l += 1

            elif a_left[l] > a_right[r]:
                out.append(a_right[r])
                r += 1

            else:
                out.append(a_left[l])
                l += 1

                out.append(a_right[r])
                r += 1

            if l == len(a_left):
                out += a_right[r:]

            if r == len(a_right):
                out += a_left[l:]

        return out


x = merge_sort([9,8,7,1,2,3,5,4,3], 'main')

print(x)