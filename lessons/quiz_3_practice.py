"""Practice class and function writing for quiz 3."""

from __future__ import annotations

class ChristmasTreeFarm:

    plots: list[int] = []

    def __init__(self, plot: int, initial_planting: int = 1):
        self.plots: list[int] = []
        initial_planting = 1
        self.plot = plot
        self.initial_planting = initial_planting

    def plant(self, plot_idx: int):
        if plots[plot_idx] > 1:
            plots[plot_idx] = 1

    def growth(self, plots: list[int]):
        idx: int = 0
        for element in plots:
            plots[idx] += 1
            idx += 1

    def harvest(self, replant: bool, plots: list[int]) -> int:
        idx: int = 0
        count: int = 0
        for element in plots:
            if plots[idx] >= 5:
                plots[idx] = 1
                idx += 1
                replant = True
            if replant == True:
                count += 1
        return count
    
    def __add__(self) -> ChristmasTreeFarm:
        new_ChristmasTreeFarm: ChristmasTreeFarm = ChristmasTreeFarm(plots += plot, initial_planting += count)
        return new_ChristmasTreeFarm


class Course:
    name: str
    level: int
    prerequisites: list[str]

    def find_courses(self, course_list: list[Course], prereq: str) -> list[str]:
        return_list: list[str] = []
        level: int
        if prereq in self.prerequisites and level >= 400:
            
    def is_valid_course(self, prereq: str) -> bool:
        if self.level < 400:
            return False
        else:
            for p in self.prerequisites:
                if p == prereq
                return True
            return False