import numpy as np
from PIL import Image
from typing import List
from colorama import Fore, Style
from .base import BaseModel


class AttackModel(BaseModel):
 
    def inference(self, feat: np.ndarray) -> List[Image.Image]:
        feat = feat[np.newaxis,...] if feat.ndim == 1 else feat # Add a batch dimension if the input is a single feature
        assert feat.shape[1] == self.input_shape[1], Fore.RED + f"✗ The input shape {feat.shape} is invalid." + Style.RESET_ALL
        outputs = self.session.run(None, {self.input_name: feat})[0]
        outputs = (outputs * 255.0).transpose(0, 2, 3, 1).astype(np.uint8) # Turn to (NHWC,u8)
        return [ Image.fromarray(output) for output in outputs ]