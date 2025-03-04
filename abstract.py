from abc import ABC, abstractmethod

class Equipment(ABC):
    def __init__(
        self,
        height,
        weight,
        shoe_size,
        skill_level,
        terrain=None,
        style=None,
        preferred_type=None,
        age=None
    ):
        self.height = float(height)
        self.weight = float(weight)
        self.shoe_size = shoe_size
        self.skill_level = skill_level.lower()
        self.terrain = (terrain.lower() if terrain else "all mountain")
        self.style = (style.lower() if style else "average")
        self.preferred_type = preferred_type
        self.age = age

    @abstractmethod
    def recommend(self):
        pass
