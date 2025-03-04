from abstract import Equipment
import parameter as param
import re

class Ski(Equipment):
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
        super().__init__(height, weight, shoe_size, skill_level, terrain, style, preferred_type, age)
        self.height = float(height)
        self.weight = float(weight)
        self.terrain = (terrain.lower() if terrain else "all mountain")
        self.style = (style.lower() if style else "average")
        self.skill_level = skill_level.lower()
        self.age = age

    def recommend(self):
        ski_length = self._calculate_length()
        din_value, din_code = self._calculate_din()

        result = {
            "recommended_ski_length_cm": round(ski_length, 1),
            "din_setting": round(din_value, 1),
            "din_code": din_code
        }
        if self.preferred_type:
            result["user_preferred_type"] = self.preferred_type
        return result

    def _calculate_length(self):
        ability_offset = param.ABILITY_OFFSET.get(self.skill_level, 0)
        terrain_offset = param.TERRAIN_OFFSET.get(self.terrain, 0)
        style_offset = param.STYLE_OFFSET.get(self.style, 0)

        base_length = self.height + ability_offset + terrain_offset + style_offset

        if (self.weight / self.height) < param.UNDERWEIGHT_RATIO:
            base_length -= 5

        return base_length

    def _get_initial_skier_code(self, kg):
        for boundary, code in param.WEIGHT_TO_CODE:
            if kg <= boundary:
                return code
        return "P"

    def _shift_code(self, code, shift):
        codes = param.CODES_ORDER
        idx = codes.index(code)
        new_idx = idx + shift
        if new_idx < 0:
            new_idx = 0
        elif new_idx >= len(codes):
            new_idx = len(codes) - 1
        return codes[new_idx]

    def _calculate_din(self):
        code = self._get_initial_skier_code(self.weight)
        if self.age is not None and (self.age < 10 or self.age >= 50):
            code = self._shift_code(code, -1)
        skill_shift = param.SKILL_CODE_OFFSET.get(self.skill_level, 0)
        code = self._shift_code(code, skill_shift)
        final_din = param.CODE_TO_DIN_271_290.get(code, 3.0)
        return final_din, code
