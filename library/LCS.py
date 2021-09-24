def LCS(s1, s2):
    """
    s1,s2の最長共通部分の長さのみ求める。部分列はわからない
    """
    dp = []
    for s2_k in s2:
        bgn_idx = 0
        for i, cur_idx in enumerate(dp):
            chr_idx = s1.find(s2_k, bgn_idx) + 1
            if not chr_idx:
                break
            dp[i] = min(cur_idx, chr_idx)
            bgn_idx = cur_idx
        else:
            chr_idx = s1.find(s2_k, bgn_idx) + 1
            if chr_idx:
                dp.append(chr_idx)
    return len(dp)