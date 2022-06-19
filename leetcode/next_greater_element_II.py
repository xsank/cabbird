def _nextGreaterElements(nums):
    length = len(nums)
    res = [-1] * length
    for i in range(length):
        for j in range(i + 1, i + length + 1):
            mj = j % length
            if nums[mj] > nums[i]:
                res[i] = (nums[mj])
                break
    return res


def nextGreaterElements(nums):
    length = len(nums)
    res = [-1] * length
    stack = []
    for i in range(length * 2):
        n = nums[i % length]
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n
        if i < length:
            stack.append(i)
    return res


if __name__ == "__main__":
    print(nextGreaterElements([1, 2, 1]))
    print(nextGreaterElements([1]))
    print(nextGreaterElements([5, 4, 3, 2, 1]))
    print(nextGreaterElements([]))
    # print(nextGreaterElements([10,44,49,96,13,74,100,110,8,108,48,28,89,3,15,21,115,12,66,16,85,4,102,27,26,40,77,11,99,15,1,70,99,40,34,23,69,85,21,5,2,112,22,123,106,100,50,94,70,63,4,117,77,107,108,74,28,85,85,122,8,23,63,104,114,39,8,68,83,51,43,60,17,62,12,3,64,41,2,98,37,72,54,57,90,116,34,39,33,34,86,10,16,63,35,31,34,48,95,112,13,85,119,116,11,68,81,118,2,113,82,16,41,102,31,56,60,14,35,90,99,81,39,14,5,0,32,99,31,77,18,76,77,41,21,4,10,79,101,7,87,47,105,80,94,48,37,47,123,88,117,85,7,63,35,120,65,92,70,57,39,7,42,79,73,114,80,102,106,71,97,116,38,107,70,19,92,95,46,4,15,80,2,120,11,44,113,121,61,102,64,45,113,30,84,28,124,64,77,31,17,93,113,68,82,3,5,30,93,47,45,97,36,90,104,94,3,121,55,25,49,17,63,118,71,23,62,5,5,96,124,102,63,16,6,119,75,48,70,46,74,98,3,29,13,84,42,32,27,90,71,114,41,105,5,18,125,33,75,34,124,64,97,21,32,74,45,24,65,105,111,60,78,50,57,15,15,61,1,101,114,61,46,40,84,23,42,12,49,38,19,20,115,118,30,5,92,109,12,61,72,45,93,60,119,67,48,107,81,53,83,84,110,121,41,11,9,8,100,102,44,70,14,4,17,111,19,6,76,57,8,38,11,3,109,112,81,68,32,37,65,43,66,59,22,54,45,15,15,73,90,113,101,11,124,15,90,98,39,38,28,89,56,63,34,90,79,77,99,104,62,51,70,93,9,7,24,52,112,25,52,92,39,97,122,24,106,56,56,69,103,41,77,124,107,71,90,8,105,119,104,116,18,94,114,17,22,46,58,67,106,14,31,114,7,115,92,1,39,97,110,84,78,50,43,34,88,106,32,24,58,60,64,94,73,104,115,87,20,14,124,0,101,62,96,52,115,102,18,104,1,20,3,71,98,101,29,106,102,101,40,32,86,75,69,58,5,68,81,34,91,88,31,82,70,115,73,3,78,117,103,65,71,63,98,32,74,122,114,78,113,49,35,113,74,41,111,56,90,100,8,116,26,100,70,10,103,120,101,71,47,125,102,70,117,35,124,31,63,88,82,19,95,34,19,96,60,57,77,109,77,66,40,124,104,116,66,61,4,43,81,13,50,87,28,118,25,117,15,18,108,23,105,80,48,35,121,80,48,77,68,41,26,120,11,70,71,125,25,10,56,96,33,10,60,106,124,5,26,5,28,13,78,1,12,92,92,54,37,31,91,112,72,108,4,88,47,87,43,80,75,44,5,82,34,99,92,63,88,37,83,123,105,115,81,22,26,19,7,104,44,84,5,15,71,5,62,52,100,42,19,113,100,1,41,12,53,38,21,10,100,54,50,81,34,81,90,2,110,95,71,101,106,47,123,37,19,95,7,94,85,24,7,103,30,70,110,23,4,48,69,13,100,99,42,116,66,37,45,38,73,46,90,100,12,87,34,118,84,106,88,94,109,53,101,107,114,45,68,23,79,86,103,86,116,81,60,109,62,91,42,35,26,108,22,12,11,103,43,24,30,37,64,45,102,66,52,86,8,77,101,88,75,114,6,107,57,4,116,26,93,96,110,58,32,104,52,101,114,98,122,85,63,54,67,53,62,34,104,47,98,69,122,30,93,50,69,82,13,58,108,3,15,68,0,12,36,50,12,0,96,45,96,91,3,35,47,50,26,12,54,34,4,59,36,85,4,58,120,97,109,10,36,99,120,104,32,42,3,121,27,58,124,100,19,80,59,88,101,34,87,35,24,4,0,118,46,102,109,19,16,113,105,110,86,23,12,119,64,8,102,109,118,101,109,1,96,30,19,51,52,16,121,9,91,91,56,22,22,97,90,24,22,48,86,99,52,100,7,19,38,39,80,94,62,68,101,19,52,18,10,37,97,5,124,27,85,107,13,120,99,27,34,60,1,42,112,35,68,98,33,12,25,103,96,40,122,34,23,21,116,4,2,17,75,34,70,64,54,74,80,38,24,58,98,104,45,122,46,89,92,116,119,67,108,16,41,117,39,105,97,37,18,86,4,16,78,35,116,63,104,100,121,107,71,11,21,60,83,5,88,71,82,37,59,74,110,104,64,112,53,100,16,15,7,23,95,80,101,44,25,60,31,72,111,3,29,67,68,123,80,55,90,123,27,119,7,109,67,41,96,115,119,35,95,8,94,83,108,33,69,120,122,88,4,6,20,121,99,124,98,122,54,84,70,49,39,18,69,77,28,74,54,83,111,118,30,39,31,42,109,89,15,95,41,75,72,18,86,67,0,79,29,119,57,30,62,13,46,5,26,42,111,61,1,120,21,13,96,102,92,15,110,11,25,21,4,110,124,24,48,107,78,55,21,5,59,42,53,41,7,97,105,118,51,66,66,42,47,49,56,75,56,106,7,13,48,116,75,18,24,71,56,55,88,31,124,68,67,64,58,60,56,122,39,9,38,46,0,12,75,86,18,30,58,100,116,49,3,37,14,43,58,51,16,27,51,87,63,64,80,22,17,86,124,91,81,1,58,74,24,11,82,54,6,21,19,22,93,106,66,40,84,109,17,81,105,48,0,65,79,107,22,31,107,60,3,122,5,97,114,8,28,99,1,65,54,92,113,97,38,15,37,30,19,52,55,37,27,77,112,83,27,72,107,67,94,113,42,1,29,70,39,78,85,15,46,20,37,42,52,96,121,72,77,79,116,84,82,42,53,76,97,73,45,44,96,9,6,70,101,66,53,63,61,89,120,12,36,115,123,118,31,95,14,8,104,12,60,35,104,97,123,34,32,114,114,102,49,61,90,54,15,77,20,57,40,4,109,16,118,6,55,103,9,36,41,124,24,62,78,87,11,70,22,125,123,93,88,90,123,38,75,98,7,6,38,25,26,105,47,35,102,33,113,42,42,96,102,84,61,61,61,96,101,17,93,93,44,44,99,18,48,13,27,5,48,124,33,41,80,86,28,99,64,95,89,71,10,19,69,2,115,91,115,100,112,60,114,35,9,125,10,93,7,107,47,89,83,34,54,86,10,30,95,69,47,25,80,124,5,61,106,11,118,63,73,76,44,86,99,10,109,125,76,28,42,19,106,90,34,117,19,46,99,79,106,29,51,68,57,123,58,0,83,15,86,111,38,47,32,74,34,93,83,11,49,22,88,10,109,59,22,83,121,124,77,10,21,106,33,115,70,63,90,124,117,23,76,66,113,102,65,90,6,103,3,108,76,1,2,41,57,30,118,113,15,9,94,100,105,20,114,118,35,115,80,2,100,36,107,124,94,28,36,51,82,67,77,39,61,86,57,61,25,1,94,53,34,118,87,85,36,12,70,124,54,80,29,15,12,117,66,89,67,70,37,44,110,54,4,31,67,9,92,114,36,40,88,3,59,47,120,32,44,34,12,63,44,74,45,95,79,37,18,83,38,43,37,72,81,7,103,107,22,6,101,12,107,94,4,8,111,12,64,74,26,27,42,89,116,56,29,39,59,108,109,5,91,13,11,61,95,14,29,113,36,96,103,84,58,121,109,22,33,3,83,5,35,50,69,29,3,77,60,68,94,48,25,87,99,19,115,47,114,38,77,28,113,88,98,48,11,75,62,101,19,72,38,82,28,109,67,20,78,119,74,88,36,24,45,23,70,99,59,75,17,36,38,60,125,106,83,10,8,57,112,107,14,1,20,32,77,92,75,15,101,90,83,10,77,10,72,96,24,5,10,15,125,34,38,98,48,55,54,6,92,11,107,5,25,1,65,114,84,35,57,112,1,109,124,103,82,13,30,69,46,124,24,46,41,26,113,76,65,104,31,117,107,47,41,10,89,108,75,60,100,57,87,31,7,7,73,32,98,78,45,66,9,113,113,83,102,96,11,16,92,43,115,96,76,20,94,15,47,59,95,78,29,49,81,113,17,122,41,46,20,87,95,109,66,67,38,11,1,32,61,44,91,35,15,44,79,12,115,110,123,43,3,28,88,23,120,116,59,59,33,125,104,75,45,29,60,79,6,56,5,63,114,11,64,13,31,26,71,89,32,54,123,116,109,123,51,27,94,23,93,64,39,114,114,108,44,40,109,125,37,118,85,125,79,102,16,100,99,81,8,90,8,44,122,81,46,68,92,56,79,119,64,38,85,91,62,62,13,92,44,15,8,113,41,7,49,35,16,44,99,85,5,69,125,119,114,67,46,71,114,27,1,9,11,85,78,43,105,95,78,45,79,83,18,75,4,16,36,77,11,104,73,73,93,108,117,89,19,3,100,100,88,49,105,123,92,12,5,63,88,104,50,0,97,88,43,13,47,8,8,15,87,92,7,1,117,93,90,37,69,25,99,5,101,43,47,39,26,34,102,65,112,51,110,69,50,59,103,90,20,78,63,10,27,112,31,0,52,120,44,67,41,28,48,0,68,87,10,20,32,122,94,123,67,102,1,116,31,25,74,113,21,116,55,24,114,81,77,105,2,81,121,53,16,4,0,67,34,83,3,29,107,57,17,86,13,30,25,1,52,30,118,84,111,46,90,64,104,43,84,107,53,73,92,83,112,75,117,13,103,103,66,86,18,49,96,80,12,19,0,95,116,48,121,80,85,116,68,101,29,34,17,106,4,106,9,55,94,45,53,6,92,99,99,125,81,87,36,118,29,34,85,105,29,90,30,54,76,1,29,67,111,101,36,19,125,37,14,86,114,53,118,118,93,56,87,23,38,103,74,52,99,48,64,58,116,29,125,18,123,56,32,62,34,57,97,111,1,70,123,110,89,124,67,21,112,87,12,41,17,119,4,93,117,71,124,30,56,70,50,11,111,62,55,24,70,68,61,31,124,39,46,101,6,65,68,113,14,28,32,36,5,61,28,123,88,35,125,113,43,11,73,56,88,73,30,33,64,15,49,101,76,72,6,12,7,51,63,89,49,67,64,107,47,33,7,4,69,75,16,12,108,2,113,110,81,79,43,51,15,93,28,105,65,18,81,72,76,4,40,12,11,91,98,24,45,84,15,25,7,59,121,125,27,3,76,99,99,117,68,86,5,37,40,92,47,41,65,70,117,105,108,55,124,114,4,94,96,73,2,53,93,7,28,50,11,81,100,87,99,108,71,29,68,89,67,75,37,97,5,26,8,10,50,96,77,33,84,97,110,98,52,41,56,81,86,13,41,116,95,31,4,119,63,27,109,16,111,19,79,106,106,43,116,1,88,10,25,48,98,16,38,15,99,49,68,59,111,74,18,102,65,66,100,109,68,87,4,102,15,9,82,111,94,107,86,76,91,120,52,99,93,31,19,113,25,57,23,102,13,9,69,54,13,4,89,104,29,63,32,39,29,90,6,49,119,52,125,62,46,45,51,54,14,113,19,23,19,111,26,38,84,91,72,80,108,7,108,96,75,38,4,46,85,24,33,118,8,116,48,40,108,68,110,95,63,108,72,10,62,125,37,4,124,124,23,45,19,6,94,54,77,13,106,79,105,124,16,44,94,60,88,47,28,65,89,3,64,117,43,65,15,10,100,113,114,65,23,82,27,106,73,73,77,16,101,54,2,16,121,102,106,125,118,12,33,123,87,61,122,13,84,39,29,97,71,10,113,12,17,22,5,8,2,100,22,105,39,22,119,93,9,5,39,15,100,106,27,8,54,65,97,6,0,71,108,107,109,32,37,78,125,54,84,90,5,71,5,29,82,24,59,114,25,15,49,38,94,40,101,75,23,25,60,26,117,20,93,29,125,81,96,7,74,91,112,99,66,1,43,92,93,54,2,89,18,58,46,95,74,59,106,83,13,59,122,7,87,35,87,80,24,81,7,38,27,18,31,76,62,31,11,114,70,60,109,17,22,47,18,114,92,37,92,19,12,104,94,36,20,76,115,17,14,30,73,20,92,17,100,118,21,113,28,25,91,118,51,65,91,87,24,38,64,101,105,121,125,20,70,13,9,44,117,22,77,112,73,36,72,61,29,68,69,61,73,9,75,4,49,82,87,90,65,107,64,54,115,15,121,56,67,71,40,38,33,9,44,81,67,120,22,26,43,94,18,15,83,21,6,113,9,122,43,37,92,118,85,75,85,112,97,95,82,26,80,21,96,96,108,124,105,45,1,31,78,32,57,43,95,46,1,62,125,1,122,44,21,7,67,122,113,86,89,110,85,60,96,72,53,125,41,23,56,91,120,75,97,3,6,59,11,52,88,64,56,121,87,92,43,90,124,105,46,8,38,44,92,51,84,119,67,14,122,123,60,99,66,64,119,17,107,72,106,125,65,70,84,43,111,32,49,120,10,31,121,65,95,91,119,84,124,24,14,93,37,45,84,57,44,13,26,15,37,97,16,74,43,96,74,7,65,78,96,30,29,43,111,95,23,56,56,46,59,51,6,5,3,0,120,69,59,119,121,55,94,76,50,104,110,107,90,73,68,21,3,79,89,109,89,96,102,70,99,15,87,26,44,6,97,85,119,122,91,83,20,31,27,54,83,91,38,3,53,28,108,121,105,107,82,22,53,27,17,79,23,109,80,107,55,100,74,36,76,82,42,102,125,104,6,88,44,59,29,30,0,78,68,79,84,108,50,89,123,37,10,21,89,114,61,12,112,42,103,55,30,120,122,68,86,84,120,41,86,123,61,39,101,111,110,94,74,64,48,89,110,32,50,96,68,110,47,93,27,94,3,26,119,8,121,11,11,117,47,71,53,105,51,15,125,23,81,93,51,61,11,82,9,106,52,121,2,87,98,55,34,107,53,52,85,43,11,65,120,0,97,61,59,77,61,84,43,109,52,6,23,79,12,69,46,20,113,16,67,42,117,36,84,75,2,114,77,12,14,34,96,21,109,65,102,22,65,109,90,21,101,82,2,103,34,32,80,16,55,17,30,93,46,75,124,47,2,37,83,14,56,105,28,122,31,41,75,89,122,5,13,47,53,69,61,9,31,122,87,14,28,109,125,70,40,87,63,20,28,59,44,115,67,11,121,108,105,40,48,36,81,93,108,41,81,105,48,115,85,89,106,37,25,15,91,87,31,41,98,8,14,12,10,87,33,99,22,74,44,6,93,48,76,86,28,4,118,112,93,92,108,91,121,85,117,73,59,37,26,118,31,67,84,40,85,96,77,109,56,92,123,33,42,123,123,63,24,91,67,42,16,112,52,67,15,41,108,105,5,35,98,105,123,15,107,13,98,24,4,102,27,52,84,90,95,42,94,89,6,90,27,51,21,101,123,47,76,24,71,2,41,96,31,1,78,22,72,64,65,95,9,17,31,15,125,40,118,103,24,30,100,90,123,35,59,107,5,77,7,59,106,123,21,78,93,38,72,57,113,58,88,98,120,55,37,78,43,83,122,71,94,12,111,49,95,73,58,64,13,47,88,112,2,66,41,72,42,30,99,113,24,76,39,27,101,94,103,113,90,68,24,94,101,46,80,27,71,46,31,12,54,80,99,125,27,108,67,40,88,70,11,31,95,114,121,122,105,119,69,16,84,35,33,73,13,73,64,58,114,60,33,50,97,121,107,84,85,52,22,4,44,27,11,77,49,88,33,107,9,35,107,57,56,57,20,18,43,24,122,80,39,34,82,73,31,73,34,17,90,43,98,116,63,66,77,69,119,104,95,14,55,49,37,78,63,25,10,41,37,6,78,106,96,40,120,117,79,54,20,120,123,122,81,18,32,70,71,55,65,87,45,54,123,9,118,98,22,88,56,101,78,91,15,25,124,70,34,26,6,105,14,117,120,104,69,87,61,119,84,58,70,3,49,32,8,32,39,119,21,15,123,58,6,57,87,12,14,109,111,46,119,11,95,37,40,123,80,57,47,10,56,76,124,19,1,19,9,89,0,40,10,105,42,88,94,47,99,57,28,85,20,119,111,86,72,32,1,36,4,77,50,110,0,8,19,77,42,95,59,27,75,80,111,68,62,50,110,40,69,87,32,37,30,24,123,123,82,80,79,5,75,17,102,37,19,94,106,26,13,55,120,71,7,33,38,99,40,108,103,11,81,65,117,123,59,51,16,118,122,47,44,19,22,55,66,61,59,27,27,117,52,116,26,30,38,23,22,93,65,100,116,88,47,35,117,27,52,48,41,48,106,51,122,52,9,106,108,33,83,87,81,8,24,58,116,50,121,124,69,101,29,125,90,70,105,54,34,86,64,83,64,22,39,13,33,87,108,100,97,116,12,101,103,60,80,30,107,53,58,86,54,111,90,67,59,102,49,65,26,18,69,93,35,121,46,46,1,53,91,50,55,17,36,55,16,15,20,125,17,85,79,14,41,50,62,14,35,41,49,70,66,7,77,26,100,108,39,45,67,73,33,41,79,16,30,71,57,102,81,54,21,75,90,7,24,42,104,48,117,50,90,8,95,86,76,16,51,73,79,124,8,45,106,4,123,43,2,54,52,42,19,6,56,88,3,88,16,15,100,66,66,65,88,58,46,48,11,75,24,4,50,19,59,35,74,0,115,47,62,42,106,97,44,58,11,36,66,62,20,104,66,43,95,49,121,120,72,112,98,115,57,48,85,13,58,4,21,86,39,101,21,5,29,19,6,81,114,2,4,124,11,97,53,21,50,110,108,124,52,31,97,51,107,98,86,14,82,60,39,68,33,60,79,3,107,58,60,104,120,123,78,86,100,112,68,3,41,40,38,71,44,47,71,66,121,31,73,76,34,56,58,11,38,15,0,37,28,63,119,35,45,72,71,93,41,39,75,9,99,49,15,85,38,83,25,20,88,73,37,50,72,0,117,65,15,121,68,45,64,51,48,28,92,32,67,6,38,72,95,22,67,43,25,12,43,110,27,96,100,17,34,13,71,105,21,8,57,120,120,36,74,45,78,96,55,45,52,86,85,75,108,122,4,27,79,87,85,52,41,59,14,9,35,47,111,52,75,36,12,21,6,82,26,2,90,64,123,80,74,35,109,66,100,89,52,56,20,78,57,85,95,63,70,29,79,19,98,66,47,104,66,84,121,2,15,53,88,18,14,35,95,112,69,43,105,38,42,100,60,29,88,43,29,3,102,45,87,60,48,19,78,31,68,83,92,117,24,101,76,32,107,83,69,25,32,18,94,19,36,63,93,23,112,21,118,83,119,19,77,67,54,112,37,13,73,91,93,43,61,44,38,45,63,52,113,106,90,19,81,30,25,42,108,101,3,74,6,15,71,86,67,65,92,67,21,95,46,47,84,56,22,22,64,14,80,6,93,123,96,94,71,0,36,91,30,26,29,123,117,4,87,104,74,46,120,72,42,92,51,79,34,10,101,116,71,69,15,34,125,10,112,16,121,59,35,100,52,79,104,98,15,50,55,12,54,81,44,80,53,43,106,88,37,71,46,33,122,23,90,106,118,2,93,62,6,63,118,76,54,22,13,16,71,117,10,25,108,55,1,78,82,99,20,47,16,24,79,68,41,35,54,52,110,92,38,112,38,40,96,4,13,7,14,78,116,93,55,105,21,70,58,17,111,87,23,51,4,7,49,119,2,53,67,48,99,104,36,103,106,59,20,103,65,92,12,101,24,15,100,114,25,124,74,118,17,87,6,1,60,48,23,89,72,93,9,55,26,51,87,84,125,59,57,35,76,124,107,14,117,23,81,13,117,58,103,107,29,68,114,85,71,33,14,57,25,29,62,120,117,49,115,68,65,85,104,105,74,66,56,47,54,12,31,43,18,100,48,106,116,72,5,2,3,80,65,122,66,46,78,54,35,76,21,107,24,121,36,92,37,111,73,120,124,43,116,42,25,54,96,75,45,1,124,32,89,82,38,60,54,80,4,36,3,122,120,83,75,34,55,25,74,4,80,34,107,53,85,73,105,14,119,77,119,34,82,37,42,22,9,102,50,121,118,61,26,97,110,51,113,96,106,111,125,10,44,25,0,37,46,54,50,79,26,10,46,54,39,16,98,57,28,47,31,67,50,77,97,57,108,59,94,2,88,117,21,113,96,55,110,29,73,59,96,28,31,102,7,116,15,9,37,69,54,15,24,66,41,76,67,48,12,109,44,53,52,84,50,52,91,99,23,43,3,44,40,10,107,29,39,58,73,114,7,93,29,31,64,32,70,94,49,32,105,18,17,53,32,26,104,61,55,86,121,27,72,68,20,47,9,124,103,114,57,46,101,114,31,75,21,66,92,100,54,14,99,97,66,101,52,50,117,0,52,8,20,27,107,45,120,6,124,87,54,25,20,114,114,60,86,72,46,41,21,95,12,60,113,15,10,121,66,96,52,50,57,107,104,36,93,100,21,2,39,123,90,82,77,5,115,4,7,75,4,38,107,94,69,53,77,23,113,21,88,82,55,46,107,48,118,118,64,72,41,55,11,75,77,102,60,98,67,103,47,20,57,33,119,49,107,111,60,86,109,18,25,7,111,81,33,85,35,91,97,114,89,77,23,6,66,25,42,45,81,0,74,17,51,124,2,20,54,72,79,117,79,103,17,122,28,51,114,114,60,108,111,82,65,60,48,124,119,102,73,77,107,11,93,14,104,114,4,63,87,24,107,13,17,57,0,117,72,92,6,14,105,125,22,1,119,66,116,120,75,70,84,114,125,66,60,102,88,0,78,68,79,79,17,122,70,18,10,95,34,110,11,26,109,62,61,33,48,67,15,9,99,46,123,36,3,38,100,7,68,16,2,104,64,121,104,37,20,65,90,94,40,65,73,76,116,81,2,1,0,82,22,9,67,31,34,100,112,21,77,79,75,32,47,98,18,56,4,27,117,93,48,16,84,65,53,88,54,41,34,44,15,39,105,118,125,21,2,6,80,8,2,0,95,70,38,42,88,125,56,59,91,63,56,70,37,93,20,103,33,17,114,2,105,60,69,10,77,88,123,89,41,10,46,81,115,58,76,15,21,119,58,59,77,2,97,8,79,91,34,98,36,116,38,0,2,38,53,1,0,28,24,113,93,28,42,9,53,34,108,48,61,36,41,112,51,79,26,58,110,67,42,56,65,36,79,60,39,102,32,38,115,72,60,93,81,113,122,121,53,108,98,47,29,65,106,51,68,37,72,74,56,103,89,71,108,88,114,100,93,3,36,110,37,27,18,64,40,77,96,15,38,14,46,118,79,77,89,14,9,23,78,81,22,44,0,111,119,51,14,18,96,18,14,89,121,53,10,33,70,71,72,120,33,71,46,109,111,121,15,68,71,10,106,77,9,15,73,47,88,54,1,20,63,120,110,7,26,56,102,23,88,13,91,119,24,58,81,9,1,46,99,96,81,24,122,57,0,119,12,106,36,67,109,98,117,117,4,28,55,69,53,37,18,80,88,42,23,103,45,32,35,120,75,87,103,39,39,40,4,121,50,81,100,72,44,113,58,0,58,120,23,101,10,69,5,39,48,20,121,70,24,107,35,85,55,10,81,122,80,109,23,94,7,36,64,52,7,90,71,30,52,38,89,0,36,101,92,97,45,113,20,11,87,76,29,86,100,68,82,29,56,29,101,107,63,24,72,70,30,79,44,45,66,101,73,23,97,27,62,64,125,87,40,55,102,80,41,124,36,39,120,65,22,37,45,83,13,53,86,86,29,0,0,17,72,53,0,87,65,115,122,6,64,76,123,92,60,3,106,35,45,12,35,40,118,69,115,118,5,112,1,60,125,60,100,103,7,107,64,47,125,92,100,53,37,77,32,77,102,117,2,92,108,45,121,29,14,83,105,3,75,7,58,18,33,9,27,46,61,37,120,77,36,118,33,15,69,10,43,7,122,79,114,95,46,125,63,22,5,59,36,93,123,73,99,45,30,73,5,95,120,59,37,96,41,30,92,66,114,80,59,4,47,34,107,31,30,121,24,51,102,63,103,59,73,90,112,50,97,41,76,8,124,60,47,15,116,10,78,111,4,95,58,77,101,55,52,113,78,52,120,80,65,83,62,103,0,27,49,71,73,72,12,78,71,31,11,13,98,0,63,7,112,79,44,27,9,82,68,117,40,45,18,45,89,59,14,72,17,26,109,82,110,24,43,36,110,25,32,34,92,101,110,9,40,15,84,28,26,76,90,35,10,25,110,60,34,50,13,42,118,22,110,97,83,125,51,45,99,40,42,51,40,64,15,75,41,8,13,95,96,29,56,93,103,76,57,79,14,115,86,51,13,68,111,43,56,28,123,50,13,68,35,21,77,86,23,12,119,42,47,99,85,107,82,27,39,85,17,6,101,124,67,12,25,42,0,14,98,41,119,101,43,7,114,28,38,55,42,54,85,48,39,105,53,51,108,87,90,98,95,42,59,115,53,75,63,75,83,108,93,13,23,13,62,38,17,73,89,95,53,41,35,54,23,97,15,36,74,66,18,102,62,96,32,25,10,14,59,7,96,16,69,44,80,21,0,119,85,77,24,108,13,88,99,75,4,114,123,62,41,99,1,44,117,68,60,65,81,52,66,40,112,11,87,93,36,82,122,36,6,66,22,91,40,51,90,24,39,98,68,47,3,65,73,81,72,51,3,56,86,48,76,123,35,8,22,63,68,77,125,124,30,37,13,115,4,7,52,111,37,63,123,56,36,87,1,91,4,105,27,75,57,100,37,90,113,75,57,66,12,118,34,42,0,101,124,123,2,88,34,48,0,41,81,37,60,123,103,123,107,22,124,94,9,100,46,83,51,70,70,27,25,42,8,50,122,113,83,116,9,101,9,77,10,61,79,99,90,48,19,93,95,19,52,9,84,55,74,67,75,119,58,65,125,13,47,51,53,113,45,17,107,10,76,80,117,124,25,75,98,119,64,95,31,63,19,113,108,97,77,32,94,43,11,2,98,18,56,15,2,40,62,56,51,47,15,36,31,125,84,78,75,1,115,107,88,108,12,100,17,76,109,115,58,71,54,14,97,18,69,121,4,44,15,103,34,88,11,39,48,55,110,21,14,18,92,102,54,67,18,53,14,17,30,96,118,73,98,119,119,27,52,96,123,42,14,37,24,77,120,71,9,84,26,41,49,4,118,50,74,104,13,85,107,121,3,50,78,102,8,89,107,75,108,99,109,15,94,0,23,55,48,118,4,85,124,72,15,97,22,63,12,117,17,86,23,121,25,97,115,51,59,49,64,105,23,115,19,105,24,58,35,9,47,23,45,92,13,25,59,73,37,31,62,120,73,41,10,39,68,114,27,120,25,79,80,120,95,56,89,21,40,7,61,81,117,28,50,92,3,19,116,99,41,123,47,113,120,124,40,1,42,105,28,18,17,88,10,80,0,48,87,18,111,24,112,13,105,104,49,67,111,11,35,3,35,4,47,29,75,25,105,74,41,86,87,21,41,103,20,55,102,42,103,62,51,3,74,113,99,56,65,97,75,103,25,121,89,46,103,7,115,78,19,43,78,64,117,25,45,53,34,86,66,105,36,98,84,69,66,67,14,9,21,26,93,80,34,104,96,80,59,101,122,7,96,69,103,63,96,81,69,0,111,52,78,120,22,58,42,101,23,76,45,109,44,44,100,31,65,76,15,113,88,44,121,4,23,37,23,103,47,102,87,91,84,92,77,68,122,63,66,77,35,21,39,107,100,27,113,75,89,65,34,75,110,42,58,36,45,48,23,89,81,71,44,26,108,69,43,83,27,125,95,88,13,24,78,2,48,34,91,97,95,18,100,78,74,121,19,78,28,24,112,39,119,37,53,96,120,18,75,90,19,61,12,26,119,41,49,61,26,27,39,62,121,18,36,101,54,48,80,53,1,4,97,111,77,60,1,62,110,32,90,121,64,96,82,1,93,41,116,101,55,92,104,40,60,117,52,75,57,31,59,52,102,39,74,83,111,69,116,53,9,42,19,104,20,58,49,15,77,101,81,73,47,84,86,106,23,101,23,72,114,112,50,41,58,78,100,67,40,3,105,31,95,11,113,50,6,45,67,102,56,26,104,88,62,11,115,62,119,99,66,62,92,75,12,82,52,85,16,9,85,36,63,14,116,30,40,64,101,45,80,70,63,41,121,15,59,111,107,0,93,32,22,93,16,114,3,22,98,64,121,2,82,104,30,66,72,68,0,20,59,0,91,83,16,1,41,58,52,58,68,51,66,108,15,60,9,106,98,100,12,36,68,29,50,80,12,53,4,107,43,109,110,22,51,18,31,24,118,35,96,42,65,80,13,64,28,61,10,8,125,107,33,14,51,9,101,106,81,16,119,37,20,58,81,49,37,102,68,65,27,51,92,105,17,93,11,31,42,17,39,54,55,70,4,2,58,71,62,42,81,114,18,77,118,59,0,113,107,98,119,35,18,115,50,92,58,110,31,38,7,64,47,85,59,54,19,92,66,101,29,10,107,4,115,64,41,55,28,64,34,116,69,48,44,102,72,58,45,18,23,108,8,105,25,86,45,54,88,77,94,62,45,23,99,68,5,114,34,33,115,53,89,39,118,79,96,77,115,15,77,3,63,20,88,117,87,96,113,18,106,77,48,78,26,33,104,102,19,82,109,111,6,76,40,100,88,71,24,42,24,67,87,33,40,62,63,3,98,16,55,40,81,90,59,105,55,25,97,100,87,117,78,22,88,74,61,8,94,112,42,111,59,124,14,118,17,29,72,64,80,60,18,115,112,64,57,94,39,47,107,104,69,93,80,12,101,21,21,121,62,92,29,17,97,49,104,10,74,29,2,44,7,40,18,7,8,2,23,118,90,28,20,96,112,114,9,24,21,20,57,58,51,34,40,36,16,105,119,113,16,87,68,22,16,82,12,80,78,79,25,43,91,93,27,117,115,68,90,71,106,75,59,46,118,48,1,75,96,73,104,5,31,32,108,7,37,85,32,30,61,39,40,119,100,45,17,14,84,37,97,51,90,94,46,66,11,83,48,104,99,105,35,41,75,57,98,0,1,94,93,73,3,50,48,27,96,34,77,42,55,40,87,66,39,12,46,79,37,85,40,113,97,34,43,79,41,43,39,25,38,21,110,86,111,59,92,5,83,56,93,26,30,105,4,116,33,53,62,45,26,125,59,39,113,105,81,50,36,104,52,46,116,122,28,23,18,7,75,99,65,56,13,110,96,50,114,64,95,37,68,34,81,0,2,8,83,20,124,40,88,7,8,29,110,36,41,12,64,67,23,54,94,8,83,60,52,100,32,9,107,17,87,12,16,1,19,106,1,109,2,10,84,17,83,2,92,82,74,11,64,33,85,3,104,102,46,118,17,70,74,8,38,118,1,28,80,124,105,15,100,68,68,92,60,32,44,11,110,17,41,122,72,66,15,77,47,109,12,88,112,117,55,121,37,80,4,86,44,30,120,30,31,4,34,116,33,43,59,64,99,50,40,60,72,95,97,10,95,12,75,117,46,61,70,79,19,43,53,109,90,5,73,102,117,40,25,4,48,111,20,81,34,25,35,33,104,120,95,73,119,122,122,111,112,57,35,65,96,28,17,28,70,103,13,100,75,16,99,68,46,18,114,65,54,81,16,30,125,5,110,34,122,121,101,106,24,125,113,99,4,59,107,112,81,72,65,6,78,6,106,18,56,88,3,26,13,42,102,83,12,86,97,102,70,23,76,50,64,120,3,86,61,82,81,98,8,101,77,41,81,106,122,66,57,124,55,8,46,85,82,16,11,97,63,19,79,82,82,42,24,54,2,44,48,18,62,69,86,7,89,57,45,107,122,69,119,41,85,76,92,78,69,19,118,36,57,59,73,103,96,101,45,105,31,31,105,17,83,23,64,104,67,123,13,46,50,3,24,81,93,115,36,66,67,100,98,101,88,84,4,84,37,107,107,86,98,63,92,35,25,103,42,42,34,35,34,66,39,104,98,56,109,100,53,16,89,10,22,48,70,37,33,21,103,56,101,7,115,81,12,85,6,78,46,56,64,31,22,114,16,93,81,109,119,13,45,14,124,66,3,21,83,75,67,34,34,31,119,55,88,26,11,43,83,123,41,15,18,4,4,36,80,24,111,82,36,84,96,102,125,51,110,114,15,44,110,55,66,63,51,125,16,54,91,24,41,125,98,61,102,81,46,53,74,58,18,117,66,38,47,25,118,120,4,55,119,78,65,67,60,59,116,108,96,46,47,125,78,124,98,61,115,104,50,73,34,70,66,98,87,3,17,103,58,66,41,64,50,89,110,28,68,110,123,6,76,117,91,90,99,80,112,78,52,89,117,60,121,82,44,112,22,68,50,104,17,83,93,53,121,92,56,22,43,67,45,38,117,6,124,89,39,16,26,93,66,99,3,70,98,7,78,23,82,54,21,14,71,84,41,8,109,66,117,120,35,18,17,76,23,67,14,32,41,97,100,24,105,0,114,8,64,64,60,14,107,77,13,107,101,105,100,96,101,109,61,94,102,112,8,14,120,13,15,53,10,78,120,33,25,53,37,99,61,100,103,65,18,23,93,103,96,9,61,91,47,0,77,98,110,6,87,66,79,9,32,27,35,9,19,75,57,102,117,10,13,26,64,97,15,11,115,32,113,70,14,53,53,103,78,99,78,119,113,72,99,110,99,96,111,29,97,121,74,54,84,59,125,75,71,109,62,14,48,22,57,62,29,105,23,55,98,96,44,98,33,65,49,92,70,39,82,71,86,1,58,66,78,119,75,4,118,89,58,37,95,19,60,79,59,42,61,83,71,6,57,9,30,62,87,90,22,95,70,0,106,99,119,61,83,20,55,50,79,96,102,47,2,78,10,28,108,93,34,21,53,86,7,2,118,89,107,85,19,124,50,8,69,41,58,118,18,99,29,3,120,74,10,115,24,117,51,122,81,85,54,10,73,71,56,96,86,111,57,79,58,73,72,107,63,101,2,25,14,42,34,117,69,115,41,15,81,88,12,114,120,40,107,52,67,119,75,1,113,102,68,24,58,84,2,120,31,9,94,53,98,93,77,28,82,115,9,56,34,55,54,24,24,97,115,76,113,93,109,44,53,106,15,15,12,72,24,7,99,62,73,33,124,82,43,99,51,105,78,113,25,82,52,103,45,116,29,92,47,103,86,6,1,62,51,40,30,86,95,21,124,34,24,78,110,54,50,86,122,102,104,122,113,0,62,23,10,107,10,84,104,30,122,91,83,112,113,98,25,63,98,109,84,85,116,93,3,104,83,55,81,99,32,9,22,68,79,63,113,23,50,78,69,6,120,46,85,37,34,7,118,52,60,77,30,64,64,87,64,90,90,124,119,123,22,40,46,53,114,6,58,47,42,102,70,70,18,1,35,25,97,48,69,36,121,14,38,68,69,47,114,99,81,116,14,28,66,5,79,64,87,7,98,14,105,22,62,78,94,86,59,98,87,98,0,108,52,11,5,120,53,117,77,48,25,41,46,40,28,92,84,60,56,99,76,88,22,90,62,53,122,69,84,36,91,69,71,58,1,35,79,99,91,33,106,76,9,9,34,89,65,40,123,74,26,101,38,125,89,39,13,19,36,36,32,117,21,62,63,51,81,78,103,77,4,90,62,55,97,3,21,44,60,32,2,87,48,16,44,63,81,79,65,16,5,29,83,43,68,66,58,80,35,85,88,54,117,46,69,31,16,94,42,120,60,27,46,122,22,117,115,76,1,113,8,48,105,65,106,105,74,110,35,120,49,124,60,94,85,119,68,103,9,32,119,106,89,53,33,34,28,82,4,37,9,84,92,85,9,97,84,76,43,124,12,43,94,83,112,57,65,38,20,23,42,86,74,109,66,103,96,8,88,55,43,2,53,87,115,78,122,22,61,114,102,71,69,32,51,90,36,90,27,99,78,35,23,60,21,40,37,55,47,55,110,58,19,41,20,84,76,75,116,6,73,107,65,117,74,9,115,96,13,17,57,42,102,125,75,46,43,75,97,95,106,54,90,3,68,15,84,115,106,18,57,8,75,26,42,110,83,122,74,3,60,75,71,4,27,92,118,90,22,71,88,103,40,43,71,5,45,73,112,32,21,123,64,55,80,84,3,94,54,49,86,19,117,94,82,103,45,125,4,115,124,41,26,121,114,74,117,18,103,30,87,58,22,28,79,41,123,64,47,26,12,18,114,74,21,39,110,81,58,87,68,63,89,4,119,45,60,104,0,107,7,6,124,35,94,107,102,122,80,71,76,26,63,97,19,92,80,113,114,114,86,114,112,29,70,106,23,65,8,24,43,114,39,106,86,116,95,67,3,76,49,63,99,94,26,119,117,72,63,27,11,21,34,82,107,38,30,106,58,125,96,77,124,93,4,89,17,55,65,27,63,50,70,76,2,69,12,118,50,50,100,18,111,6,75,1,92,45,32,48,85,115,91,88,82,37,115,72,23,115,15,42,11,85,115,120,54,39,3,40,120,54,105,45,77,64,12,44,94,16,87,115,7,15,42,34,18,82,55,96,32,7,96,108,112,14,105,73,115,119,44,61,104,118,116,77,73,82,107,62,55,102,14,113,75,75,21,114,122,29,108,21,38,123,50,20,109,44,63,3,10,92,71,32,16,88,95,68,81,41,61,27,38,93,101,109,115,97,112,60,92,34,20,36,67,12,59,37,63,18,32,101,48,35,43,11,34,10,114,62,80,59,112,29,8,43,1,122,116,94,121,50,43,17,64,37,6,103,18,94,63,81,64,63,67,27,43,26,64,17,0,46,70,11,63,118,38,59,112,108,45,60,38,26,30,20,38,50,13,48,124,63,15,119,50,92,36,118,72,82,29,31,14,67,23,97,64,98,78,20,106,28,116,113,111,96,90,11,38,29,27,21,32,48,101,102,63,0,99,82,81,85,5,66,57,67,10,27,45,63,65,44,69,70,85,15,77,87,53,95,8,28,123,18,34,89,108,62,52,99,23,35,82,5,111,88,13,11,34,46,75,98,103,6,24,11,103,30,45,125,79,67,53,110,124,73,101,114,40,36,85,113,98,87,72,119,34,12,38,35,57,84,24,109,56,80,29,122,88,103,44,34,66,98,89,27,110,101,120,125,14,30,64,80,78,124,12,66,55,51,82,66,81,19,55,46,54,14,76,80,89,120,10,5,108,64,106,15,123,68,89,25,115,71,3,120,20,78,69,27,17,105,121,123,10,109,23,77,57,100,48,67,110,90,61,54,52,105,67,44,119,105,69,26,40,34,70,97,1,48,88,119,10,100,1,1,31,45,19,59,71,74,115,2,16,7,9,109,8,87,16,99,124,100,37,113,110,51,10,64,36,17,105,33,14,117,113,34,24,47,71,107,11,55,86,75,50,25,118,61,64,41,83,56,8,47,48,103,44,15,30,31,59,104,77,14,69,36,12,25,39,84,30,54,23,111,80,4,39,58,116,39,27,1,49,71,21,114,80,118,93,12,80,81,47,125,38,83,30,71,0,80,55,90,95,52,33,119,44,89,8,82,38,47,41,120,108,123,51,64,59,4,9,118,123,80,95,75,29,58,121,44,76,76,36,4,106,65,31,66,89,85,118,96,95,53,59,23,13,124,40,116,35,102,87,105,119,70,32,69,36,64,23,72,54,83,99,113,96,19,90,19,9,81,90,80,21,0,17,85,8,7,68,16,98,77,17,114,109,120,97,83,42,112,98,76,123,106,39,114,58,92,90,85,36,112,5,37,102,125,4,106,57,94,55,42,64,102,46,11,65,38,118,35,11,58,55,106,20,100,86,4,1,106,4,37,42,2,95,108,65,64,62,114,14,77,17,13,28,102,108,123,69,47,81,101,118,31,85,113,1,6,59,23,75,10,85,117,92,43,59,9,48,90,74,5,96,86,23,79,86,27,26,20,25,113,77,53,86,62,17,52,116,38,22,55,16,104,117,30,44,78,115,37,66,35,82,26,107,93,114,61,27,19,110,3,47,90,40,33,119,37,69,74,34,125,68,45,79,102,48,40,74,12,108,55,59,3,54,35,118,109,47,21,104,29,20,66,107,91,2,98,29,16,32,89,76,73,41,79,103,71,56,114,0,70,49,52,19,99,12,104,123,61,27,96,32,8,18,20,35,19,2,70,76,42,31,109,44,84,78,101,93,25,37,22,46,1,100,67,89,61,76,48,95,56,123,5,38,42,123,37,0,10,2,38,86,57,35,59,118,112,73,53,2,33,56,27,6,58,7,101,18,54,92,77,57,15,121,32,92,2,123,40,95,30,18,60,58,78,1,92,91,70,29,71,121,40,113,99,65,123,69,51,48,47,86,114,21,49,114,122,25,115,66,112,31,33,111,19,124,104,74,45,51,123,60,115,59,125,121,22,66,119,74,14,119,68,13,46,77,81,123,6,107,104,6,39,11,87,109,78,17,50,94,28,106,6,88,110,70,71,68,62,84,43,43,39,98,0,35,115,42,99,56,34,95,0,16,21,97,31,125,39,95,11,71,114,25,80,47,59,41,98,91,44,43,74,95,1,74,62,76,107,30,71,93,118,95,116,78,50,111,22,48,61,65,69,58,0,48,45,68,84,94,121,3,63,49,82,44,51,122,75,75,99,33,100,110,4,51,0,63,91,121,38,86,30,77,51,6,106,71,91,50,84,37,98,45,6,67,120,89,102,72,76,107,47,113,121,31,41,77,22,86,68,30,97,75,27,85,14,63,46,84,125,88,31,50,60,7,19,99,108,121,102,57,123,84,4,76,107,96,0,32,75,62,1,53,35,80,21,0,113,47,56,38,78,23,19,35,50,4,44,14,56,100,79,62,110,15,10,43,16,8,0,67,117,41,73,103,66,102,115,89,35,2,16,38,73,22,27,77,94,20,110,37,44,120,71,120,78,105,85,56,49,111,28,110,78,17,27,116,93,96,5,22,32,95,90,75,75,75,57,67,105,90,57,27,17,78,91,67,121,37,124,64,100,65,36,28,101,92,2,47,86,28,78,34,42,124,101,23,87,125,105,3,66,2,67,42,5,75,123,97,118,115,125,25,88,18,19,125,63,68,8,55,90,32,19,122,60,118,12,115,86,116,98,45,19,104,57,122,61,61,105,4,26,109,105,49,64,37,81,70,1,73,32,98,7,103,9,21,38,35,101,26,97,22,20,103,29,59,27,102,4,107,73,2,75,80,77,3,74,68,123,77,111,6,101,62,119,10,93,23,85,86,70,77,115,114,1,46,44,50,40,106,19,113,100,19,34,103,101,3,109,122,57,109,100,79,97,13,112,28,110,73,45,72,5,111,75,58,21,72,66,13,58,110,20,21,4,92,64,20,85,61,6,13,25,117,41,94,74,11,124,13,121,3,66,18,101,81,79,67,91,65,17,117,6,52,109,111,40,80,67,62,104,50,125,36,32,12,86,74,35,31,79,122,55,58,68,80,5,78,116,11,123,83,25,55,52,17,6,117,32,57,18,39,79,36,93,94,81,21,9,125,12,79,89,35,1,122,13,0,40,83,60,54,113,120,114,37,94,19,34,43,15,7,2,66,9,32,117,77,71,101,8,42,24,120,48,109,9,10,93,15,95,22,98,59,46,24,96,95,26,45,19,110,84,115,90,89,11,0,28,9,41,72,11,80,58,18,30,115,102,57,113,83,119,48,9,70,61,80,118,78,47,93,92,117,15,125,74,88,17,12,104,49,4,27,101,33,32,103,17,30,0,93,56,90,38,11,24,120,51,11,73,10,59,11,105,110,33,120,82,113,87,76,62,28,80,11,27,95,58,67,19,116,115,75,59,41,42,12,0,113,80,60,46,85,30,92,82,24,103,91,77,38,85,22,89,74,15,62,112,120,109,59,115,48,21,108,113,91,84,120,10,23,36,31,48,75,38,120,15,100,108,19,39,41,23,95,33,77,67,52,29,68,54,18,63,88,47,18,110,44,22,35,3,86,8,109,95,66,64,81,11,69,91,5,105,95,100,39,78,117,103,99,30,113,109,18,19,39,58,101,71,1,43,80,44,117,82,39,5,26,42,38,68,45,49,1,9,101,31,116,63,104,89,99,116,124,72,54,26,0,54,19,12,28,102,37,20,37,79,54,54,97,107,32,73,78,76,5,13,58,107,7,73,95,85,37,49,4,61,99,82,75,20,3,30,85,120,110,28,90,1,71,90,53,74,43,63,29,5,93,113,93,20,108,21,82,14,81,51,44,21,120,97,9,27,9,31,108,62,23,10,105,36,55,6,43,124,3,109,48,78,36,0,124,109,120,37,92,106,92,46,61,10,85,77,47,66,64,102,8,108,35,71,61,26,92,79,96,69,13,23,97,117,90,66,80,94,68,40,77,57,50,115,78,101,112,51,63,37,116,46,73,4,49,88,1,2,58,32,80,74,60,104,40,55,123,79,32,113,48,43,29,99,57,103,64,85,123,17,64,29,81,101,115,56,18,24,27,35,103,60,31,109,52,110,14,12,65,86,51,45,7,32,43,41,11,25,75,61,69,119,77,81,112,106,72,63,19,69,108,38,50,17,58,63,9,4,5,119,41,99,11,79,71,48,51,104,43,15,14,69,1,33,91,122,35,117,37,23,124,94,11,7,97,98,39,70,119,51,29,43,33,61,28,94,29,119,59,75,107,9,115,2,28,25,78,15,74,49,29,97,99,42]))
