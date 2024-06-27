import onnx
from pathlib import Path
from typing import Union
from colorama import Fore, Style
from onnxruntime import InferenceSession


class BaseModel:
    
    def __init__(self, model_path: Union[str, Path]):
        self.session = self._get_session(model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.input_shape = self.session.get_inputs()[0].shape

    def _get_session(self, model_path: Union[str, Path]):
        try:
            onnx_model = onnx.load(model_path)
            onnx.checker.check_model(onnx_model)
            print(Fore.GREEN + f"✓ ONNX model is loaded successfully from {model_path}." + Style.RESET_ALL)
            
        except Exception as e:
            raise Exception(Fore.RED + f"✗ Fail to load ONNX model from {model_path}. {e}" + Style.RESET_ALL)

        return InferenceSession(model_path, providers=["CPUExecutionProvider"])  # Use CPU for inference in our case
  