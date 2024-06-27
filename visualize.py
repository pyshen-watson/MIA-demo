from typing import List
import numpy as np
from PIL import Image
from pathlib import Path
from matplotlib import pyplot as plt

def visualize_feat(feat:np.ndarray) -> Image.Image:
    size = np.sqrt(feat.shape[0]).astype(int) 
    feat = feat[:size*size].reshape(size, size) # Trim the feature map to a square
    feat = (feat - feat.min()) / (feat.max() - feat.min()) * 255 # Normalize the feature map to 0~255
    return Image.fromarray(feat.astype(np.uint8))

def save_fig(imgs: List[Image.Image], target_name:str, attack_name:str, save_path: Path):
    
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    titles = ["Original Image", f"Feature Map\nby {target_name}", f"Reconstructed Image\nby {attack_name}"]
    
    for i in range(3):
        ax[i].imshow(imgs[i])
        ax[i].set_title(titles[i])
        ax[i].axis("off")
    
    plt.savefig(save_path)
    plt.close()