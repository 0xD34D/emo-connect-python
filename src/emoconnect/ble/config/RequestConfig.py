
from dataclasses import dataclass
import json


@dataclass
class RequestConfig:
    requestType: str
    data: list[int]

    def toJson(self) -> str:
        return json.dumps({'data': self.data})
