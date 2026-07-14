class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        pos_and_sp = []

        for p, s in zip(position, speed):
            pos_and_sp.append((p,s))

        pos_and_sp.sort()

        curr_pos, curr_speed = pos_and_sp.pop()
        curr_car_reach_time = (target - curr_pos) / curr_speed
        res += 1

        while pos_and_sp:
            pos, speed = pos_and_sp.pop()
            reach_time = (target - pos) / speed

            if reach_time <= curr_car_reach_time:
                continue
            else:
                res += 1
                curr_pos, curr_speed = pos, speed
                curr_car_reach_time = (target - curr_pos) / curr_speed
        
        return res





