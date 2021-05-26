# def solution(n, lost, reserve):
#     answer = 0
#     people = [i for i in range(1, n + 1)]
#     for i in people:
#         if i in reserve:
#             answer += 1
#             pass
#         else:
#             if (i - 1 or i + 1) in reserve:
#                 answer += 1
#                 pass
#             else:
#                 pass
#     return answer
#
# if __name__ == '__main__':
#     n = 5
#     lost = [2,4]
#     reserve = [3]
#     print(solution(n,lost, reserve))

# answer = 0
# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]
#
# people = [i for i in range(1,n+1)]
# for i in people:
#     if i in reserve:
#         answer += 1
#         pass
#     else:
#         if (i-1 or i+1) in reserve:
#             answer += 1
#             pass
#         else:
#             pass
# print(answer)
#
# answer = len(people) - len(lost)
# for i in lost:
#     before = i-1
#     after = i+1
#     if before in reserve:
#         answer += 1
#         reserve.remove(before)
#     elif after in reserve:
#         answer += 1
#         reserve.remove(after)
#     else:
#         pass
#
# print(answer)


# def solution(n, lost, reserve):
#     people = [i for i in range(1, n + 1)]
#     answer = len(people) - len(lost)
#     for i in lost:
#         before = i - 1
#         after = i + 1
#         if before in reserve:
#             answer += 1
#             reserve.remove(before)
#         elif after in reserve:
#             answer += 1
#             reserve.remove(after)
#         else:
#             pass
#     return answer


# def solution(n, lost, reserve):
#     people = [i for i in range(1, n + 1)]
#     answer = len(people) - len(set(lost) - set(reserve))
#     for i in lost:
#         before = i - 1
#         after = i + 1
#
#         if i in reserve:
#             reserve.remove(i)
#         elif before in reserve:
#             answer += 1
#             reserve.remove(before)
#         elif after in reserve:
#             answer += 1
#             reserve.remove(after)
#         else:
#             pass
#     return answer
# if __name__ == '__main__':
#     n = 5
#     lost = [2,3,4]
#     reserve = [1,3,5]
#     print(solution(n,lost, reserve))


def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost:
            answer += 1
        else:
            if i in reserve:
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost:
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer

if __name__ == '__main__':
    n = 5
    lost = [2,3,4]
    reserve = [1,3,5]
    print(solution(n,lost, reserve))