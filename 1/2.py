#!/usr/bin/env python3

import re


class SwearDetector:
    def __init__(self, data_string: str):
        if not isinstance(data_string, str):
            raise TypeError("data_string must be a str type")
        self.data = data_string

    def censor(self):
        res = re.sub(
            r"^chuj|kurwa|dupa|jeban[aey]|jeba[ćł]",
            "---",
            self.data,
            flags=re.IGNORECASE,
        )
        return res


if __name__ == "__main__":
    data = "Chuj kurwa dupa jebać jebany. Coś innego, jakiś test, bez przekleństw."
    detector = SwearDetector(data)
    res = detector.censor()
    print(res)
