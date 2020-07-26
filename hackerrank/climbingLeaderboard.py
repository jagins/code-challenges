def climbingLeaderboard(scores, alice):
    leaderboard = sorted(set(scores), reverse = True)
    length = len(leaderboard)
    result = []
    for score in alice:
        while length > 0 and score >= leaderboard[length - 1]:
            length -= 1
        result.append(length + 1)
    return result