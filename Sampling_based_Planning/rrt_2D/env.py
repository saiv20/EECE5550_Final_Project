"""
Environment for rrt_2D
@author: huiming zhou
"""


class Env:
    def __init__(self):
        self.x_range = (0, 50)
        self.y_range = (0, 30)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 1, 30],
            [0, 30, 50, 1],
            [1, 0, 50, 1],
            [50, 1, 1, 30]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        #Random Obstacles
        obs_rectangle = [
            [14, 12, 8, 2],
            [18, 22, 8, 3],
            [26, 7, 2, 12],
            [32, 14, 10, 2]
        ]
        #Enclosure
        #obs_rectangle = [[14, 21, 6, 2],  # Vertical bar of the reverse C
        #    [14, 12, 6, 2],  # Horizontal bar of the reverse C
        #    [20, 12, 2, 11]]  # Connection between bars
        #Narrow
        #obs_rectangle = [[20, 10, 5, 5],[20, 17, 5, 15]] #Replace 10 and 5 by 0 and 15 for full closed scenario
        #No Obstacles
        #obs_rectangle = []
        #Symmetric
        '''
        side_length = 4
        gap = 2
        num_squares_per_row = 3
        obs_rectangle = []

        for i in range(num_squares_per_row):
            for j in range(num_squares_per_row):
                x = i * (side_length + gap) + 12  # Adjust starting x-coordinate
                y = j * (side_length + gap) + 12  # Adjust starting y-coordinate
                obs_rectangle.append([x, y, side_length, side_length])
        '''
        return obs_rectangle

    @staticmethod
    def obs_circle():
        obs_cir = [
            [7, 12, 3],
            [46, 20, 2],
            [15, 5, 2],
            [37, 7, 3],
            [37, 23, 3]
        ]
        #obs_cir = []
        return obs_cir
