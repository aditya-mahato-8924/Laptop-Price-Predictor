from pydantic import BaseModel, Field
from typing import Annotated


class LaptopData(BaseModel):
    Company: Annotated[str, Field(..., description='Manufacturing Company of the laptop', examples=['Asus'])]
    TypeName: Annotated[str, Field(... , description='Name of the laptop type', examples=['Ultrabook'])]
    Ram: Annotated[int, Field(..., description='Ram present in the laptop in GB', min=2, gt=0, examples=[8])]
    Weight: Annotated[float, Field(..., description='Weight of the laptop in Kg', gt=0, examples=[2.03])]
    Touchscreen:  Annotated[int, Field(..., description='Whether the laptop has touchscreen or not', ge=0, le=1, examples=[0])]
    IPSpanel:  Annotated[int, Field(..., description='Whether the laptop has IPS panel or not', ge=0, le=1, examples=[1])]
    PPI: Annotated[float, Field(..., description='PPI of the laptop', gt= 0, examples=[240.2])]
    RetinaDisplay: Annotated[int, Field(..., description='Whether the laptop has RetinaDisplay or not', ge=0, le=1, examples=[0])]
    CPU_freq: Annotated[float, Field(..., description='Frequency of the CPU', gt=0, examples=[2.8])]
    CPU_brand: Annotated[str, Field(..., description='Brand of the CPU', examples=['Intel'])]
    Processor: Annotated[str, Field(..., description='Processor present in the laptop', examples=['core i5'])]
    OS: Annotated[str, Field(...,  description='OS of the laptop', examples=['Windows'])]
    GPU_brand:  Annotated[str, Field(..., description='Brand of the GPU', examples=['Intel'])]
    PrimaryStorage: Annotated[float, Field(..., description='Primary storage in GB of the laptop', gt=0, examples=[512.0])]
    SecondaryStorage: Annotated[float, Field(..., description='Secondary storage in GB of the laptop', ge=0, examples=[0.0])]
    PrimaryStorageType: Annotated[str, Field(..., description='Primary storage type of the laptop', examples=['SSD'])]
    SecondaryStorageType: Annotated[str, Field(..., description='Secondary storage type of the laptop', examples=['No'])]
    