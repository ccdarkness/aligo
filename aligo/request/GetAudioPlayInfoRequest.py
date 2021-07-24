"""..."""
from dataclasses import dataclass

from aligo.types import DataClass


@dataclass(unsafe_hash=True)
class GetAudioPlayInfoRequest(DataClass):
    """..."""
    file_id: str
    drive_id: str = None