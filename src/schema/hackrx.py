from pydantic import BaseModel, Field, HttpUrl
from typing import List,Dict,Union,Any
class HackRxRunRequest(BaseModel):
    """
    Request model for running a HackRx task.
    """
    documents: Union[HttpUrl,List[HttpUrl]] = Field(
        ...,
        description="List of document URLs to process. Can be a single URL or a list of URLs."
    )
    questions: List[str] = Field(
        ...,
        description="List of questions to ask about the documents."
    )
class HackRxRunResponse(BaseModel):
    """
    Response model for HackRx task results.
    """
    answers: List[str] = Field(
        ...,
        description="List of answers corresponding to the questions asked."
    )