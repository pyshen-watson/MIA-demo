import numpy as np
from PIL import Image
from typing import Union, List
from .base import BaseModel

class TargetModel(BaseModel):

    def inference(self, inputs: Union[Image.Image, List[Image.Image]]):
        """
        Input: Single or multiple PIL.Image object(s)
        Output: A np.ndarray in the shape of (N, 512)
        """
        
        # Uniform the input type to a list
        if isinstance(inputs, Image.Image):
            inputs = [inputs]
        
        # Turn the image from PIL.Image (NHWC,u8) to np.ndarray (NCHW,f32)
        n, c, h, w = self.input_shape
        inputs = [ img.convert("RGB").resize((w, h)) for img in inputs ]
        np_img = np.stack(inputs).astype(np.float32).transpose(0, 3, 1, 2) / 255.0

        # Inferencing
        return self.session.run(None, {self.input_name: np_img})[0] # (N, 512)