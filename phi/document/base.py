from typing import Optional, Dict, Any, List

from pydantic import BaseModel, ConfigDict

from phi.embedder import Embedder


class Document(BaseModel):
    """Model for managing a document"""

    content: str
    name: Optional[str] = None
    page: Optional[int] = None
    meta_data: Dict[str, Any] = {}
    embedder: Optional[Embedder] = None
    embedding: Optional[List[float]] = None
    usage: Optional[Dict[str, Any]] = None

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def embed(self, embedder: Optional[Embedder] = None) -> None:
        """Embed the document using the provided embedder"""

        _embedder = embedder or self.embedder
        if _embedder is None:
            raise ValueError("No embedder provided")

        self.embedding, self.usage = _embedder.get_embedding_and_usage(self.content)
