class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return (C - A) * (D - B) + (G - E) * (H - F) - max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))
