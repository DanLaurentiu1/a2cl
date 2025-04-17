from typing import List, Literal, Tuple, Optional
from pydantic import BaseModel
from enum import Enum

DifficultyLevel = Literal[0, 1, 2]

class TopicTypes(str, Enum):
    DATA_STRUCTURES = "DataStructures"
    ALGORITHMS = "Algorithms"
    CONCEPTS = "Concepts"
    MISCELLANEOUS = "Miscellaneous"

class TopicJSON(BaseModel):
    name: str
    type: TopicTypes

class ProblemJSON(BaseModel):
    id: int
    name: str
    topics: List[TopicJSON]
    difficulty: DifficultyLevel
    acceptanceRate: float

class ProfileJSON(BaseModel):
    name: str
    proficiencies: List[Tuple[TopicJSON, int]]

class PlanJSON(BaseModel):
    id: int
    title: str
    profile: ProfileJSON
    problems: List[Tuple[bool, ProblemJSON]]
    topics: Optional[List[TopicJSON]] = None

class UpdatePlanProblemsRequest(BaseModel):
    problems: List[Tuple[bool, ProblemJSON]]