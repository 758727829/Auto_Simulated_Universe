import os
from typing import List


class Config:
    def __init__(self):
        self.order_text = "1 2 3 4"
        self.angle = "1.0"
        self.difficult = "2"
        self.allow_difficult = [1, 2, 3, 4, 5]
        self.text = "info.txt"
        self.read()

    @property
    def multi(self) -> float:
        return float(self.angle)

    @property
    def order(self) -> List[int]:
        return [int(i) for i in self.order_text.split(" ")]

    @property
    def diffi(self) -> int:
        return int(self.difficult) if int(self.difficult) in self.allow_difficult else 1

    def read(self):
        if os.path.exists(self.text):
            with open(self.text, "r", encoding="utf-8") as f:
                self.order_text = f.readline().strip()
                self.angle = f.readline().strip()
                try:
                    self.difficult = str(int(f.readline().strip()))
                except:
                    pass
        else:
            self.save()

    def save(self):
        with open(self.text, "w", encoding="utf-8") as f:
            f.write(f"{self.order_text}\n{self.angle}\n{self.diffi}")


config = Config()
