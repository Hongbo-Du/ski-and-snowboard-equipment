from abstract import Equipment
import parameter as param
import csv
import math
import os

class Snowboard(Equipment):
    _CHART_DATA = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if Snowboard._CHART_DATA is None:
            Snowboard._CHART_DATA = self._load_chart_data()

    def _load_chart_data(self):
        data = []
        csv_path = os.path.join(os.path.dirname(__file__), 'snowboard_size_chart.csv')
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    h = float(row['height'])
                    w = float(row['weight'])
                    l = float(row['length'])
                    data.append((h, w, l))
                except ValueError:
                    continue
        return data

    def _lookup_chart_length(self):
        best_length = None
        best_dist = float('inf')
        for (h, w, length) in Snowboard._CHART_DATA:
            dist = math.sqrt((self.height - h)**2 + (self.weight - w)**2)
            if dist < best_dist:
                best_dist = dist
                best_length = length
        if best_length is None:
            best_length = self.height * 0.9
        return best_length

    def _apply_style_offset(self, base_length):
        offset = param.SNOWBOARD_STYLE_OFFSETS.get(self.style, 0)
        return base_length + offset

    def _binding_stiffness(self):
        stiffness_map = {
            'beginner': "soft",
            'intermediate': "medium",
            'advanced': "stiff",
            'expert': "very stiff"
        }
        return stiffness_map.get(self.skill_level, "medium")

    def recommend(self):
        base_length = self._lookup_chart_length()
        tuned_length = self._apply_style_offset(base_length)
        binding_stiffness = self._binding_stiffness()

        result = {
            "recommended_snowboard_length_cm": round(tuned_length, 1),
            "binding_stiffness": binding_stiffness
        }
        if self.preferred_type:
            result["user_preferred_type"] = self.preferred_type
        return result
