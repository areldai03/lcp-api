from abc import ABC, abstractmethod

class DifficultyEstimator(ABC):
    @abstractmethod
    def estimate(self, text: str) -> dict:
        pass
