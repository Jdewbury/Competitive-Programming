class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color: 
            return image
        
        def fill_pixel(image, target, color, sr, sc):
            if sc < 0 or sc >= len(image[0]) or sr < 0 or sr >= len(image):
                return
            if image[sr][sc] != target:
                return

            image[sr][sc] = color
            # recursively iterate on neighboring pixels
            fill_pixel(image, target, color, sr-1, sc)
            fill_pixel(image, target, color, sr+1, sc)
            fill_pixel(image, target, color, sr, sc-1)
            fill_pixel(image, target, color, sr, sc+1)
        
        fill_pixel(image, image[sr][sc], color, sr, sc)

        return image