from pydantic import BaseModel
from typing import Dict, List


class Payload(BaseModel):
    user_query: List[Dict]