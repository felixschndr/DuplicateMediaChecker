import dataclasses


@dataclasses.dataclass
class Media:
    path: str
    file_size: float
    height: int
    width: int


@dataclasses.dataclass
class Image(Media):
    pass

@dataclasses.dataclass
class Video(Media):
    length: int