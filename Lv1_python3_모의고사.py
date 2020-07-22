def solution(answers):

    answer = []
    tester1 = []
    tester2 = []
    tester3 = []
    score_testers = [0, 0, 0]
    number = 0

    while number != len(answers):
        tester1.append([1,2,3,4,5][((number)%5)])
        tester2.append([2,1,2,3,2,4,2,5][((number)%8)])
        tester3.append([3,3,1,1,2,2,4,4,5,5][((number)%10)])

        if tester1[number] == answers[number]:
            score_testers[0] += 1
        if tester2[number] == answers[number]:
            score_testers[1] += 1
        if tester3[number] == answers[number]:
            score_testers[2] += 1

        number += 1

    top_score = max(score_testers)
    if score_testers[0] == top_score:
        answer.append(1)
    if score_testers[1] == top_score:
        answer.append(2)
    if score_testers[2] == top_score:
        answer.append(3)

    return answer
