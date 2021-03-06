from .factor import Vec, Score, Factor
from typing import List

class Wave:

    BASESCORE = 100

    def __init__(self):
        self.factors: List[MetaFactor] = []
    
    def appendFactor(self, factor: Factor, tag: int, weight=1):
        meta = MetaFactor(factor, tag)
        meta.weight = weight
        self.factors.append(meta)
        
    
    def evaluate(self, x: float, y: float) -> List[Score]:
        vec2 = Vec(x, y)
        total_score: List[Score] = []
        total_points = 0
        for meta in self.factors:
            factor = meta.factor
            weight = meta.weight
            score = factor.evaluate(vec2)
            for reason in score.reasons:
                reason.point = round(reason.point*weight*Wave.BASESCORE)
            score.total = round(score.total*weight*Wave.BASESCORE)
            score.tag = meta.tag
            total_score.append(score)
            total_points += score.total

        results = {}
        results['scores'] = total_score
        results['total_points'] = total_points
        return results

class MetaFactor:
    def __init__(self, factor: Factor, tag: int):
        self.factor = factor
        self.weight = 1
        self.tag = tag