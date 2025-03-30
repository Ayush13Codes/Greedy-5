class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # T: O(m + n), S: O(1)
        s_ptr, p_ptr = 0, 0
        star_idx, match_idx = -1, -1
        m, n = len(s), len(p)

        while s_ptr < m:
            if p_ptr < n and (p[p_ptr] == s[s_ptr] or p[p_ptr] == "?"):
                # Character match or '?', move both pointers
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < n and p[p_ptr] == "*":
                # '*' encountered: store position and match index
                star_idx = p_ptr
                match_idx = s_ptr
                p_ptr += 1
            elif star_idx != -1:
                # Mismatch: backtrack to last '*' and match one more character
                p_ptr = star_idx + 1
                match_idx += 1
                s_ptr = match_idx
            else:
                # Mismatch and no '*' to use
                return False

        # If p still has '*', move p_ptr to end
        while p_ptr < n and p[p_ptr] == "*":
            p_ptr += 1

        return p_ptr == n  # True if we've matched everything
