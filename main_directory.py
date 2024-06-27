import numpy as np
from PIL import Image
from pathlib import Path
from colorama import Fore, Style
from argparse import ArgumentParser

from models import TargetModel, AttackModel
from visualize import visualize_feat, save_fig

def get_args():
    parser = ArgumentParser()
    parser.add_argument( "-t", "--target_path",   type=str, required=True, help="The path to the target model" ) 
    parser.add_argument( "-a", "--attack_path",   type=str, required=True, help="The path to the attack model" )
    parser.add_argument( "-i", "--input_dir",  type=str, required=True, help="The path to the directory of input images") 
    parser.add_argument( "-o", "--output_dir", type=str, required=True, help="The path to the directory of output images") 
    parser.add_argument( "-v", "--verbose", action="store_true", default=False, help="Save all the results")
    return parser.parse_args()

if __name__ == "__main__":
    
    args = get_args()
    target_path = Path(args.target_path)
    attack_path = Path(args.attack_path)
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    
    # Load the models
    target_model = TargetModel(target_path)
    attack_model = AttackModel(attack_path)
    
    # Inference
    img_paths = list(input_dir.glob("*.jpg"))
    imgs = [ Image.open(path) for path in img_paths ]
    feats = target_model.inference(imgs)
    rec_imgs = attack_model.inference(feats)
    
    for path, img, feat, rec_img in zip(img_paths, imgs, feats, rec_imgs):
        
        # In verbose mode, save all the details in a separate directory
        save_dir = output_dir / f"{path.stem}" if args.verbose else output_dir
        save_dir.mkdir(parents=True, exist_ok=True)
        feat_img = visualize_feat(feat)
        
        # Save the details in verbose mode
        if args.verbose:
            img.save(save_dir / "original.jpg")
            feat_img.save(save_dir / "feature.jpg")
            rec_img.save(save_dir / "reconstructed.jpg")
            np.save(save_dir / "feature.npy", feat)
        
        save_fig(imgs=[img, feat_img, rec_img], 
            target_name=target_path.stem, 
            attack_name=attack_path.stem, 
            save_path=save_dir / f"result-{path.stem}.jpg")
        
        print(f"{Fore.GREEN}✓ The results have been saved at {save_dir}.{Style.RESET_ALL}")
        