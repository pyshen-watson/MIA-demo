python main_single.py \
    -t assets/weights/mbf_large_v1.onnx \
    -a assets/weights/attack_idiap_v3.onnx \
    -i assets/images/0.jpg \
    -o assets/outputs/single/1v3 \
    -v
python main_single.py \
    -t assets/weights/mbf_large_v2.onnx \
    -a assets/weights/attack_idiap_v3.onnx \
    -i assets/images/0.jpg \
    -o assets/outputs/single/2v3 \
    -v
python main_single.py \
    -t assets/weights/mbf_large_v3.onnx \
    -a assets/weights/attack_idiap_v3.onnx \
    -i assets/images/0.jpg \
    -o assets/outputs/single/3v3 \
    -v