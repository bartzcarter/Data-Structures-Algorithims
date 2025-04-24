
class Solution:
    def generate_tri(self, numRows):
        tri = []

        for i in range(numRows):
            if i == 0:
                tri.append([1])
            else:
                prev_row = tri[-1]
                new = [1]
                for j in range(1, i):
                    new.append(prev_row[j-1] + prev_row[j])
                new.append(1)
                tri.append(new)

        return tri

def main():
    solution = Solution()
    triangle = solution.generate_tri(5)
    for row in triangle:
        print(row)

if __name__ == '__main__':
    main()